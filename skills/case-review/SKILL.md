---
name: case-review
description: "Record each patient case in one de-identified template and run a short review afterwards: what went well, delays, complaints, data errors and knowledge-base updates. Use at case close and for monthly quality reviews."
metadata:
  version: 0.1.0
  stage: cross-cutting
  owner: NEXA Longevity
  reviewed_by: ""
  reviewed_on: ""
  languages: [zh, en]
  license: CC-BY-4.0
  author: NEXA Longevity
---

# 案例记录与复盘 · Case Record & Review

## 用途 · Purpose

按统一模板记录每个案例（去标识），结案后做简短复盘：哪些顺利、哪里延误、投诉、知识库数据错误，以及需要更新的 Skill 或数据。它把一线经验反哺到知识库和 Skills。

Record every case in one de-identified template and review it at close: what went well, delays, complaints, data errors and updates needed to Skills or the knowledge base, feeding front-line experience back into the library.

## 何时使用 · When to use

- 案例结案时
- 月度质量复盘
- 发生投诉或差错后

## 输入 · Inputs

| 字段 Field | 说明 Description | 必需 Required |
|---|---|---|
| case_timeline | 案例关键节点与日期 | 是 |
| outcome_service | 服务层面的结果（不含医疗结果评价） | 是 |
| issues | 延误、投诉、差错 | 否 |
| data_errors | 发现的知识库错误 | 否 |

## 步骤 · Steps

1. **去标识**：姓名、证件、联系方式、病历号全部去除，年龄写年龄段，国籍可保留到地区。
2. **时间线**：首次咨询、匹配、预约、入境、入院、出院、回国、首次随访。
3. **指标**：首次咨询到给出匹配方案的时长；病历材料一次通过；患者推荐意愿（如有）。
4. **复盘**：顺利之处、问题、根因、改进动作与负责人。
5. **反哺**：需要修订的 Skill、需要更新的数据记录（附来源）。
6. 用 compliance-check 确认去标识后再存档。

## 输出格式 · Output format

```
【案例概要 / Case summary】（去标识）
【时间线 / Timeline】
【指标 / Metrics】
【复盘 / Review】顺利 / 问题 / 根因 / 改进
【反哺 / Updates】Skill：… 数据：…
```

## 边界与禁止事项 · Boundaries

- 不记录可识别个人身份的信息。
- 不评价医生的医疗决策，只记录服务流程。
- 复盘用于改进，不用于对外宣传。

## 医学声明 · Disclaimer

本 Skill 仅提供信息整理与流程支持，不构成医疗建议，诊断与治疗决定以执业医生意见为准。This Skill organises information and supports workflows only; it is not medical advice. Diagnosis and treatment decisions rest with licensed physicians.

---
© NEXA Longevity · CC BY 4.0 · https://skills.nxlongevity.com
