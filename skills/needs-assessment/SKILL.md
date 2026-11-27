---
name: needs-assessment
description: Structure a new medical-travel enquiry into a needs profile and flag whether cross-border care in China looks suitable, unsuitable or urgent. Use on the first contact with a patient, before matching doctors.
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

# 初步需求评估 · Initial Needs Assessment

## 用途 · Purpose

在首次接触患者时，把病情、诉求、预算、时间、语言和出行条件梳理成一份标准需求档案，并按统一规则标出"适合推进 / 需补充信息 / 不建议跨境 / 紧急情况"，帮助顾问快速决定下一步。

Turn a first enquiry into a standard needs profile and flag, by fixed rules, whether to proceed, collect more information, advise against travel, or treat as urgent.

## 何时使用 · When to use

- 收到新咨询（消息、表单、电话记录）时
- 患者情况发生变化，需要重新判断是否继续推进时

## 输入 · Inputs

| 字段 Field | 说明 Description | 必需 Required |
|---|---|---|
| enquiry | 患者或家属的原始咨询内容 | 是 |
| summary | 已有的病历摘要（来自 `medical-record-summary`） | 否 |

## 步骤 · Steps

1. **提取需求档案**（缺失写"未知"）：
   - 方向：七个方向之一，或"其他"
   - 病情概况与当前阶段（只引用患者或病历的说法）
   - 诉求类型：第二意见 / 手术 / 系统治疗 / 检查体检 / 康复调理 / 医美 / 其他
   - 期望时间、预算范围、付费方式（自费 / 保险）
   - 语言、国籍与所在地、是否有陪同人
   - 出行条件：能否乘飞机、是否需要轮椅或医疗转运
2. **按规则标记**（命中任一项即标记，按优先级从高到低）：
   - **紧急情况**：描述中有急性症状（如胸痛、呼吸困难、意识改变、大出血、突发肢体无力或言语不清）→ 立即建议当地急诊，不进入跨境流程。
   - **不建议跨境**：病情不稳定无法长途飞行；预期获益明显依赖本地持续治疗；所需治疗在中国对外籍患者不可提供（如需核实，写"待核实"）。
   - **需补充信息**：关键病历缺失，或方向、诉求无法判断。
   - **适合推进**：以上都不命中。
3. **列出下一步**：需要补充的材料、建议使用的下一个 Skill（如 `medical-record-summary`、`doctor-matching`）。
4. **双语输出**：顾问用中文，患者沟通稿用患者语言（v0.1 为英文）。

## 输出格式 · Output format

```
【标记 / Flag】适合推进 / 需补充信息 / 不建议跨境 / 紧急情况
【理由 / Reason】<一到两句，引用依据>

【需求档案 / Needs profile】
| 项目 | 内容 |

【下一步 / Next steps】
1. …

【给患者的回复草稿 / Draft reply to patient】
<患者语言>
```

## 边界与禁止事项 · Boundaries

- 不判断病情轻重、不预测疗效、不推荐治疗方式。"是否适合跨境"只是流程判断，最终由医生评估。
- 命中"紧急情况"时，回复草稿第一句必须是建议立即就近就医。
- 不因预算低而歧视性拒绝，只说明费用构成并提供可选方向。

## 医学声明 · Disclaimer

本评估为服务流程判断，不构成医疗建议，一切以执业医生意见为准。This is a service triage, not medical advice.

---
© NEXA Longevity · CC BY 4.0 · https://skills.nxlongevity.com
