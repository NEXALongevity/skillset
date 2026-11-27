---
name: second-opinion-prep
description: "Prepare a complete, well-framed package for a second opinion from a Chinese specialist: questions, records checklist, timeline and consent. Use when a patient already has a diagnosis or plan and wants an independent review."
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

# 第二诊疗意见准备 · Second Opinion Preparation

## 用途 · Purpose

当患者已有诊断或治疗方案、希望听取中国专家的第二意见时，帮助整理问题清单、病历材料、病程时间线和同意书，让会诊医生在最短时间内拿到判断所需的信息。它只准备材料，不给出第二意见本身。

When a patient already has a diagnosis or plan and wants an independent review from a Chinese specialist, assemble the questions, records, timeline and consent so the reviewing doctor gets what they need quickly. It prepares the package; it never gives the opinion itself.

## 何时使用 · When to use

- 患者在本国已确诊，想确认诊断或比较治疗方案时
- 本国方案已无更多选择，想了解中国是否有其他路径时
- 远程会诊（teleconsult-coordination）之前

## 输入 · Inputs

| 字段 Field | 说明 Description | 必需 Required |
|---|---|---|
| current_diagnosis | 现有诊断（来自原始报告） | 是 |
| current_plan | 本国医生建议的方案 | 是 |
| records | 病理、影像、化验、既往治疗记录 | 是 |
| patient_questions | 患者最想问的问题 | 是 |
| deadline | 需要答复的时间（如治疗开始前） | 否 |

## 步骤 · Steps

1. **框定问题**：把患者的担心改写成 3 到 5 个可回答的问题，例如"诊断是否成立""方案 A 与 B 的取舍""是否需要补充检查"。
2. **材料清单**：按专科列出必需材料（如肿瘤：病理报告与切片/蜡块是否可寄送、免疫组化、分期影像；骨科：负重位 X 光、MRI）。标出缺失项。
3. **时间线**：按日期列出症状、检查、诊断、治疗与疗效。
4. **同意与隐私**：取得患者书面同意，说明材料会发给哪家机构，用 compliance-check 检查。
5. **交付**：生成中英双语"会诊申请包"目录，交给 teleconsult-coordination 或 appointment-booking。

## 输出格式 · Output format

```
【会诊问题 / Questions for the reviewer】1. … 2. …
【病程时间线 / Timeline】
| 日期 | 事件 | 来源文件 |
【材料清单 / Records】☐ 已有 … ☐ 缺失 …
【同意状态 / Consent】
【交付去向 / Next】
```

## 边界与禁止事项 · Boundaries

- 不提供第二意见，不评价原诊断或原方案是否正确。
- 不暗示中国方案一定更好，问题表述保持中立。
- 材料缺失时如实标注，不用推测补齐。
- 切片、蜡块等实物寄送需遵守双方国家规定，提示向医院确认。

## 医学声明 · Disclaimer

本 Skill 仅提供信息整理与流程支持，不构成医疗建议，诊断与治疗决定以执业医生意见为准。This Skill organises information and supports workflows only; it is not medical advice. Diagnosis and treatment decisions rest with licensed physicians.

---
© NEXA Longevity · CC BY 4.0 · https://skills.nxlongevity.com
