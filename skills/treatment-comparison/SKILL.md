---
name: treatment-comparison
description: "Lay out treatment options a patient's doctors have proposed in China and elsewhere side by side: what each involves, duration, trips needed, cost range from written quotes and questions to ask, without ranking them. Use when a patient weighs options."
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

# 治疗方案对比 · Treatment Option Comparison

## 用途 · Purpose

把患者的医生们（中国与其他国家）已经提出的治疗方案并排列出：每个方案包含什么、周期、需要几次行程、来自书面报价的费用区间、需要问医生的问题。它整理选项，不排序、不推荐。

Put the options a patient's doctors have proposed, in China and elsewhere, side by side: what each involves, duration, trips needed, cost ranges from written quotes and questions to ask. It organises options without ranking or recommending.

## 何时使用 · When to use

- 患者拿到两个以上方案、难以取舍时
- 患者想知道中国方案与本国方案的差别时
- 第二意见返回后

## 输入 · Inputs

| 字段 Field | 说明 Description | 必需 Required |
|---|---|---|
| options | 各方案来源（医生/医院）、内容、周期 | 是 |
| quotes | 书面报价（来自 cost-estimate） | 否 |
| patient_priorities | 患者看重的因素：时间、费用、语言、距离家人 | 是 |

## 步骤 · Steps

1. **只收录医生提出的方案**，每个注明来源与日期；患者自己听说的方案标注"未经医生提出"。
2. **逐项对齐**：方案内容、周期、住院天数、行程次数、随访要求、费用区间（只用书面报价）。
3. **按患者看重的因素**做对照，不打分、不排序。
4. **问题清单**：每个方案需要问医生的问题（适应条件、风险、证据）。
5. 涉及疗效与风险的比较，一律写"请向医生确认"。

## 输出格式 · Output format

```
【方案对照 / Side by side】
| 维度 | 方案 A | 方案 B |
【与患者优先事项的关系 / Against your priorities】
【问医生的问题 / Questions】
【说明】方案选择由患者与医生共同决定
```

## 边界与禁止事项 · Boundaries

- 不推荐、不排序方案，不比较疗效优劣。
- 不收录没有医生提出的方案作为选项。
- 费用只用书面报价。

## 医学声明 · Disclaimer

本 Skill 仅提供信息整理与流程支持，不构成医疗建议，诊断与治疗决定以执业医生意见为准。This Skill organises information and supports workflows only; it is not medical advice. Diagnosis and treatment decisions rest with licensed physicians.

---
© NEXA Longevity · CC BY 4.0 · https://skills.nxlongevity.com
