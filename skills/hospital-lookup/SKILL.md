---
name: hospital-lookup
description: Search the verified hospital knowledge base by specialty direction, city, hospital type or ranking, and return sourced profiles. Use when an advisor or patient asks which Chinese hospitals are strong in a field or where.
metadata:
  version: 0.1.0
  stage: learn
  owner: NEXA Longevity
  reviewed_by: ""
  reviewed_on: ""
  languages: [zh, en]
  license: CC-BY-4.0
  author: NEXA Longevity
---

# 医生与机构档案查询 · Hospital & Doctor Lookup

## 用途 · Purpose

从本库经核实的知识库（`data/hospitals/`）中，按方向、城市、医院类型或排名检索医疗机构，返回带来源和核实日期的档案。v0.1 只收录七个方向各前 10 家公立头部医院；医生档案、民营医院和外资医院在 v0.2 加入。

Search the verified knowledge base in `data/hospitals/` and return sourced profiles. v0.1 covers the top 10 public hospitals in each of the seven directions; doctor profiles, private and foreign-invested hospitals come in v0.2.

## 何时使用 · When to use

- "上海哪些医院的肿瘤科比较强？"
- "Which hospitals in China are known for orthopedics?"
- 为 `doctor-matching` 准备候选机构池

## 输入 · Inputs

| 字段 Field | 说明 Description | 必需 Required |
|---|---|---|
| direction | oncology / cardio-cerebrovascular / reproductive / checkup-longevity / tcm / orthopedics / aesthetics | 否 |
| city / province | 城市或省份 | 否 |
| type | public / private / foreign | 否 |
| keyword | 专长关键词，如"质子""肝移植" | 否 |
| language | 输出语言 | 是 |

至少提供 direction、city 或 keyword 中的一项。

## 步骤 · Steps

1. 读取 `data/hospitals/<direction>.yaml`（未指定方向时读取全部文件）。
2. 按条件筛选；按 `ranking.rank` 升序排列。
3. 每条结果必须带出 `source_list`、`source_url`、`verified_on`。
4. 若 `verified_on` 距今超过 12 个月，在该条后标注"信息可能过时，请复核"。
5. 知识库里查不到时，明确说"本库 v0.1 暂未收录"，可以建议用户查阅公开名单，但**不得根据模型记忆补充医院或医生**。
6. 按 language 输出，医院名同时给出中英文。

## 输出格式 · Output format

```
共找到 <n> 家（数据范围：本库 v0.1，<方向>）

| 排名 | 医院 | 城市 | 优势科室 | 国际部 | 来源与核实日期 |

说明：排名引自 <source_list>，仅反映该名单的评价，不代表本库推荐。
<标准医学声明>
```

## 边界与禁止事项 · Boundaries

- 只返回知识库中的记录，不编造、不补充。
- 不对医院做"最好""首选"之类评价；排名一律注明出处。
- 不提供医院内部联系方式，只给官网或公开的国际部信息。

## 医学声明 · Disclaimer

本 Skill 仅提供公开信息检索，不构成就医推荐，一切以执业医生意见为准。This Skill returns public information only and is not a medical recommendation.

---
© NEXA Longevity · CC BY 4.0 · https://skills.nxlongevity.com
