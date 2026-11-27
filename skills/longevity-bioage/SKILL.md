---
name: longevity-bioage
description: "Organise a longevity assessment: collect biomarkers and lifestyle data, explain published biological-age methods and their limits, and prepare a structured report for the reviewing physician. Use for longevity and check-up clients; it does not diagnose."
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

# 长寿与生物年龄评估 · Longevity & Biological Age Assessment

## 用途 · Purpose

为长寿医学和高端体检客户组织评估流程：收集生物标志物与生活方式数据，说明已发表的生物年龄算法及其局限，生成给评估医生的结构化报告。生物年龄只是研究性指标，不是诊断。

Organise a longevity assessment for longevity and premium check-up clients: collect biomarkers and lifestyle data, explain published biological-age methods and their limits, and prepare a structured report for the reviewing physician. Biological age is a research metric, not a diagnosis.

## 何时使用 · When to use

- 客户咨询抗衰、长寿项目时
- 体检后希望了解"生物年龄"时
- 长寿项目前后对比时

## 输入 · Inputs

| 字段 Field | 说明 Description | 必需 Required |
|---|---|---|
| chronological_age | 实际年龄 | 是 |
| biomarkers | 已有化验结果（含单位与检测日期） | 是 |
| method | 拟用的算法（如基于常规血液指标的表型年龄、表观遗传时钟），需有文献出处 | 否 |
| lifestyle | 睡眠、运动、饮食、吸烟饮酒 | 否 |

## 步骤 · Steps

1. **方法说明**：列出可选的生物年龄方法、所需指标、文献出处和局限（人群来源、实验室差异、不能用于个体诊断）。
2. **数据核对**：检查所需指标是否齐全、单位是否与方法一致、检测日期是否接近。缺项不估算。
3. **计算**：只有在使用已发表公式且指标齐全时才计算；公式与系数从原文献获取并写明出处，不凭记忆。
4. **报告**：给医生的报告包括原始数据、计算结果、方法局限；给客户的说明强调"研究性指标，变化趋势比单次数值更有意义"。
5. 医生给出干预建议后，交给 nutrition-exercise 等执行。

## 输出格式 · Output format

```
【方法 / Method】名称、文献、所需指标、局限
【数据核对 / Data check】
| 指标 | 数值 | 单位 | 日期 | 状态 |
【结果 / Result】（仅在条件满足时）
【给客户的说明 / Client note】
【待医生审阅 / For physician review】
```

## 边界与禁止事项 · Boundaries

- 生物年龄不是诊断，不用来判断疾病或寿命。
- 不使用来源不明的算法；缺少指标时不估算。
- 不推荐未经批准的抗衰药物、干细胞或其他未获批疗法。
- 宣传中不得出现"逆龄 X 岁"等承诺性表述。

## 医学声明 · Disclaimer

本 Skill 仅提供信息整理与流程支持，不构成医疗建议，诊断与治疗决定以执业医生意见为准。This Skill organises information and supports workflows only; it is not medical advice. Diagnosis and treatment decisions rest with licensed physicians.

---
© NEXA Longevity · CC BY 4.0 · https://skills.nxlongevity.com
