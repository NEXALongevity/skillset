---
name: return-followup-handover
description: "Hand a patient over from the Chinese care team to their home doctor: translated discharge documents, medication list, follow-up schedule, imaging and contacts, so nothing is lost after the flight home. Use at discharge."
metadata:
  version: 0.1.0
  stage: recover
  owner: NEXA Longevity
  reviewed_by: ""
  reviewed_on: ""
  languages: [zh, en]
  license: CC-BY-4.0
  author: NEXA Longevity
---

# 回国随访交接 · Return-home Follow-up Handover

## 用途 · Purpose

出院时把患者从中国医疗团队交接给本国医生：翻译好的出院材料、用药清单、随访时间表、影像资料、双方联系方式，确保回国后不断档。合并首批规划中的"出院与回国随访"。

At discharge, hand the patient from the Chinese team to their home doctor: translated discharge documents, medication list, follow-up schedule, imaging and contacts, so nothing is lost after the flight home.

## 何时使用 · When to use

- 出院前 1 到 2 天准备
- 回国后首次本地就诊前
- 随访中需要两地医生沟通时

## 输入 · Inputs

| 字段 Field | 说明 Description | 必需 Required |
|---|---|---|
| discharge_docs | 出院小结、手术记录、病理、影像、处方 | 是 |
| home_doctor | 本地医生或医院（如已确定） | 否 |
| followup_orders | 随访要求 | 是 |
| language | 本地医生语言 | 是 |

## 步骤 · Steps

1. **材料清单**：出院小结、手术记录、病理报告、影像（DICOM 光盘或下载链接）、处方、植入物信息卡（如有）。
2. **翻译**：交给 medical-record-translation。
3. **用药清单**：通用名、剂量、疗程、在本国是否可获得（提示患者咨询本地药师），交 drug-supplement-interactions 核对。
4. **随访时间表**：交给 chronic-care-followup。
5. **联系通道**：在华主治团队的官方联系渠道、本地医生联系方式；确认患者同意两地医生沟通。
6. **交接信**：写一封给本地医生的双语交接信。

## 输出格式 · Output format

```
【交接包 / Handover pack】☐ …
【给本地医生的信 / Letter to home doctor】
【用药清单 / Medications】
【随访时间表 / Follow-up】
【联系通道 / Contacts】
```

## 边界与禁止事项 · Boundaries

- 交接信只转述在华医生的医嘱与记录，不加入新的医学判断。
- 患者未同意前不向第三方发送病历。
- 药物在本国是否可携带、可获得，提示患者向海关与药师确认。

## 医学声明 · Disclaimer

本 Skill 仅提供信息整理与流程支持，不构成医疗建议，诊断与治疗决定以执业医生意见为准。This Skill organises information and supports workflows only; it is not medical advice. Diagnosis and treatment decisions rest with licensed physicians.

---
© NEXA Longevity · CC BY 4.0 · https://skills.nxlongevity.com
