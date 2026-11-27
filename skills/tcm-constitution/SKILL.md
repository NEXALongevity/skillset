---
name: tcm-constitution
description: Guide a wellness-oriented TCM body-constitution self-assessment based on the China Association of Chinese Medicine standard (nine constitution types), explain results in plain language and refer to a licensed TCM physician. Use for wellness clients; it is not a TCM diagnosis.
metadata:
  version: 0.1.0
  stage: assess
  owner: NEXA Longevity
  reviewed_by: ""
  reviewed_on: ""
  languages: [zh, en]
  license: CC-BY-4.0
  author: NEXA Longevity
---

# 中医体质辨识 · TCM Body Constitution Self-Assessment

## 用途 · Purpose

按中华中医药学会《中医体质分类与判定》标准的九种体质框架，引导客户完成体质自评，用通俗语言解释结果，并转介执业中医师。体质辨识用于养生保健，不是中医诊断，也不开方。

Guide a wellness self-assessment using the nine-constitution framework of the China Association of Chinese Medicine standard, explain the result in plain language and refer to a licensed TCM physician. It is for wellness, not a TCM diagnosis, and never prescribes.

## 何时使用 · When to use

- 康养、体检客户对中医调理感兴趣时
- 去中医康养目的地前（tcm-wellness-destinations）
- 向外国客户介绍中医体质概念时

## 输入 · Inputs

| 字段 Field | 说明 Description | 必需 Required |
|---|---|---|
| questionnaire | 标准问卷的作答结果（使用标准原文问卷） | 是 |
| language | 输出语言 | 是 |
| health_conditions | 已知疾病（有疾病者优先就医） | 否 |

## 步骤 · Steps

1. **问卷**：使用《中医体质分类与判定》标准问卷原文（九种体质：平和质、气虚质、阳虚质、阴虚质、痰湿质、湿热质、血瘀质、气郁质、特禀质），翻译版本需与原文对照。
2. **计分**：按标准规定的原始分与转化分方法计算，判定"是 / 倾向是 / 否"，计分规则以标准原文为准。
3. **解释**：用客户的语言解释每种体质的典型表现，避免把体质描述成疾病。
4. **建议方向**：只给标准中通用的起居、饮食、运动养生方向；涉及中药、针灸等治疗时转介执业中医师。
5. 有明确疾病或症状的客户，先建议就医。

## 输出格式 · Output format

```
【体质结果 / Result】
| 体质 | 转化分 | 判定 |
【通俗解释 / In plain words】
【养生方向 / Wellness direction】
【转介 / Referral】执业中医师
【说明】体质辨识用于养生保健，不是诊断
```

## 边界与禁止事项 · Boundaries

- 不做中医诊断，不开中药方剂，不推荐具体中成药。
- 体质描述不得与疾病挂钩或暗示治疗效果。
- 使用标准原文问卷与计分方法，不自行增删题目。
- 有疾病者先就医。

## 医学声明 · Disclaimer

本 Skill 仅提供信息整理与流程支持，不构成医疗建议，诊断与治疗决定以执业医生意见为准。This Skill organises information and supports workflows only; it is not medical advice. Diagnosis and treatment decisions rest with licensed physicians.

---
© NEXA Longevity · CC BY 4.0 · https://skills.nxlongevity.com
