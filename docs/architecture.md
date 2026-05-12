# Architecture

## Overview

AI AWS GRC Platform uses an event-driven AWS architecture to collect, normalize, analyze, and report cloud governance findings.

## Core Workflow

1. AWS services generate security and compliance findings
2. Amazon EventBridge routes events
3. AWS Lambda processes and normalizes findings
4. Amazon Bedrock analyzes risk and compliance impact
5. Findings stored in Amazon S3 and DynamoDB
6. Dashboard and reporting services display risk posture

## AWS Services

- AWS Security Hub
- AWS Config
- AWS Lambda
- Amazon EventBridge
- Amazon Bedrock
- Amazon S3
- Amazon DynamoDB
- Amazon Inspector
- Amazon Macie
- AWS CloudTrail
- Amazon CloudWatch

## AI Layer

Amazon Bedrock is used to:
- summarize findings
- explain business impact
- generate remediation guidance
- assist with audit reporting
