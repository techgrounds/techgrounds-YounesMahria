import aws_cdk as cdk
from stack.my_stack import TheMvpProjectStack

app = cdk.App()


app.default_env = cdk.Environment(region='eu-central-1') # Define your default region
env_EU = cdk.Environment(region="eu-central-1") # Define your region

# Deploy your stack
TheMvpProjectStack(app, 'TheMvpProjectStack', env=env_EU)
app.synth()