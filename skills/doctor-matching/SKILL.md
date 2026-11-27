---
name: doctor-matching
description: Shortlist candidate hospitals (and, from v0.2, doctors) for a patient from the verified knowledge base, ranked by condition fit, budget, timing, language and location, with reasons and sources. Use after needs assessment and record summary.
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

# 医生与方案匹配 · Doctor & Treatment Matching

## 用途 · Purpose

根据患者的需求档案和病历摘要，从本库知识库中筛出 3 至 5 家候选机构，逐一说明匹配理由、需要确认的问题和信息来源，帮助顾问在 48 小时内给出有依据的候选方案。v0.1 只匹配到医院层面；医生档案在 v0.2 加入后，再细化到专家。

Shortlist 3-5 candidate hospitals from the knowledge base, each with reasons, open questions and sources. v0.1 matches at hospital level; doctor-level matching arrives with doctor profiles in v0.2.

## 何时使用 · When to use

- `needs-assessment` 标记为"适合推进"之后
- 患者要求在几家医院之间比较时
- 首选机构无法接收，需要替补候选时

## 输入 · Inputs

| 字段 Field | 说明 Description | 必需 Required |
|---|---|---|
| needs_profile | `needs-assessment` 输出的需求档案 | 是 |
| case_summary | `medical-record-summary` 输出的摘要 | 建议 |
| preferences | 城市偏好、语言、是否需要国际部、预算上限 | 否 |
| exclude | 已排除的机构 | 否 |

## 步骤 · Steps

1. **确定方向**：从需求档案取方向；跨方向时（如肿瘤合并心脏病）分别检索并标注。
2. **建候选池**：调用 `hospital-lookup` 取该方向全部记录，去掉 exclude。
3. **逐项打分**（每项 0 至 2 分，写明依据）：
   - 专科匹配：`strengths` 或 `ranking.specialty` 是否覆盖患者的具体病种或诉求
   - 公开排名：方向内排名前 3 得 2 分，4 至 10 得 1 分
   - 国际化服务：有公开的国际医疗部得 2 分，有特需门诊得 1 分，未知 0 分
   - 地理与交通：是否在患者偏好城市，或是否有直飞患者所在地的国际航班（不确定写"待确认"，给 0 分）
   - 信息新鲜度：`verified_on` 在 12 个月内得 2 分，否则 0 分
4. **排序**：按总分排序，取前 3 至 5 家；同分时优先排名更高者。
5. **列出待确认问题**：每家机构需要向医院确认的事项，如是否接收外籍患者、等待时间、大致费用区间、语言支持。
6. **给出下一步**：建议先向哪 1 至 2 家提交病历摘要，或安排远程会诊。

## 输出格式 · Output format

```
【匹配结果 / Shortlist】基于本库 v0.1 数据（<方向>，共 <n> 家候选）

| 顺序 | 医院 | 城市 | 得分 | 匹配理由 | 来源与核实日期 |

【逐家说明 / Notes】
1. <医院>
   - 匹配点：…
   - 待确认：…

【下一步 / Next step】…

【说明】打分规则见本 Skill，排名引自公开名单，仅作初筛参考，不代表疗效比较。
<标准医学声明>
```

## 边界与禁止事项 · Boundaries

- 候选只能来自知识库；库里没有合适机构时如实说明，不凭记忆补充。
- 不比较疗效、不承诺能约到专家或某个时间、不报具体价格。
- 不根据机构是否付费合作调整排序；若存在合作关系，须在输出中如实披露。
- 匹配结果须经顾问复核后才发给患者。

## 医学声明 · Disclaimer

本结果为服务初筛，不构成就医推荐或医疗建议，最终方案以执业医生评估为准。This is a service shortlist, not a medical recommendation.

---
© NEXA Longevity · CC BY 4.0 · https://skills.nxlongevity.com
