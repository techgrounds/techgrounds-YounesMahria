import aws_cdk as core
import aws_cdk.assertions as assertions

from the_mvp_project.the_mvp_project_stack import TheMvpProjectStack

# example tests. To run these tests, uncomment this file along with the example
# resource in the_mvp_project/the_mvp_project_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = TheMvpProjectStack(app, "the-mvp-project")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
