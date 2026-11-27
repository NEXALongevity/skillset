---
name: drug-supplement-interactions
description: Build a complete medication and supplement list (including Chinese patent medicines and herbal products) and flag possible interactions for a pharmacist or doctor to confirm, citing the source checked. Use before treatment, surgery or travel.
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

# 药物与保健品相互作用 · Drug & Supplement Interaction Check

## 用途 · Purpose

整理患者正在使用的全部药物与保健品（含中成药、草药、膳食补充剂），按权威来源检查可能的相互作用，并把需要确认的问题交给药师或医生。它负责查清和提问，不负责决定停药或换药。

Compile everything a patient takes, including Chinese patent medicines, herbs and supplements, check possible interactions against authoritative sources and hand questions to a pharmacist or doctor. It finds and asks; it never decides to stop or switch a medicine.

## 何时使用 · When to use

- 来华手术或治疗前（尤其抗凝、抗血小板药物）
- 在华开了新药或中成药，回国前核对时
- 长寿或营养项目推荐保健品前

## 输入 · Inputs

| 字段 Field | 说明 Description | 必需 Required |
|---|---|---|
| medications | 药名（通用名）、剂量、频率 | 是 |
| supplements | 保健品、中成药、草药（尽量写成分） | 是 |
| planned_treatment | 计划中的手术或治疗 | 否 |
| sources | 可用的核查来源（药品说明书、药学数据库、药师） | 否 |

## 步骤 · Steps

1. **统一清单**：药名统一为通用名；中成药与保健品列出主要成分；不清楚成分的标"成分待核"。
2. **逐对检查**：只依据药品说明书、权威药学数据库或药师意见判断；每条结论写明来源。
3. **分级**：已知存在相互作用报道 / 未查到报道 / 无法核查（成分不明）。"未查到"不等于"安全"。
4. **围手术期提醒**：抗凝、抗血小板药和可能影响凝血的草药或补充剂，提示由手术医生决定是否、何时停用。
5. **生成问题清单**交给药师或医生。

## 输出格式 · Output format

```
【用药清单 / List】
| 类别 | 名称 | 成分 | 剂量 | 状态 |
【可能的相互作用 / Possible interactions】
| 组合 | 等级 | 来源 | 需要确认的问题 |
【给药师/医生的问题 / Questions】
【提醒】任何停药、换药以医生或药师意见为准
```

## 边界与禁止事项 · Boundaries

- 不建议停药、减量或替换；只提出问题。
- 结论必须注明查到的来源；不凭记忆断言。
- 成分不明的产品写"无法核查"，并建议患者带原包装就诊。

## 医学声明 · Disclaimer

本 Skill 仅提供信息整理与流程支持，不构成医疗建议，诊断与治疗决定以执业医生意见为准。This Skill organises information and supports workflows only; it is not medical advice. Diagnosis and treatment decisions rest with licensed physicians.

---
© NEXA Longevity · CC BY 4.0 · https://skills.nxlongevity.com
