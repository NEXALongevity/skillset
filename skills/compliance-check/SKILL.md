---
name: compliance-check
description: Self-check medical-travel content and workflows for privacy, consent, medical-boundary and advertising risks before sending or publishing. Use for patient messages, marketing copy, case write-ups and data transfers.
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

# 合规与风险检查 · Compliance & Risk Check

## 用途 · Purpose

在对外发送或发布之前，按统一清单检查内容与流程是否存在隐私、知情同意、医学边界和宣传用语方面的风险，并给出修改建议。它是自检工具，不替代律师或监管部门的意见。

Check content and workflows against one checklist for privacy, consent, medical-boundary and advertising risks before anything is sent or published, and suggest fixes. It is a self-check, not legal advice.

## 何时使用 · When to use

- 发给患者或合作伙伴的方案、报价、介绍材料发出前
- 社交媒体、官网、宣传册等对外宣传内容发布前
- 跨境传输病历等健康数据之前
- 撰写案例、复盘或开源示例之前（检查是否残留真实个人信息）

## 输入 · Inputs

| 字段 Field | 说明 Description | 必需 Required |
|---|---|---|
| content | 待检查的文字，或流程描述 | 是 |
| content_type | patient-message / marketing / data-transfer / case-record / other | 是 |
| patient_region | 患者所在国家或地区（影响适用法规） | 否 |
| consent_status | 是否已取得患者书面同意：yes / no / unknown | 涉及个人信息时必需 |

## 步骤 · Steps

按以下四类逐项检查，每项给出 通过 / 风险 / 不适用：

**A. 隐私与数据 Privacy & data**
1. 是否包含可识别个人的信息（姓名、证件号、电话、住址、面部照片、完整病历号）？是否为完成本次任务所必需（最小必要原则）？
2. 涉及健康数据跨境传输时，是否已取得患者明确的书面同意？
3. 提示适用法规：中国《个人信息保护法》；患者在欧盟或欧洲经济区时提示 GDPR；涉及美国医疗机构时提示 HIPAA；其他地区提示"请确认当地法规"。

**B. 知情同意 Consent**
4. 是否告知患者服务内容、费用构成、可能风险，以及顾问与医疗机构的关系（是否收取机构佣金）？
5. 是否说明医疗决定由患者与执业医生共同做出？

**C. 医学边界 Medical boundary**
6. 是否出现诊断结论、治疗推荐或预后判断，且未注明来自执业医生？
7. 是否附有标准医学声明（`shared/disclaimer.md`）？

**D. 宣传用语 Advertising**（content_type = marketing 时重点检查）
8. 是否出现保证疗效、承诺结果的表述，如"根治""治愈率 100%""无副作用""零风险""最好的医院/医生"？
9. 是否使用患者形象或证言作为疗效证明？
10. 是否引用未注明来源的数据或排名？
11. 医疗美容内容是否推荐未获国家药监局批准的产品或器械，或机构、医生是否不具备相应资质？

## 输出格式 · Output format

```
【检查结论 / Result】通过 / 需修改 / 暂停发送
（任一隐私或宣传项为"风险"时，结论至少为"需修改"；未取得同意即跨境传输健康数据时，结论为"暂停发送"）

【逐项结果 / Checklist】
| 编号 | 检查项 | 结果 | 说明 |

【修改建议 / Suggested fixes】
- 原文："…" → 建议："…"

【适用法规提示 / Regulations to consider】
- …

【提醒 / Note】本检查为自检工具，重大事项请咨询律师。
```

## 边界与禁止事项 · Boundaries

- 不出具法律意见，不判断是否违法，只标出风险点与修改方向。
- 法规名称可以引用，具体条款以官方最新文本为准，不凭记忆引用条款编号。
- 检查过程中看到的个人信息不在输出中复述，用"[已隐去]"代替。

## 医学声明 · Disclaimer

本 Skill 仅提供合规自检支持，不构成法律或医疗建议。This Skill supports self-checks only and is not legal or medical advice.

---
© NEXA Longevity · CC BY 4.0 · https://skills.nxlongevity.com
