import json
import boto3
import os

def lambda_handler(event, context):
    ec2 = boto3.client('ec2')
    sns = boto3.client('sns')
    lambda_client = boto3.client('lambda')

    response = ec2.describe_instances(
        Filters=[{'Name': 'instance-state-name', 'Values': ['running']}]
    )
    running_instances = sum(len(res['Instances']) for res in response['Reservations'])

    # Get environment variables with fallback defaults
    cost_limit = float(os.getenv('COST_LIMIT', '5.00'))  
    free_tier_limit = int(os.getenv('FREE_TIER_LIMIT', '730')) 

    # Example cost calculation (update the rate as needed)
    current_cost = running_instances * 0.004  

    # Check if current cost exceeds the limit
    if current_cost > cost_limit:
        sns.publish(
            TopicArn=os.getenv('SNS_TOPIC_ARN'),  # Environment variable for SNS topic ARN
            Message=f'Alert: Your current cost has reached ${current_cost:.2f}.',
            Subject='Cost Alert'
        )
        # Invoke the stop function asynchronously
        lambda_client.invoke(
            FunctionName=os.getenv('STOP_FUNCTION_NAME'),  # Environment variable for stop function name
            InvocationType='Event'
        )

    # Check if running instances exceed the free tier limit
    if running_instances > free_tier_limit:
        sns.publish(
            TopicArn=os.getenv('SNS_TOPIC_ARN'),
            Message=f'Alert: You have exceeded your free tier limit with {running_instances} running instances.',
            Subject='Free Tier Alert'
        )

    return {
        'statusCode': 200,
        'body': json.dumps('Check completed!')
    }