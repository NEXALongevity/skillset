---
name: quote-builder
description: "Produce a clear, bilingual service quote for a patient or partner from verified cost items: medical, travel and service fees separated, inclusions and exclusions, validity and refund terms. Use after cost-estimate and before sending a proposal."
metadata:
  version: 0.1.0
  stage: match
  owner: NEXA Longevity
  reviewed_by: ""
  reviewed_on: ""
  languages: [zh, en]
  license: CC-BY-4.0
  author: NEXA Longevity
---

# 报价单生成 · Quote Builder

## 用途 · Purpose

把 cost-estimate 整理好的费用项生成一份正式、双语、可签字确认的报价单：医疗费、行程费、服务费分开列；写清包含与不包含、有效期、付款节点和退款规则。合并首批规划中的"费用预估与报价"。

Turn the items from cost-estimate into a formal bilingual quote the patient can sign: medical, travel and service fees listed separately, with inclusions, exclusions, validity, payment milestones and refund terms.

## 何时使用 · When to use

- cost-estimate 完成后、向患者或合作伙伴发正式方案时
- 方案变化需要重新报价时

## 输入 · Inputs

| 字段 Field | 说明 Description | 必需 Required |
|---|---|---|
| cost_items | cost-estimate 输出的分项与来源 | 是 |
| service_fee | NEXA 或顾问服务费及其构成 | 是 |
| validity | 报价有效期 | 是 |
| payment_terms | 付款节点与退款规则 | 是 |
| commission_disclosure | 是否从医疗机构收取佣金 | 是 |

## 步骤 · Steps

1. **分三栏**：医疗费（注明"以医院结算为准"）、行程费（估计）、服务费（固定或按项）。
2. **包含与不包含**：逐条写出，尤其是复查、康复、并发症处理、延长住院。
3. **透明披露**：服务费构成；是否从医疗机构收取佣金（compliance-check 第 4 项）。
4. **条款**：有效期、付款节点、取消与退款规则、价格变动处理。
5. **双语排版**：中文 + 患者语言，金额与币种一致。
6. 发送前跑 compliance-check。

## 输出格式 · Output format

```
【报价单 / Quotation】编号、日期、有效期
| 类别 | 项目 | 金额 | 说明 |
【包含 / Included】【不包含 / Not included】
【付款与退款 / Payment & refunds】
【披露 / Disclosure】
【签字确认 / Acceptance】
```

## 边界与禁止事项 · Boundaries

- 医疗费只能来自医院书面报价，并注明以医院结算为准。
- 不隐藏佣金或附加费用。
- 不以"限时优惠"等方式施压。

## 医学声明 · Disclaimer

本 Skill 仅提供信息整理与流程支持，不构成医疗建议，诊断与治疗决定以执业医生意见为准。This Skill organises information and supports workflows only; it is not medical advice. Diagnosis and treatment decisions rest with licensed physicians.

---
© NEXA Longevity · CC BY 4.0 · https://skills.nxlongevity.com
