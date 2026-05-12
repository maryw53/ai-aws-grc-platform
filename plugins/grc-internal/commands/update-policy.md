---
description: Manage policy lifecycle and updates
---

# Update Policy

Manages policy documents through their lifecycle.

## Arguments

- `$1` - Policy file path or name (required)
- `$2` - Action (optional: review, update, version, approve)

## Actions

- **review** - Analyze policy for gaps and needed updates
- **update** - Suggest policy updates based on framework changes
- **version** - Create new version with change tracking
- **approve** - Generate approval workflow documentation

## Policy Lifecycle

1. Draft → Review → Approve → Publish → Monitor → Retire

## Instructions

1. Analyze current policy content
2. Compare against framework requirements
3. Identify needed updates
4. Generate redlined changes or new version
5. Create approval documentation

## Examples

```bash
# Review general security policy
/grc-internal:update-policy "Information Security Policy.md" review

# Update policy for PCI-DSS March 2025 requirements
/grc-internal:update-policy "Access Control Policy.md" update

# Version control for compliance
/grc-internal:update-policy "Data Protection Policy.md" version

# Generate approval workflow
/grc-internal:update-policy "Incident Response Policy.md" approve
```
