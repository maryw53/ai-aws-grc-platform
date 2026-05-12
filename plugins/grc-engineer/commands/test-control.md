---
description: Test security control effectiveness with automated validation
---

# Test Control

Automatically tests whether security controls are properly implemented and effective. Validates configuration, functionality, and compliance with framework requirements.

## Usage

```bash
/grc-engineer:test-control <control-id> [cloud-provider] [options]
```

## Arguments

- `$1` - Control ID or name (e.g., "access_control_account_management", "AC-2", "encryption_at_rest")
- `$2` - Cloud provider (optional): `aws`, `azure`, `gcp`, `kubernetes` (default: auto-detect)
- `$3` - Options (optional): `--verbose`, `--fix-failures`, `--output=json`

## Examples

```bash
# Test access control implementation
/grc-engineer:test-control access_control_account_management

# Test encryption on AWS with verbose output
/grc-engineer:test-control encryption_at_rest aws --verbose

# Test logging and auto-fix failures
/grc-engineer:test-control logging_and_monitoring --fix-failures

# Test all controls (summary)
/grc-engineer:test-control all aws
```

## Test Categories

### 1. Configuration Tests

Validates that controls are properly configured:

- Resources exist and are enabled
- Configuration matches requirements
- Required parameters are set correctly

### 2. Functionality Tests

Verifies controls are actually working:

- Services are active and responding
- Data is being collected/protected
- Automation is functioning

### 3. Compliance Tests

Checks alignment with framework requirements:

- Meets all framework criteria
- No conflicts or gaps
- Evidence can be collected

### 4. Integration Tests

Ensures controls work together:

- Data flows correctly
- Dependencies are satisfied
- No configuration conflicts

## Output Format

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CONTROL TEST RESULTS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Control: Access Control - Account Management (AC-2)
Frameworks: NIST 800-53, ISO A.9.2, SOC2 CC6.1, PCI 8.1
Cloud Provider: AWS
Test Duration: 12.3s

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CONFIGURATION TESTS (5)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

✓ TEST 1: Unique User IDs
  Status: PASS
  Requirement: All users must have unique identifiers
  Result: 47 IAM users found, all with unique IDs
  Frameworks: All

✓ TEST 2: Access Approval Process
  Status: PASS
  Requirement: Documented approval for all user accounts
  Result: 100% of users have creator tags with approval timestamps
  Evidence: All users tagged with Creator and ApprovedBy
  Frameworks: NIST AC-2, SOC2 CC6.1

✗ TEST 3: Quarterly Access Reviews
  Status: FAIL
  Requirement: Access reviews every 90 days (PCI 8.1.4)
  Result: Last review: 2024-11-15 (92 days ago)
  Expected: Reviews within last 90 days
  Impact: PCI-DSS violation
  Frameworks: PCI-DSS 8.1.4

  Remediation:
  Run quarterly access review immediately:
  ```bash
  aws lambda invoke \
    --function-name quarterly-access-review \
    --payload '{"trigger":"manual"}' \
    response.json
  ```

  Or use automated script:

  ```bash
  python scripts/access_review.py --immediate
  ```

✓ TEST 4: Automated User Provisioning
  Status: PASS
  Requirement: Automated account lifecycle management
  Result: IAM Identity Center configured with SCIM provisioning
  Frameworks: NIST AC-2(1), SOC2 CC6.2

✓ TEST 5: Least Privilege Enforcement
  Status: PASS
  Requirement: Permissions boundaries applied
  Result: 95% of users have permissions boundaries
  Note: 2 admin users exempted (documented)
  Frameworks: NIST AC-6, SOC2 CC6.1

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
FUNCTIONALITY TESTS (5)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

✓ TEST 6: CloudTrail Logging Active
  Status: PASS
  Requirement: All account management events logged
  Result: CloudTrail active in all regions
  Events logged: 1,247 IAM events in last 24 hours
  Frameworks: NIST AU-2, SOC2 CC7.2

⚠ TEST 7: Inactive Account Detection
  Status: WARNING
  Requirement: Detect and disable accounts inactive >90 days
  Result: 3 users inactive >90 days detected

  Inactive users:

- john.doe@company.com (127 days inactive)
- jane.smith@company.com (94 days inactive)
- test.user@company.com (215 days inactive)

  Action required: Disable or justify retention
  Frameworks: PCI-DSS 8.1.4

  Remediation:

  ```bash
  # Disable inactive users
  python scripts/disable_inactive_users.py --threshold=90 --execute

  # Or review individually
  aws iam list-users | jq '.Users[] | select(.PasswordLastUsed < "2024-09-15")'
  ```

✓ TEST 8: Access Analyzer Enabled
  Status: PASS
  Requirement: Continuous unused access detection
  Result: Access Analyzer active, 0 high-priority findings
  Last scan: 2 hours ago
  Frameworks: SOC2 CC6.1, NIST AC-2(4)

✓ TEST 9: MFA Enforcement
  Status: PASS
  Requirement: Multi-factor authentication required
  Result:

- Root account: MFA enabled
- IAM users: 45/47 have MFA (96%)
- 2 service accounts exempted (no console access)
  Frameworks: NIST IA-2(1), PCI 8.3, SOC2 CC6.1

✓ TEST 10: Audit Trail Integrity
  Status: PASS
  Requirement: Tamper-proof audit logs
  Result: CloudTrail log file validation enabled
  S3 bucket: Object Lock enabled (COMPLIANCE mode)
  Frameworks: NIST AU-9, SOC2 CC7.3

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
COMPLIANCE TESTS (4)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

✓ TEST 11: Log Retention Period
  Status: PASS
  Requirement: 1 year retention (PCI 10.7, SOC2)
  Result: S3 lifecycle configured for 365 days

- Online storage: 180 days
- Glacier archive: 185 days
- Total: 365 days ✓
  Frameworks: PCI-DSS 10.7, SOC2 CC7.3, NIST AU-11

✓ TEST 12: Separation of Duties
  Status: PASS
  Requirement: Admin privileges separated
  Result: No users have both admin and auditor roles
  Frameworks: NIST AC-5, SOC2 CC6.1

✓ TEST 13: Evidence Availability
  Status: PASS
  Requirement: Evidence can be collected on demand
  Result: Evidence collection script executed successfully
  Artifacts: 5 evidence files generated (2.3 MB)
  Frameworks: All

✗ TEST 14: Access Review Documentation
  Status: FAIL
  Requirement: Documented access review process
  Result: Policy document exists but not updated in last year
  Last update: 2023-12-10
  Required: Annual updates minimum
  Frameworks: ISO A.9.2.5, SOC2 CC6.1

  Remediation:
  Update access review policy document with:

- Current review frequency (quarterly)
- Responsible parties
- Escalation procedures
- Recent review results

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
INTEGRATION TESTS (1)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

✓ TEST 15: End-to-End Account Lifecycle
  Status: PASS
  Requirement: Complete lifecycle automation
  Test scenario: Create user → Assign permissions → Review → Deactivate
  Result: All steps completed successfully

- User created with proper tags
- Permissions boundary applied
- CloudTrail events captured
- Access review flagged inactive user
- User successfully deactivated
  Frameworks: All

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
TEST SUMMARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Total Tests: 15
✓ Passed: 11 (73%)
✗ Failed: 2 (13%)
⚠ Warnings: 2 (13%)

CONTROL STATUS: PARTIALLY EFFECTIVE

Critical Issues (2):

1. Quarterly access review overdue (92 days since last review)
2. Access review policy document outdated

Warnings (2):

1. 3 inactive users detected (>90 days)
2. 2 users without MFA (service accounts)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
FRAMEWORK COMPLIANCE STATUS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

NIST 800-53 (AC-2):        ⚠ PARTIALLY COMPLIANT
  Issues: Access review overdue, documentation outdated

ISO 27001 (A.9.2):         ⚠ PARTIALLY COMPLIANT
  Issues: Documentation outdated

SOC2 (CC6.1):              ⚠ PARTIALLY COMPLIANT
  Issues: Access review overdue, documentation outdated

PCI-DSS (8.1):             ✗ NON-COMPLIANT
  Issues: Quarterly review requirement violated

Overall Assessment: Control is operational but has compliance gaps
Audit Risk: MEDIUM - Fix before audit
Remediation Priority: HIGH

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
REMEDIATION PLAN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

IMMEDIATE (Fix today):

1. Run quarterly access review
   Command: python scripts/access_review.py --immediate
   Impact: Resolves PCI-DSS violation
   Estimated time: 2 hours

2. Disable inactive users
   Command: python scripts/disable_inactive_users.py --threshold=90 --execute
   Impact: Reduces security risk
   Estimated time: 30 minutes

THIS WEEK (Fix within 7 days):
3. Update access review policy document
   Task: Review and update policy document
   Assign to: Security team lead
   Impact: Resolves SOC2/ISO documentation requirement
   Estimated time: 4 hours

VERIFICATION:
After remediation, re-run test:
  /grc-engineer:test-control access_control_account_management

Expected result: 100% pass rate, all frameworks compliant

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
EVIDENCE PACKAGE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Evidence collected: ./evidence/test-AC2-20250115.zip (2.3 MB)

Contents:
✓ test_results.json          # Machine-readable test results
✓ iam_users_snapshot.json    # Current user inventory
✓ cloudtrail_events.json     # Last 90 days of account events
✓ access_analyzer_report.pdf # Access analysis findings
✓ compliance_matrix.xlsx     # Framework crosswalk

Ready for auditor review: Yes

```

## JSON Output

```bash
/grc-engineer:test-control access_control_account_management --output=json
```

```json
{
  "control_id": "access_control_account_management",
  "control_name": "Access Control - Account Management",
  "frameworks": ["NIST AC-2", "ISO A.9.2", "SOC2 CC6.1", "PCI 8.1"],
  "timestamp": "2025-01-15T10:30:00Z",
  "duration_seconds": 12.3,
  "summary": {
    "total_tests": 15,
    "passed": 11,
    "failed": 2,
    "warnings": 2,
    "pass_rate": 0.73,
    "status": "PARTIALLY_EFFECTIVE"
  },
  "tests": [
    {
      "id": "TEST-001",
      "name": "Unique User IDs",
      "category": "configuration",
      "status": "PASS",
      "frameworks": ["NIST", "ISO", "SOC2", "PCI"],
      "result": {
        "users_checked": 47,
        "unique_ids": 47,
        "duplicates": 0
      }
    },
    {
      "id": "TEST-003",
      "name": "Quarterly Access Reviews",
      "category": "configuration",
      "status": "FAIL",
      "frameworks": ["PCI"],
      "result": {
        "last_review_date": "2024-11-15",
        "days_since_review": 92,
        "threshold": 90,
        "violation": true
      },
      "remediation": {
        "command": "python scripts/access_review.py --immediate",
        "estimated_time_minutes": 120
      }
    }
  ],
  "framework_compliance": {
    "NIST": {
      "status": "PARTIAL",
      "score": 0.86,
      "issues": ["Access review overdue", "Documentation outdated"]
    },
    "ISO": {
      "status": "PARTIAL",
      "score": 0.86,
      "issues": ["Documentation outdated"]
    },
    "SOC2": {
      "status": "PARTIAL",
      "score": 0.73,
      "issues": ["Access review overdue", "Documentation outdated"]
    },
    "PCI": {
      "status": "NON_COMPLIANT",
      "score": 0.66,
      "issues": ["Quarterly review requirement violated"]
    }
  },
  "evidence_package": "./evidence/test-AC2-20250115.zip"
}
```

## Automated Testing Schedule

Set up continuous testing:

```bash
# Daily testing (cron)
0 2 * * * /grc-engineer:test-control all aws --output=json > /var/log/compliance/daily-test.json

# Weekly comprehensive test
0 3 * * 0 /grc-engineer:test-control all aws --verbose --output=json > /var/log/compliance/weekly-test.json
```

## CI/CD Integration

```yaml
# GitHub Actions
name: Compliance Testing

on:
  schedule:
    - cron: '0 2 * * *'  # Daily at 2 AM
  push:
    branches: [main]

jobs:
  test-controls:
    runs-on: ubuntu-latest
    steps:
      - name: Test Access Control
        run: /grc-engineer:test-control access_control_account_management --output=json > results.json

      - name: Check Compliance Threshold
        run: |
          PASS_RATE=$(jq '.summary.pass_rate' results.json)
          if (( $(echo "$PASS_RATE < 0.90" | bc -l) )); then
            echo "Compliance below 90%: $PASS_RATE"
            exit 1
          fi

      - name: Upload Evidence
        uses: actions/upload-artifact@v3
        with:
          name: compliance-evidence
          path: evidence/*.zip
```

## Test Coverage by Framework

| Framework | Tests | Coverage |
|-----------|-------|----------|
| **NIST 800-53** | 12 | AC-2, AC-2(1-4), AC-5, AC-6, AU-2, AU-9, AU-11 |
| **ISO 27001** | 10 | A.9.2.1-5, A.12.4.1-4 |
| **SOC2** | 11 | CC6.1-6.3, CC7.2-7.3 |
| **PCI-DSS** | 9 | 8.1, 8.1.1, 8.1.3, 8.1.4, 8.3, 10.2, 10.7 |

## Auto-Fix Mode

```bash
/grc-engineer:test-control access_control_account_management --fix-failures
```

Automatically attempts to remediate failures:

- ✓ Run overdue access reviews
- ✓ Disable inactive users
- ✓ Enable missing configurations
- ✗ Cannot auto-fix: Documentation updates (requires manual review)

## Related Commands

- `/grc-engineer:generate-implementation` - Generate control implementation
- `/grc-engineer:scan-iac` - Scan infrastructure for violations
- `/grc-engineer:monitor-continuous` - Set up continuous monitoring
- `/grc-engineer:collect-evidence` - Collect compliance evidence
