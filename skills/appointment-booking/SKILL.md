---
name: appointment-booking
description: Prepare and track a specialist appointment request at a Chinese hospital through its international department or official booking channel, with documents, time options and confirmation checks. Use after a doctor or hospital is shortlisted.
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

# 医生号源查询与预约 · Specialist Appointment Booking

## 用途 · Purpose

在候选医生和医院确定后，按医院官方渠道（国际医疗部、特需门诊、官方小程序或电话）准备预约申请、跟进确认，并把确认信息交给行程规划。它不抢号、不使用非官方号贩渠道。

Once a doctor or hospital is shortlisted, prepare the appointment request through the hospital's official channel (international department, VIP clinic, official app or phone), follow up and pass confirmed details to itinerary planning. No scalping or unofficial channels.

## 何时使用 · When to use

- 医生与方案匹配（doctor-matching）给出候选后
- 远程会诊后医生建议来华面诊时
- 预约被改期、需要重新安排时

## 输入 · Inputs

| 字段 Field | 说明 Description | 必需 Required |
|---|---|---|
| hospital | 医院名称（来自知识库） | 是 |
| department_or_doctor | 科室或医生 | 是 |
| preferred_dates | 可就诊日期范围（至少 2 个选项） | 是 |
| record_summary | 中英文病历摘要（来自 medical-record-summary） | 是 |
| patient_language | 患者语言、是否需要口译 | 是 |
| identity_doc_type | 护照等证件类型（不填号码） | 是 |

## 步骤 · Steps

1. **确认官方渠道**：从知识库读取医院国际医疗部或官网信息；没有记录时写"待查官方渠道"，不使用第三方号贩。
2. **准备申请包**：病历摘要、近期影像与报告清单、希望解决的问题（3 条以内）、可就诊日期、语言需求。
3. **起草预约邮件或留言**：中英双语，说明患者为境外患者、是否需要国际部协助缴费与口译。
4. **跟进清单**：记录提交时间、对方回复、预约号或确认函，48 小时未回复时按官方电话跟进。
5. **确认关键事项**：就诊地点（院区、楼层）、是否需空腹、需带原件、实名挂号所需证件、取消改期规则、诊查费。
6. 确认后交给 visa-itinerary 和 china-practical-guide。

## 输出格式 · Output format

```
【预约申请 / Request】（中英双语邮件草稿）
【跟进记录 / Tracking】
| 日期 | 动作 | 对方回复 | 下一步 |
【确认信息 / Confirmed】院区、日期时间、医生/科室、注意事项、取消规则
【待确认 / To confirm】
```

## 边界与禁止事项 · Boundaries

- 只使用医院官方渠道；不代抢号、不买卖号源。
- 不在申请中夸大病情以求加号。
- 患者证件号、联系方式只在发送给医院时使用，不写入记录模板与示例。
- 医生是否接诊由医院决定，不向患者承诺。

## 医学声明 · Disclaimer

本 Skill 仅提供信息整理与流程支持，不构成医疗建议，诊断与治疗决定以执业医生意见为准。This Skill organises information and supports workflows only; it is not medical advice. Diagnosis and treatment decisions rest with licensed physicians.

---
© NEXA Longevity · CC BY 4.0 · https://skills.nxlongevity.com
