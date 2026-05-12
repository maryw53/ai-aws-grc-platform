# AI AWS GRC Platform

AI AWS GRC Platform is an AWS-focused cloud governance and compliance project that uses AWS security services, event-driven automation, and Amazon Bedrock to analyze security findings and generate remediation guidance.

The goal of the project is to simulate how modern cloud governance teams can automate parts of security monitoring, compliance reporting, and risk analysis in AWS environments.

## Current Focus

The current implementation focuses on:
- Security Hub findings ingestion
- event-driven workflows using EventBridge and Lambda
- AI-assisted finding summarization with Amazon Bedrock
- sample compliance and security workflows
- governance-oriented reporting structure

Additional integrations for Macie, Inspector, and AWS Config are planned.

## Architecture Overview

The platform follows an event-driven AWS architecture.

1. AWS services generate findings
2. EventBridge routes events
3. Lambda functions process findings
4. Findings are normalized and stored
5. Amazon Bedrock generates summaries and remediation guidance
6. Dashboards and reports display governance posture

## AWS Services Used

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
- AWS IAM

## Example Workflow

Example:
A public S3 bucket is detected by Security Hub.

Workflow:
1. Security Hub generates a finding
2. EventBridge triggers a Lambda function
3. Lambda normalizes the finding
4. Bedrock analyzes compliance impact
5. Remediation guidance is generated
6. Evidence is stored for reporting workflows

## Project Structure

```text
docs/               Architecture and project documentation
backend/            Lambda workflows and APIs
frontend/           Dashboard application
infrastructure/     Terraform and CloudFormation templates
samples/            Example AWS findings
scripts/            Utility scripts
tests/              Unit and integration tests
