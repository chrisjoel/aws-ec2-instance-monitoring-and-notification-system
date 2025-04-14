# aws-ec2-instance-monitoring-and-notification-system

## Date: 14/04/2025

## Overview

    This AWS Lambda function monitors running EC2 instances and sends alerts via SNS if costs exceed a specified limit or if free tier usage thresholds are reached. It uses the Boto3 library to interact with AWS services.

## Prerequisites

    1. AWS account with EC2 and SNS permissions
    2. Python 3.x
    3. Boto3 library

## Architecture

## Environment variable for the lambda

    COST_LIMIT=xxx
    FREE_TIER_LIMIT=xxx
    SNS_TOPIC_ARN=arn:aws:sns:REGION:ACCOUNT_ID:xxxx
    STOP_FUNCTION_NAME=xxx_xxx_xxxx
