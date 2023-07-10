#!/usr/bin/env python3
import os
import aws_cdk as cdk

from aws_cdk import (
    aws_backup as backupService, 
)

from constructs import Construct

class BackupPlanStack(cdk.Stack):
    def __init__(self, scope: Construct, id: str, ec2_stack, **kwargs):
        super().__init__(scope, id, **kwargs)

        web_server = ec2_stack.web_server

        # Use the app_prd_vpc and security_group_rds as needed in the BackupPlanStack
        vault = backupService.BackupVault(self, "Webserver_BackupVault", backup_vault_name="Webserver_Backup_Vault")

        # Create a BackupPlan
        plan = backupService.BackupPlan(self, "AWS-Webserver_Backup-Plan", backup_plan_name="Webserver_Backup")
        
        # Select which resources to backup
        plan.add_selection("Selection", resources=[
            backupService.BackupResource.from_ec2_instance(web_server),
        ])
        
        # Plan: backup.BackupPlan
        plan.add_rule(backupService.BackupPlanRule(
            backup_vault=vault,
            rule_name="Webserver_Backup_Rule",
            completion_window=cdk.Duration.hours(2),
            start_window=cdk.Duration.hours(1),
            enable_continuous_backup=True,
            delete_after=cdk.Duration.days(7),
            schedule_expression=cdk.aws_events.Schedule.cron(
                minute='0',
                hour='20')
        ))