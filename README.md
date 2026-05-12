# Architecture

AI AWS GRC Platform uses an event-driven AWS architecture to collect, normalize, analyze, and report cloud governance findings.

## Core Workflow

1. AWS services generate findings
2. EventBridge routes events
3. Lambda processes findings
4. Bedrock analyzes risk
5. Evidence stored in S3/DynamoDB
6. Dashboards and reports updated
