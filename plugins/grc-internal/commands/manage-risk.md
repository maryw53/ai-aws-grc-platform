---
description: Manage the risk register and risk assessments
---

# Manage Risk

Maintains the organizational risk register and performs risk assessments.

Risk register entries belong in `./grc-data/risks/` and should follow
[`docs/GRC-DATA.md`](../../../docs/GRC-DATA.md) plus
`schemas/risk.schema.json`.

## Arguments

- `$1` - Action (required: add, update, assess, report)
- `$2` - Risk ID or description (required for add/update)

## Actions

- **add** - Add a new risk to the register
- **update** - Update an existing risk's status or attributes
- **assess** - Perform risk assessment on a system or process
- **report** - Generate risk register report

## Risk Attributes

- Risk description and category
- Likelihood (1-5 scale)
- Impact (1-5 scale)
- Inherent vs residual risk scores
- Mitigation status and owner
- Target resolution date
- Linked findings or controls when the risk is backed by current evidence

## Example

```bash
/grc-internal:manage-risk add "Cloud misconfiguration exposure"
/grc-internal:manage-risk report
```
