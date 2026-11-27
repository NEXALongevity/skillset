---
name: checkup-report-explainer
description: "Explain a health check-up report in plain language: what each abnormal flag means in general terms, which items to raise with a doctor and how urgent follow-up is likely to be. Use after a check-up in China or abroad; it does not diagnose."
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

# 体检报告解读 · Check-up Report Explainer

## 用途 · Purpose

用患者听得懂的语言解释体检报告：每个异常标记一般代表什么、为什么要复查、应该带着哪些问题去找哪一科的医生。它解释报告，不做诊断，也不替代体检中心的总检医生意见。

Explain a check-up report in plain language: what each flagged item generally means, why follow-up is suggested and which specialty to ask. It explains the report; it does not diagnose or replace the reviewing physician.

## 何时使用 · When to use

- 在华体检后患者拿到中文报告时
- 患者带着本国体检报告咨询是否需要来华进一步检查时
- 体检中心的总检建议需要翻译和说明时

## 输入 · Inputs

| 字段 Field | 说明 Description | 必需 Required |
|---|---|---|
| report | 体检报告（文字或表格），含参考范围 | 是 |
| age_sex | 年龄、性别 | 是 |
| history | 既往病史与用药 | 否 |
| language | 输出语言 | 是 |

## 步骤 · Steps

1. **读取结构**：按系统归类（血液、肝肾功能、血脂血糖、影像、心电图等），保留原始数值与参考范围。
2. **标出异常**：只标报告本身标记为异常或超出参考范围的项目，不自行设定新阈值。
3. **通俗解释**：每个异常项说明它测量什么、一般可能与哪些情况有关（列举而不判断）、通常建议做什么（复查、专科就诊）。
4. **紧急程度分级**：按报告和总检医生的提示分为"尽快就医 / 近期专科复查 / 定期随访"；报告中出现危急值或总检提示尽快就诊时，第一行写明。
5. **问题清单**：为患者生成带去门诊的问题。
6. 需要专科就诊时，交给 needs-assessment 或 doctor-matching。

## 输出格式 · Output format

```
【先看这里 / Read first】（如有需要尽快就医的项目）
【异常项一览 / Flagged items】
| 项目 | 结果 | 参考范围 | 一般含义 | 建议 |
【正常项 / Normal】（简述）
【带给医生的问题 / Questions for your doctor】
【说明】本解读不构成诊断
```

## 边界与禁止事项 · Boundaries

- 不做诊断，不说"你得了某病"，只说"可能与…有关，需医生判断"。
- 不调整参考范围，不根据单项结果推荐药物或保健品。
- 影像报告中的结节、占位等描述，一律建议由相应专科医生评估。
- 危急值或总检医生提示尽快就医时，必须放在第一行。

## 医学声明 · Disclaimer

本 Skill 仅提供信息整理与流程支持，不构成医疗建议，诊断与治疗决定以执业医生意见为准。This Skill organises information and supports workflows only; it is not medical advice. Diagnosis and treatment decisions rest with licensed physicians.

---
© NEXA Longevity · CC BY 4.0 · https://skills.nxlongevity.com
