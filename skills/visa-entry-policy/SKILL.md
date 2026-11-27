---
name: visa-entry-policy
description: Look up which China entry routes may apply to a patient's nationality and stay length (visa-free, mutual exemption, 240-hour transit, Hainan 30-day, visa), with sources and as-of dates. Use before any trip is booked.
metadata:
  version: 0.1.0
  stage: travel
  owner: NEXA Longevity
  reviewed_by: ""
  reviewed_on: ""
  languages: [zh, en]
  license: CC-BY-4.0
  author: NEXA Longevity
  mcp: nexa-travel-mcp/visa_entry_options
---

# 签证与入境政策查询 · Visa & Entry Policy Lookup

## 用途 · Purpose

按患者国籍、护照类型和预计停留天数，列出可能适用的入境方式，每一条都附官方来源和核实日期，并标出与就医相关的风险点（例如免签政策列明的入境目的不含就医）。优先调用 NEXA 签证与入境政策 MCP 获取结构化结果。

Given nationality, passport type and length of stay, list the entry routes that may apply, each with an official source and as-of date, and flag medical-trip risks (for example, visa-free purposes that do not list medical treatment). Call the NEXA visa & entry MCP first when available.

## 何时使用 · When to use

- 患者有初步就医意向、开始估算行程长度时
- 确定医院与日期后、订机票之前
- 政策到期日临近（如单方面免签有效期截至 2026-12-31）或行程跨越到期日时
- 患者持双重国籍、港澳台证件或在第三国长期居留时

## 输入 · Inputs

| 字段 Field | 说明 Description | 必需 Required |
|---|---|---|
| nationality | 护照签发国（双重国籍需分别列出） | 是 |
| passport_type | 普通 / 外交 / 公务等 | 是 |
| stay_days | 预计在华停留总天数（含恢复与缓冲） | 是 |
| entry_date | 预计入境日期 | 是 |
| purpose | 就医 / 体检 / 康养 / 陪同 | 是 |
| onward_ticket | 是否持有前往第三国（地区）的联程机票 | 否 |
| destination_province | 就医省份（海南有单独政策） | 否 |

## 步骤 · Steps

1. **调用 MCP**：`visa_entry_options(nationality, stay_days, entry_date, purpose, onward_ticket, destination_province)`；MCP 不可用时，按本 Skill 的规则手工查官方来源。
2. **列出候选入境方式**，逐条写明：名称、适用条件、可停留天数、政策有效期、官方来源链接、数据核实日期（as_of）。
3. **核对停留天数**：入境方式的停留上限必须覆盖治疗、恢复与缓冲的全部天数；不够时建议办理签证，不建议依赖"出境再入境"。
4. **核对入境目的**：单方面免签、互免协定和 240 小时过境免签的公开说明中，允许的活动通常是经商、旅游、探亲访友、交流访问、过境，并未写明"就医"。凡是就医、住院、手术，一律提示"请向中国驻当地使领馆确认就医是否适用免签；如不确定，申请签证"。
5. **核对有效期**：入境日期或离境日期晚于政策有效期时标红，并提示到期前重新核实。
6. **列出不覆盖情形**：数据集中没有的国籍、外交公务护照、港澳台居民、持中国护照的华侨，各给出查询方向，不作判断。
7. 交给"签证与行程规划"（visa-itinerary）生成材料清单和日程。

## 输出格式 · Output format

```
【结论 / Summary】最稳妥的入境方式：…（理由一句话）
【候选入境方式 / Options】
| 方式 | 是否可能适用 | 停留上限 | 有效期 | 就医是否列明 | 来源 | 核实日期 |
【风险提示 / Risks】
- …
【需向使领馆确认 / Ask the embassy】
- …
【下一步 / Next】交给 visa-itinerary 生成材料清单与日程
```

## 边界与禁止事项 · Boundaries

- 不断言某人一定可以免签入境；只列出可能适用的方式和官方来源。
- 数据集外的国籍或政策一律写"未收录，请查官方"，不凭记忆补全。
- 不代办签证，不代填官方表格，不处理护照号等证件信息。
- 政策随时调整，输出必须带 as_of 日期和来源链接。

## 医学声明 · Disclaimer

本 Skill 提供入境政策信息整理，不构成法律或移民建议；入境许可以中国驻外使领馆、国家移民管理局及边检现场决定为准。This Skill organises entry-policy information and is not legal or immigration advice.

---
© NEXA Longevity · CC BY 4.0 · https://skills.nxlongevity.com
