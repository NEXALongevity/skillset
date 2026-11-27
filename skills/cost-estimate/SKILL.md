---
name: cost-estimate
description: Build a transparent cost range for a medical trip from hospital quotes and user-supplied travel prices, and compare quotes item by item. Never invents prices. Use before sending a quote or when a patient compares options.
metadata:
  version: 0.1.0
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
| direction | 七大方向之一或具体项目 | 是 |
| quotes | 医院书面报价，含项目、金额、币种、是否含税、有效期 | 是 |
| stay_days | 在华停留天数 | 是 |
| travel_prices | 机票、住宿每晚、口译每天等，由用户提供 | 否 |
| contingency_pct | 不可预见费比例，默认 15% | 否 |
| fx_rate | 换算汇率与日期（用户提供） | 否 |

## 步骤 · Steps

1. **调用 MCP 取费用项清单**：`cost_checklist(direction)`，得到该方向常见费用项，用于检查漏项（只有项目名，没有金额）。
2. **录入报价**：逐项登记金额、币种、来源（报价单名称与日期）。没有书面来源的金额标记"口头/待确认"。
3. **调用 MCP 计算**：`cost_estimate(items, stay_days, contingency_pct, fx_rate)`，得到医疗、行程、服务三类小计，以及低/高区间（高位 = 小计 × (1+不可预见费)）。
4. **比价**：两份以上报价时调用 `compare_quotes(quotes)`，输出逐项对照、漏项、口径差异（如是否含术前检查、植入物、住院床位、术后复查、口译）。
5. **写清假设**：汇率日期、未包含项、预交金与最终结算的关系（多退少补）。
6. 结果交给 quote-builder 生成正式报价单，交付前用 compliance-check 检查费用表述。

## 输出格式 · Output format

```
【费用区间 / Range】低 … – 高 …（币种，汇率日期）
【分项 / Breakdown】
| 类别 | 项目 | 金额 | 来源 | 状态 |
【比价 / Comparison】（多份报价时）
| 项目 | 报价 A | 报价 B | 差异说明 |
【漏项 / Missing items】
【假设与说明 / Assumptions】
```

## 边界与禁止事项 · Boundaries

- 不编造、不估算任何医疗价格；没有报价的项目写"待报价"。
- 不承诺最终费用；说明实际以医院结算为准，预交金多退少补。
- 汇率由用户提供或注明"待换算"，不凭记忆给汇率。
- 不评价医院定价是否合理，只指出口径差异。

## 医学声明 · Disclaimer

费用整理基于用户提供的报价，不构成价格承诺或医疗建议；治疗方案与实际费用以医疗机构为准。Cost summaries rely on quotes supplied by the user and are not a price guarantee or medical advice.

---
© NEXA Longevity · CC BY 4.0 · https://skills.nxlongevity.com
