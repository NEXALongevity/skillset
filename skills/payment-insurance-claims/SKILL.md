---
name: payment-insurance-claims
description: Plan how a patient pays a Chinese hospital (deposit, card, transfer, mobile pay with foreign cards) and prepare the document pack for an overseas insurance claim or direct billing. Use before admission and after discharge.
metadata:
  version: 0.1.0
  stage: travel
  owner: NEXA Longevity
  reviewed_by: ""
  reviewed_on: ""
  languages: [zh, en]
  license: CC-BY-4.0
  author: NEXA Longevity
---

# 跨境支付与保险理赔 · Cross-border Payment & Insurance Claims

## 用途 · Purpose

帮患者规划在华就医的付款方式（预交金、国际卡、境外汇款、绑定外卡的移动支付），并在出院后整理海外保险理赔或直付所需的材料。它只做流程和清单，不代收代付款项，不判断保单是否赔付。

Help patients plan how to pay a Chinese hospital (deposit, international cards, wire transfer, mobile pay linked to foreign cards) and, after discharge, assemble the document pack for an overseas insurance claim or direct billing. It is a process and checklist tool; it never handles money or decides coverage.

## 何时使用 · When to use

- 入院前需要准备预交金时
- 患者有海外医疗保险，希望直付或事后理赔时
- 出院结算后整理发票、费用清单与病历时

## 输入 · Inputs

| 字段 Field | 说明 Description | 必需 Required |
|---|---|---|
| payer | 自费 / 保险直付 / 保险事后报销 / 雇主或机构付费 | 是 |
| insurer | 保险公司名称与保单类型（不填保单号） | 否 |
| hospital | 医院与是否有国际医疗部 | 是 |
| estimated_amount | 预计金额与币种（来自 cost-estimate） | 是 |
| payment_tools | 患者持有的卡和支付工具 | 是 |

## 步骤 · Steps

1. **确认付款路径**：医院是否接受境外卡、是否可对公汇款、预交金要求与退款规则（向国际医疗部确认）。
2. **移动支付准备**：提示患者出发前在常用移动支付应用中绑定境外银行卡并完成实名，了解单笔限额与手续费以应用内显示为准。
3. **保险直付**：请患者先联系保险公司申请担保函（Guarantee of Payment），确认医院是否在其直付网络；未确认前按自费准备。
4. **理赔材料清单**：发票、费用明细清单、出院小结、诊断证明、检查报告、处方、付款凭证；需要时准备英文翻译（medical-record-translation）。
5. **时限提醒**：记录保险公司的报案和递交时限，按保单原文为准。
6. 完成后用 compliance-check 检查跨境传输病历的同意情况。

## 输出格式 · Output format

```
【付款方案 / Payment plan】
| 阶段 | 金额 | 方式 | 需提前准备 |
【保险 / Insurance】直付 / 事后理赔；需联系事项
【理赔材料清单 / Claim pack】☐ …
【时限 / Deadlines】
【待确认 / To confirm】
```

## 边界与禁止事项 · Boundaries

- 不代收、代付、垫付任何款项，不收集卡号、密码、验证码。
- 不判断保单是否赔付，以保险公司书面答复为准。
- 手续费、限额、汇率以支付机构和银行显示为准，不凭记忆给数字。
- 不建议拆分发票或改动诊断以迎合理赔。

## 医学声明 · Disclaimer

本 Skill 只提供付款与理赔流程支持，不构成财务、保险或医疗建议。This Skill supports payment and claim workflows only; it is not financial, insurance or medical advice.

---
© NEXA Longevity · CC BY 4.0 · https://skills.nxlongevity.com
