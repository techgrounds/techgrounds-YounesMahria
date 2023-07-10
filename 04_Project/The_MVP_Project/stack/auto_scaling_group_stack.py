#!/usr/bin/env python3
import os

import aws_cdk as cdk

from aws_cdk import (
    aws_ec2 as ec2,
    aws_autoscaling as autoscaling,
    aws_elasticloadbalancingv2 as elbv2,
    aws_elasticloadbalancingv2_targets as targets,
    aws_certificatemanager as acm,
    aws_cloudwatch as cloudwatch,
    
    App, CfnOutput, Duration, Stack, 

)

from constructs import Construct


from stack._variables import (
    AMAZ_INSTANCE_TYPE,
    AMAZ_LINUX,
    #USER_DATA,
    AMAZ_WINDOWS,
    COOLDOWN
)

class AutoScalingGroupStack(cdk.Stack):
    def __init__(self, scope: Construct, id: str, vpc_stack, security_group_stack, ec2_stack, iam_stack, ssh_stack, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        app_prd_vpc = vpc_stack.app_prd_vpc
        management_prd_vpc = vpc_stack.management_prd_vpc
        security_group_web_server = security_group_stack.security_group_web_server
        security_group_rds = security_group_stack.security_group_rds
        #web_server = ec2_stack.web_server
        ec2_app_prd_key = ssh_stack.ec2_app_prd_key
        ec2_app_prd_key_pair = ssh_stack.ec2_app_prd_key_pair
        ec2_management_prd_key = ssh_stack.ec2_management_prd_key
        ec2_management_prd_key_pair = ssh_stack.ec2_management_prd_key_pair
        app_product_role = iam_stack.app_product_role
        management_server_role = iam_stack.management_server_role


        # Read the contents of the user data file
        with open('userdata/web-server-user-data.sh', 'r') as file:
            web_server_user_data = file.read()

        # Create a UserData object from the file contents
        web_server_user_data_object = ec2.UserData.custom(web_server_user_data)

        USER_DATA = web_server_user_data_object

        """
        # Create an Auto Scaling group for the web server instances
        web_server_auto_scaling_group = autoscaling.AutoScalingGroup(self, "AutoScalingGroup",
            vpc=app_prd_vpc,
            auto_scaling_group_name="web-server",
            instance_type=ec2.InstanceType(AMAZ_INSTANCE_TYPE),
            machine_image=AMAZ_LINUX,
            key_name=ec2_app_prd_key,
            security_group=security_group_web_server,
            user_data=USER_DATA,
            vpc_subnets=ec2.SubnetSelection(subnet_type=ec2.SubnetType.PRIVATE_WITH_EGRESS),
            block_devices=[
                autoscaling.BlockDevice(
                    device_name='/dev/xvda',
                    volume=autoscaling.BlockDeviceVolume.ebs(
                        volume_size=8,
                        encrypted=True,
                    )
                )
            ],
            role=app_product_role,
            min_capacity=1,
            max_capacity=3,
            health_check=autoscaling.HealthCheck.ec2(
                grace=cdk.Duration.seconds(60)
            )
        )
        """
        
        # Create an Auto Scaling group
        web_server_auto_scaling_group = autoscaling.AutoScalingGroup(
            self,
            "AutoScalingGroup",
            auto_scaling_group_name="Cloud10WebServerASG",
            vpc=app_prd_vpc,
            instance_type=ec2.InstanceType.of(ec2.InstanceClass.BURSTABLE3, ec2.InstanceSize.MICRO),
            machine_image=ec2.AmazonLinuxImage(generation=ec2.AmazonLinuxGeneration.AMAZON_LINUX_2),
            user_data=USER_DATA,
            security_group=security_group_web_server,
            #desired_capacity=1,
            min_capacity=1,
            max_capacity=3,
            vpc_subnets=ec2.SubnetSelection(subnet_type=ec2.SubnetType.PRIVATE_ISOLATED),
            block_devices=[
                autoscaling.BlockDevice(
                    device_name="/dev/xvda",
                    volume=autoscaling.BlockDeviceVolume.ebs(20, encrypted=True)
                )
            ],
        )


        # Tag the instances launched by the Auto Scaling group
        web_server_auto_scaling_group.node.default_child.add_property_override("Tags", [{
            "Key": "Name",
            "Value": "web_server",
            "PropagateAtLaunch": True
        }])

        """    
         
        # Create an Auto Scaling group for the web server instances
        web_server_auto_scaling_group = autoscaling.AutoScalingGroup(self, "AutoScalingGroup",
            vpc=app_prd_vpc,
            auto_scaling_group_name="web-server",
            instance_type=ec2.InstanceType(AMAZ_INSTANCE_TYPE),
            machine_image=ec2.MachineImage.generic_linux(
                {"eu-central-1": "ami-08b66382534b75845"}
            ),
            key_name=ec2_app_prd_key,
            security_group=security_group_web_server,
            user_data=USER_DATA,
            vpc_subnets=ec2.SubnetSelection(subnet_type=ec2.SubnetType.PRIVATE_ISOLATED),
            block_devices=[
                autoscaling.BlockDevice(
                    device_name='/dev/xvda',
                    volume=autoscaling.BlockDeviceVolume.ebs(
                        volume_size=8,
                        encrypted=True,
                    )
                )
            ],
            role=app_product_role,
            min_capacity=1,
            max_capacity=3,
            health_check=autoscaling.HealthCheck.ec2(
                grace=cdk.Duration.seconds(60)
            )
        )


        # Tag the instances launched by the Auto Scaling group
        web_server_auto_scaling_group.node.default_child.add_property_override("Tags", [{
            "Key": "Name",
            "Value": "web_server",
            "PropagateAtLaunch": True
        }]
        )
        """

        # Create a Metric object for the CPU utilization of the instances in the Auto Scaling group
        cpu_metric = cloudwatch.Metric(
            namespace="AWS/EC2",
            metric_name="CPUUtilization",
            dimensions_map={"AutoScalingGroupName": web_server_auto_scaling_group.auto_scaling_group_name},
            statistic="Average",
        )
        
        # Configure a step scaling policy to scale out when CPU utilization exceeds 80% or 30%
        scaling_policy = web_server_auto_scaling_group.scale_on_metric(
            "ScalingPolicy",
            metric=cpu_metric,
            scaling_steps=[
                autoscaling.ScalingInterval(upper=30, change=-1),
                autoscaling.ScalingInterval(lower=80, change=1),
            ],
            adjustment_type=autoscaling.AdjustmentType.CHANGE_IN_CAPACITY,
        )





        
        """
        # Get the underlying CfnAutoScalingGroup object (to eliminate the type error in the dependency)
        cfn_asg = web_server_auto_scaling_group.node.default_child

        # Scale up based on CPU utilization
        cpu_scale_up_policy = autoscaling.CfnScalingPolicy(
            self,
            "CpuScaleUpPolicy",
            policy_type="TargetTrackingScaling",
            auto_scaling_group_name=web_server_auto_scaling_group.auto_scaling_group_name,
            target_tracking_configuration=autoscaling.CfnScalingPolicy.TargetTrackingConfigurationProperty(
                target_value=70,
                predefined_metric_specification=autoscaling.CfnScalingPolicy.PredefinedMetricSpecificationProperty(
                    predefined_metric_type="ASGAverageCPUUtilization"
                )
            )
        )
        cpu_scale_up_policy.add_dependency(cfn_asg)

        # Scale down based on CPU utilization
        cpu_scale_down_policy = autoscaling.CfnScalingPolicy(
            self,
            "CpuScaleDownPolicy",
            policy_type="TargetTrackingScaling",
            auto_scaling_group_name=web_server_auto_scaling_group.auto_scaling_group_name,
            target_tracking_configuration=autoscaling.CfnScalingPolicy.TargetTrackingConfigurationProperty(
                target_value=50,
                predefined_metric_specification=autoscaling.CfnScalingPolicy.PredefinedMetricSpecificationProperty(
                    predefined_metric_type="ASGAverageCPUUtilization"
                )
            )
        )
        cpu_scale_down_policy.add_dependency(cfn_asg)

        # Create a CloudWatch alarm for scaling up
        cpu_utilization_high_alarm = cloudwatch.CfnAlarm(
            self,
            "CpuUtilizationHighAlarm",
            alarm_description="Scale up if CPU utilization is greater than 70 percent for 1 minute",
            comparison_operator="GreaterThanThreshold",
            evaluation_periods=1,
            metric_name="CPUUtilization",
            namespace="AWS/EC2",
            period=60, # 1 minute in seconds
            statistic="Average",
            threshold=70,
            alarm_actions=[cpu_scale_up_policy.ref],
            dimensions=[cloudwatch.CfnAlarm.DimensionProperty(name="Scaling Up", value=web_server_auto_scaling_group.auto_scaling_group_name)]
        )

        # Create a CloudWatch alarm for scaling down
        cpu_utilization_low_alarm = cloudwatch.CfnAlarm(
            self,
            "CpuUtilizationLowAlarm",
            alarm_description="Scale down if CPU utilization is low",
            comparison_operator="LessThanThreshold",
            evaluation_periods=1,
            metric_name="CPUUtilization",
            namespace="AWS/EC2",
            period=60, # 1 minute in seconds
            statistic="Average",
            threshold=50,
            alarm_actions=[cpu_scale_down_policy.ref],
            dimensions=[cloudwatch.CfnAlarm.DimensionProperty(name="Scaling Down", value=web_server_auto_scaling_group.auto_scaling_group_name)]
        )


        """
        
        
        """
        # Configure a step scaling policy to scale out when CPU utilization exceeds 80%
        scale_out_policy = web_server_auto_scaling_group.scale_on_metric(
            "ScaleOutPolicy",
            metric=cpu_metric,
            scaling_steps=[autoscaling.ScalingInterval(upper=80, change=1),],
            adjustment_type=autoscaling.AdjustmentType.CHANGE_IN_CAPACITY,
        )

        # Configure a step scaling policy to scale in when CPU utilization falls below 30%
        scale_in_policy = web_server_auto_scaling_group.scale_on_metricscale_on_metric(
            "ScaleInPolicy",
            metric=cpu_metric,
            scaling_steps=[autoscaling.ScalingInterval(lower=30, change=-1),],
            adjustment_type=autoscaling.AdjustmentType.CHANGE_IN_CAPACITY,
        )
        """

        #scale_in_policy.node.add_tags("Name", "Scale in")
        #scale_out_policy.node.add_tags("Name", "Scale Out")

                        
        self.web_server_auto_scaling_group = web_server_auto_scaling_group