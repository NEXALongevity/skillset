---
name: multilingual-scripts
description: Provide reviewed, reusable scripts for common touchpoints (first contact, explaining fees, delays, bad news handover, discharge) in Chinese, English and the patient's language, compliant with medical-boundary and advertising rules. Use when drafting messages to patients.
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

# 多语言沟通话术 · Multilingual Communication Scripts

## 用途 · Purpose

为跨境医疗从业者提供常见场景的标准话术：首次沟通、说明费用、行程延误、转达医生的不好消息、出院交接，中英文加患者语言。话术遵守医学边界与宣传合规，可按场景复用。与 multilingual-communication 的区别：那个做实时翻译，这个提供标准话术模板。

Reusable, reviewed scripts for common touchpoints: first contact, explaining fees, delays, relaying difficult news from a doctor and discharge, in Chinese, English and the patient's language, within medical and advertising rules. multilingual-communication translates live; this provides templates.

## 何时使用 · When to use

- 新顾问上岗、统一服务口径时
- 需要给患者发标准消息时
- 处理投诉或延误时

## 输入 · Inputs

| 字段 Field | 说明 Description | 必需 Required |
|---|---|---|
| scenario | first-contact / fees / delay / difficult-news / discharge / complaint | 是 |
| language | 患者语言 | 是 |
| details | 需填入的具体信息 | 否 |
| tone | 正式 / 亲切 | 否 |

## 步骤 · Steps

1. 选择场景模板，填入具体信息（用占位符 {…} 标出必须替换的部分）。
2. 术语引用 shared/glossary.yaml。
3. 医学内容只转述医生原话，注明"医生说明"；不加入顾问自己的判断。
4. 转达不好消息时：先确认患者希望谁在场、以何种方式得知；由医生本人告知诊断，顾问只协调与陪伴。
5. 输出中文 + 患者语言对照，并跑 compliance-check。

## 输出格式 · Output format

```
【场景 / Scenario】
【话术 / Script】
| 中文 | 患者语言 |
【使用提示 / Notes】
```

## 边界与禁止事项 · Boundaries

- 话术不得承诺疗效或结果。
- 诊断、预后等坏消息由医生告知，话术只用于安排与陪伴。
- 不使用施压或制造焦虑的销售话术。

## 医学声明 · Disclaimer

本 Skill 仅提供信息整理与流程支持，不构成医疗建议，诊断与治疗决定以执业医生意见为准。This Skill organises information and supports workflows only; it is not medical advice. Diagnosis and treatment decisions rest with licensed physicians.

---
© NEXA Longevity · CC BY 4.0 · https://skills.nxlongevity.com
