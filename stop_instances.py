import json
import boto3
import os

def lambda_handler(event, context):
    ec2 = boto3.client('ec2')

    response = ec2.describe_instances(
        Filters=[{'Name': 'instance-state-name', 'Values': ['running']}]
    )

    instances_to_stop = []
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            # Add your logic to decide which instances to stop
            if instance['InstanceId']:  # Example check; replace with your criteria
                instances_to_stop.append(instance['InstanceId'])

    if instances_to_stop:
        ec2.stop_instances(InstanceIds=instances_to_stop)
        return {
            'statusCode': 200,
            'body': json.dumps(f'Stopped instances: {instances_to_stop}')
        }
    else:
        return {
            'statusCode': 200,
            'body': json.dumps('No instances to stop')
        }