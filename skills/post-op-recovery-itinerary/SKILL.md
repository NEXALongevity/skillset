---
name: post-op-recovery-itinerary
description: "Plan the recovery phase after surgery in China: where to stay, rehab sessions, wound checks, red flags, fitness-to-fly confirmation and the handover home, strictly following the surgeon's instructions. Use from discharge to departure."
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

# 术后康复行程 · Post-operative Recovery Itinerary

## 用途 · Purpose

从出院到回国之间的康复安排：住哪里、康复治疗、伤口复查、警示信号、由医生确认是否适合乘机，以及回国交接。所有时间点以主刀医生和康复医生的书面意见为准。

Plan the stretch from discharge to flying home: where to stay, rehab sessions, wound checks, red flags, the surgeon's fitness-to-fly confirmation and the handover home, strictly following written instructions from the surgical and rehab teams.

## 何时使用 · When to use

- 手术确定后，提前规划康复期
- 出院当天更新行程
- 康复进度变化、需要延长停留时

## 输入 · Inputs

| 字段 Field | 说明 Description | 必需 Required |
|---|---|---|
| procedure | 手术名称与日期 | 是 |
| discharge_orders | 出院医嘱：复查时间、康复要求、活动限制 | 是 |
| mobility | 行动能力 | 是 |
| return_flight | 计划返程日期与航程时长 | 是 |

## 步骤 · Steps

1. **住处**：靠近医院、无障碍、有电梯；需要时安排护理或陪护。
2. **日程**：按医嘱排康复治疗、换药、拆线、复查。
3. **警示信号**：出院小结中列出的情况；没有列出时向医生索取。
4. **乘机确认**：返程前由医生书面确认可以乘机；需要轮椅或特殊协助时提前向航空公司申请；长途飞行的血栓预防措施由医生决定。
5. **改期预案**：医生不同意按期乘机时，改签与延住的方案。
6. **交接**：交给 return-followup-handover。

## 输出格式 · Output format

```
【康复日程 / Recovery schedule】
| 日期 | 术后第几天 | 安排 | 地点 | 备注 |
【警示信号 / Red flags】
【乘机确认 / Fit to fly】
【改期预案 / Plan B】
```

## 边界与禁止事项 · Boundaries

- 不安排早于医生允许的乘机或活动。
- 不给出康复训练的强度处方，按康复医生要求执行。
- 警示信号出现时先就医。

## 医学声明 · Disclaimer

本 Skill 仅提供信息整理与流程支持，不构成医疗建议，诊断与治疗决定以执业医生意见为准。This Skill organises information and supports workflows only; it is not medical advice. Diagnosis and treatment decisions rest with licensed physicians.

---
© NEXA Longevity · CC BY 4.0 · https://skills.nxlongevity.com
