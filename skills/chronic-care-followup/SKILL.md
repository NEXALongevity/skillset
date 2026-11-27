---
name: chronic-care-followup
description: "Set up and run a structured follow-up plan for chronic conditions (hypertension, diabetes, post-cancer surveillance) between a Chinese hospital and the patient's home doctor: schedule, home readings, red flags and reports. Use after treatment or diagnosis."
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

# 慢病随访 · Chronic Care Follow-up

## 用途 · Purpose

为高血压、糖尿病、肿瘤术后监测等慢病建立结构化随访计划：随访时间表、居家监测记录、需要立即就医的警示信号、给中国医生和本地医生的定期报告。计划内容以医生医嘱为依据，本 Skill 负责执行与提醒。

Set up and run a structured follow-up plan for chronic conditions such as hypertension, diabetes and post-cancer surveillance: schedule, home readings, red flags and periodic reports to the Chinese and local doctors. The plan follows physician orders; this Skill handles execution and reminders.

## 何时使用 · When to use

- 在华治疗出院、回国后需要长期随访时
- 患者在中国确诊慢病、需要与本地医生共同管理时
- 随访数据需要定期整理给医生看时

## 输入 · Inputs

| 字段 Field | 说明 Description | 必需 Required |
|---|---|---|
| condition | 疾病与当前治疗 | 是 |
| physician_orders | 医生给出的随访要求（项目、频率、目标值） | 是 |
| home_readings | 居家监测数据（如血压、血糖） | 否 |
| local_doctor | 本地医生是否已对接 | 否 |

## 步骤 · Steps

1. **随访表**：把医嘱拆成日历：复查项目、时间、在哪里做（本地还是返华）。
2. **居家监测模板**：按医嘱列出监测项和记录格式，目标值只写医生给出的数值。
3. **警示信号**：列出医嘱或出院小结中写明的需立即就医的情况；没有写明时提示患者向医生索取。
4. **定期报告**：按月或按随访节点汇总数据，生成给医生的中英双语简报（趋势、超出目标的次数、用药依从、患者问题）。
5. **对接**：与 return-followup-handover 衔接，确保本地医生拿到完整材料。

## 输出格式 · Output format

```
【随访日历 / Schedule】
| 时间 | 项目 | 地点 | 状态 |
【居家监测 / Home readings】
【警示信号 / Red flags】
【阶段报告 / Report to doctor】
```

## 边界与禁止事项 · Boundaries

- 不调整药物剂量，不设定医生没有给出的目标值。
- 数据异常只提示"联系医生"，不给处理建议。
- 出现警示信号时，首先提示就近就医或拨打当地急救电话。

## 医学声明 · Disclaimer

本 Skill 仅提供信息整理与流程支持，不构成医疗建议，诊断与治疗决定以执业医生意见为准。This Skill organises information and supports workflows only; it is not medical advice. Diagnosis and treatment decisions rest with licensed physicians.

---
© NEXA Longevity · CC BY 4.0 · https://skills.nxlongevity.com
