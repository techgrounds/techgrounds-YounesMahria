import sys
import logging
import pymysql
import json
import os
import boto3
from botocore.exceptions import ClientError



# rds settings
user_name = os.environ['USER_NAME']
rds_host = os.environ['RDS_HOST']
db_name = os.environ['DB_NAME']

logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Retrieve the secret values from AWS Secrets Manager
secret_name = os.environ['SECRET_NAME']
region_name = "eu-central-1"

session = boto3.session.Session()
client = session.client(
    service_name="secretsmanager",
    region_name=region_name,
)

try:
    logger.info("Retrieving secret value")
    get_secret_value_response = client.get_secret_value(SecretId=secret_name)
    logger.info("Finished retrieving secret value")
except ClientError as e:
    logger.error(f"An error occurred: {e}")
    raise e

if "SecretString" in get_secret_value_response:
    secret = json.loads(get_secret_value_response["SecretString"])
    user_name = secret["username"]
    password = secret["password"]
else:
    binary_secret_data = get_secret_value_response["SecretBinary"]

try:
    logger.info("Connecting to MySQL instance")
    conn = pymysql.connect(host=rds_host, user=user_name, passwd=password, db=db_name, connect_timeout=5)
    logger.info("SUCCESS: Connection to RDS MySQL instance succeeded")
except pymysql.MySQLError as e:
    logger.error("ERROR: Unexpected error: Could not connect to MySQL instance.")
    logger.error(e)
    sys.exit()

s3 = boto3.client('s3')

def lambda_handler(event, context):
    logger.info("Starting function")

    try:
        bucket_name = event['bucket']
        file_key = event['key']

        logger.info("Starting to get S3 object")
        obj = s3.get_object(Bucket=bucket_name, Key=file_key)
        sql_file_content = obj['Body'].read().decode('utf-8')
        logger.info("Finished getting S3 object")

        logger.info("Starting to execute SQL statements")
        with conn.cursor() as cur:
            for sql_statement in sql_file_content.split(';'):
                if sql_statement.strip():  # Ignore empty statements
                    cur.execute(sql_statement)
            conn.commit()
        logger.info("Finished executing SQL statements")
        return 'Executed SQL file successfully'

    except Exception as e:
        logger.error(f"An error occurred: {e}")
        return 'Error executing SQL file'

    logger.info("Finished function")