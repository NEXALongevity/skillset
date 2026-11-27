---
name: teleconsult-coordination
description: "Coordinate a remote consultation with a Chinese specialist: platform and consent, records sent in advance, time zones, interpreter, question list and written summary afterwards. Use before deciding to travel."
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

# 远程会诊安排 · Teleconsultation Coordination

## 用途 · Purpose

协调患者与中国专家的远程会诊：确认医院提供的合规渠道与同意书、提前发送病历、换算时区、安排医学口译、准备问题清单、会后整理书面纪要。远程会诊的形式与资质要求以医院规定为准。

Coordinate a remote consultation with a Chinese specialist: the hospital's compliant channel and consent, records in advance, time zones, a medical interpreter, the question list and a written summary afterwards. Format and requirements follow the hospital's rules.

## 何时使用 · When to use

- 决定是否来华之前
- second-opinion-prep 完成后
- 回国后随访需要在华医生意见时

## 输入 · Inputs

| 字段 Field | 说明 Description | 必需 Required |
|---|---|---|
| hospital_doctor | 会诊医院与医生 | 是 |
| package | 会诊申请包（来自 second-opinion-prep） | 是 |
| time_zones | 患者所在时区 | 是 |
| interpreter | 是否需要口译、语言 | 是 |

## 步骤 · Steps

1. **渠道**：使用医院提供的远程会诊或互联网医院渠道；确认会诊性质（咨询意见，还是可以开具处方或检查单），以医院说明为准。
2. **同意**：患者签署会诊与数据传输同意书（compliance-check）。
3. **材料**：至少提前 3 个工作日发送申请包，确认医生已收到并可打开影像。
4. **时间**：提供 2 到 3 个候选时间，双方时区同时写明。
5. **会中**：口译逐句翻译；顾问记录，不插入自己的判断。
6. **会后**：整理纪要（医生原话要点、建议的下一步、需要补充的材料），请医院确认或以医院出具的书面意见为准。

## 输出格式 · Output format

```
【会诊安排 / Booking】日期、北京时间 / 患者时间、渠道、参与人
【会前清单 / Before】☐ …
【会诊纪要 / Summary】（以医院书面意见为准）
【下一步 / Next】
```

## 边界与禁止事项 · Boundaries

- 只使用医院提供的合规渠道。
- 纪要只记录医生意见，不添加解读。
- 远程会诊不能替代面诊时，按医生意见安排来华。

## 医学声明 · Disclaimer

本 Skill 仅提供信息整理与流程支持，不构成医疗建议，诊断与治疗决定以执业医生意见为准。This Skill organises information and supports workflows only; it is not medical advice. Diagnosis and treatment decisions rest with licensed physicians.

---
© NEXA Longevity · CC BY 4.0 · https://skills.nxlongevity.com
