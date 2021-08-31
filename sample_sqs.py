import localstack_client.session as boto3

client = boto3.client('sqs')
print(client.list_queues())
# response = client.create_queue(
#     QueueName='test_queue2',
#     Attributes={
#         'string': 'string'
#     },
#     tags={
#         'string': 'string'
#     }
# )

