---
name: nutrition-exercise
description: Turn a doctor's or dietitian's recommendations into a practical, culturally appropriate weekly meal and activity plan for recovery or prevention, with safety limits stated. Use during recovery or as part of longevity programmes; it does not prescribe.
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

# 营养与运动 · Nutrition & Exercise Planning

## 用途 · Purpose

把医生或营养师的建议落成可执行的一周饮食与运动计划，兼顾患者的饮食文化、宗教禁忌和在华期间能买到的食物。它执行医嘱，不自行开处方式的饮食或运动方案。

Turn a doctor's or dietitian's recommendations into a practical weekly meal and activity plan that respects the patient's food culture, religious restrictions and what is available in China. It implements recommendations; it does not prescribe.

## 何时使用 · When to use

- 术后恢复期、出院时医生给出饮食或活动要求后
- 体检或长寿评估后，医生建议调整生活方式时
- 患者在华长期停留、需要适应当地饮食时

## 输入 · Inputs

| 字段 Field | 说明 Description | 必需 Required |
|---|---|---|
| recommendations | 医生或营养师的书面建议 | 是 |
| restrictions | 过敏、宗教饮食（如清真）、素食等 | 是 |
| location | 所在城市与住宿条件（能否做饭） | 否 |
| activity_level | 当前活动能力与限制 | 是 |

## 步骤 · Steps

1. **提取约束**：从建议中列出硬性要求（如低盐、软食、禁止负重）和目标。
2. **饮食计划**：按一周排餐，标注在当地容易买到的食物；清真、素食等要求优先满足；在中国外出就餐时给出点餐说明卡。
3. **运动计划**：只使用医生允许的活动类型和强度；术后计划写明"由康复医师确认后再进阶"。
4. **安全提示**：列出应停止运动并联系医生的情况。
5. **复盘**：每周记录执行情况，交给 chronic-care-followup 或医生。

## 输出格式 · Output format

```
【约束 / Constraints】
【一周饮食 / Weekly meals】
【点餐卡 / Ordering card】（患者语言 + 中文）
【活动计划 / Activity】
【停止信号 / Stop and call】
```

## 边界与禁止事项 · Boundaries

- 不设定热量、营养素或运动强度的具体处方，除非来自医生或营养师。
- 不推荐保健品；涉及保健品时交给 drug-supplement-interactions。
- 不承诺减重、逆转疾病等效果。

## 医学声明 · Disclaimer

本 Skill 仅提供信息整理与流程支持，不构成医疗建议，诊断与治疗决定以执业医生意见为准。This Skill organises information and supports workflows only; it is not medical advice. Diagnosis and treatment decisions rest with licensed physicians.

---
© NEXA Longevity · CC BY 4.0 · https://skills.nxlongevity.com
