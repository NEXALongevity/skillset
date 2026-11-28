---
name: cost-estimate
description: Build a transparent cost range for a medical trip from hospital quotes and user-supplied travel prices, and compare quotes item by item. Never invents prices. Use before sending a quote or when a patient compares options.
metadata:
  version: 0.3.0
  stage: match
  owner: NEXA Longevity
  reviewed_by: ""
  reviewed_on: ""
  languages: [zh, en]
  license: CC-BY-4.0
  author: NEXA Longevity
  mcp: nexa-travel-mcp/cost_estimate
---

# 费用预估与比价 · Cost Estimate & Quote Comparison

## 用途 · Purpose

把医院报价、患者或顾问提供的行程费用整理成一份可核对的费用区间，并对多份报价逐项比对，找出漏项和口径差异。所有金额都来自医院书面报价或用户输入，MCP 只做计算、换算和漏项检查，不提供任何价格数据。

Turn hospital quotes and user-supplied travel prices into a checkable cost range, and compare several quotes line by line to expose missing items and different scopes. Every figure comes from a written quote or the user; the MCP calculates and checks gaps but holds no price data.

## 何时使用 · When to use

- 拿到一家或多家医院的书面报价后
- 患者问"大概要花多少"，需要说明费用构成而不是给一个数字时
- 比较中国与其他国家方案、或比较国内两家机构时
- 生成正式报价单（quote-builder）之前

## 输入 · Inputs

| 字段 Field | 说明 Description | 必需 Required |
|---|---|---|
| direction | 医疗方向 / Specialty direction | 清单需要 / For checklist |
| quotes | 书面报价、项目、金额、币种、含税范围及有效期 / Written quotes, line items, amounts, currencies, tax scope and validity | 计算需要 / For calculation |
| stay_days | 停留天数 / Stay length | 涉及行程时 / For travel |
| travel_prices | 用户提供的数量、单位和单价 / User-supplied quantities, units and prices | 否 / No |
| contingency_pct | 预算缓冲比例，默认 15% / Budget buffer percentage, default 15% | 否 / No |
| fx | 用户提供的 `from`、`to`、`rate`、`date` / User-supplied FX pair, rate and date | 涉及换算时 / For conversion |

## 步骤 · Steps

1. **先核对范围 / Establish scope.** 调用 `cost_checklist` 查可能漏项，核对每份书面报价的币种、日期、有效期、数量、是否含税及费用边界。无可确认金额时，只给费用清单和询价问题。Use the checklist to spot gaps, then verify currency, date, validity, quantities, tax and quote scope. With no confirmed figures, return a checklist and questions.
2. **对齐明细 / Align line items.** 同名但范围不同的项目分开列，只有确认范围相同，才用统一名称比较。将每项标为已报价、已包含但未单列、明确不含、已列待报价、未列明。只有书面明确为零才填 0。Match items only when scope agrees. Keep priced, bundled, excluded, listed without a price, and absent items distinct. Use zero only if documented.
3. **计算已知部分 / Calculate known costs.** 调用 `cost_estimate`，传入项目、金额或上下限、币种和不含身份信息的来源标识，按需加 `direction`、`stay_days`、`contingency_pct` 和 `fx`。分别列出已知费用、缓冲和待报价项。缺少带日期的汇率时保留原币，换算未覆盖的币种单列。Send item data without identifiers. Show known costs, contingency and pending items separately. Keep original currencies when no dated rate is supplied, and disclose any currency omitted by conversion.
4. **同范围比价 / Compare like for like.** 至少两份报价时调用 `compare_quotes`。只在范围与币种对齐后比较总额。已包含但未单列的项目避免重复计费，定金单列为付款节点并核对抵扣及退款条款。Call the comparison tool for two or more quotes. Compare totals only after aligning scope and currency, avoid counting bundled amounts twice, and confirm how deposits are applied or refunded.
5. **无 MCP 时 / Without MCP.** 使用相同分项表，按币种列计算式并复核。无法确认的数字留待核实。Use the same table, show and verify the arithmetic by currency, and flag unavailable figures. 交付正式报价前走 `quote-builder` 和 `compliance-check`。

## 输出格式 · Output format

```
【费用区间 / Range】低 … – 高 …（币种，汇率日期）
【分项 / Breakdown】
| 类别 | 项目 | 金额 | 来源 | 状态 |
【比价 / Comparison】（多份报价时）
| 项目 | 报价 A | 报价 B | 差异说明 |
【漏项 / Missing items】
【待询价与付款节点 / Follow-up questions and payment milestones】
【假设与说明 / Assumptions】
```

## 边界与禁止事项 · Boundaries

- 不编造、不估算任何医疗价格；没有报价的项目写"待报价"。
- 实际费用及定金安排以服务方书面条款与结算为准。
- 汇率由用户提供或注明"待换算"，不凭记忆给汇率。
- 不评价医院定价是否合理，只指出口径差异。
- 调用远程 MCP 时，只发计算所需的去标识化明细。不要发送原始报价文件、病历、姓名或联系方式。Send only de-identified calculation fields to the remote MCP. Keep original files and personal details in the approved workflow.

## 医学声明 · Disclaimer

费用整理基于用户提供的报价，不构成价格承诺或医疗建议；治疗方案与实际费用以医疗机构为准。Cost summaries rely on quotes supplied by the user and are not a price guarantee or medical advice.

---
© NEXA Longevity · CC BY 4.0 · https://skills.nxlongevity.com
