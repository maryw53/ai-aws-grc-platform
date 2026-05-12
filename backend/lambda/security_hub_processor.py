import json


def lambda_handler(event, context):
    """
    Processes sample AWS Security Hub findings.

    Future versions will:
    - normalize findings
    - send findings to Amazon Bedrock
    - store evidence
    - generate remediation guidance
    """

    finding = extract_finding(event)

    response = {
        "resource": finding.get("resource"),
        "severity": finding.get("severity"),
        "description": finding.get("description"),
        "status": "processed"
    }

    return {
        "statusCode": 200,
        "body": json.dumps(response)
    }


def extract_finding(event):
    return {
        "resource": event.get("resource", "unknown-resource"),
        "severity": event.get("severity", "UNKNOWN"),
        "description": event.get("description", "No description provided")
    }
