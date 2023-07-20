#!/usr/bin/env python3
import os
import aws_cdk as cdk

from aws_cdk import (
    aws_backup as backup,
    aws_events as events,
    Duration
)

from constructs import Construct

class BackupPlanStack(cdk.Stack):
    def __init__(self, scope: Construct, id: str, ec2_stack, **kwargs):
        super().__init__(scope, id, **kwargs)

        management_server = ec2_stack.management_server

        # Create a backup vault
        backup_vault = backup.BackupVault(self, "Cloud10Backup",
            backup_vault_name = "TechgroundsCloud10Backup",
            removal_policy = cdk.RemovalPolicy.DESTROY
        )

        # Create a backup plan
        backup_plan = backup.BackupPlan(self, "Plan",
            backup_plan_name = "DailyBackupPlan",
            backup_vault = backup_vault,
        )

        # Add a rule to the backup plan
        backup_plan.add_rule(backup.BackupPlanRule(
            #time_zone = "Europe/Amsterdam",
            delete_after = Duration.days(7), # Retain backups for 7 days
            start_window = Duration.minutes(60),
            completion_window = Duration.minutes(120),
            schedule_expression = events.Schedule.cron(hour="20", minute="0"), # 8pm NL Amsterdam time
        ))

        # Add a selection to the backup plan using resource IDs
        backup_plan.add_selection("Selection",
            resources = [backup.BackupResource.from_ec2_instance(management_server)], # Backup this Management instance
            #role = cdk.Role.from_role_arn(self, "Role", "arn:aws:iam::123456789012:role/my-role"), # The role that AWS Backup uses to perform backups
        )