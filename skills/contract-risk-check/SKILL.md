---
name: contract-risk-check
description: Review medical-travel contracts (patient service agreements, partner and referral agreements, hospital cooperation) against a checklist of risk points such as liability, refunds, data transfer and commission disclosure, and flag clauses for a lawyer. Use before signing.
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

# 合同风险检查 · Contract Risk Check

## 用途 · Purpose

按清单检查跨境医疗相关合同的风险点：患者服务协议、海外合作中介或转诊协议、与医院的合作协议。重点看责任划分、退款、医疗纠纷处理、数据跨境、佣金披露、争议解决。它标出风险并建议问律师的问题，不出具法律意见。

Check medical-travel contracts (patient service agreements, partner or referral agreements, hospital cooperation) against a risk checklist: liability split, refunds, handling of medical disputes, cross-border data, commission disclosure and dispute resolution. It flags risks and questions for a lawyer; it is not legal advice.

## 何时使用 · When to use

- 与新合作方、新医院签约前
- 修订患者服务协议时
- 发生纠纷前后复核合同条款时

## 输入 · Inputs

| 字段 Field | 说明 Description | 必需 Required |
|---|---|---|
| contract_text | 合同全文 | 是 |
| contract_type | patient-service / partner-referral / hospital-cooperation | 是 |
| our_role | NEXA 在合同中的角色 | 是 |
| jurisdictions | 涉及的国家或地区 | 是 |

## 步骤 · Steps

1. **角色定位**：明确 NEXA 是服务协调方，不是医疗服务提供方；检查合同是否把医疗责任错误地归到协调方。
2. **逐项检查**：服务范围；医疗责任与医疗纠纷处理路径；费用、退款与取消；佣金或推荐费披露；个人信息与健康数据跨境（同意、最小必要、存储地）；宣传用语限制；保密；终止；争议解决与适用法律。
3. **标出缺失条款**与对 NEXA 明显不利或对患者不公平的条款。
4. **生成问律师的问题清单**。

## 输出格式 · Output format

```
【合同概况 / Overview】
【风险点 / Risks】
| 条款 | 原文摘要 | 风险 | 建议问律师 |
【缺失条款 / Missing】
【结论 / Result】可签 / 修改后再签 / 需律师审阅
```

## 边界与禁止事项 · Boundaries

- 不出具法律意见，不判断合同效力。
- 引用法规只写名称，条款以官方文本为准。
- 涉及金额与责任的结论一律建议律师审阅。

## 医学声明 · Disclaimer

本 Skill 仅提供信息整理与流程支持，不构成医疗建议，诊断与治疗决定以执业医生意见为准。This Skill organises information and supports workflows only; it is not medical advice. Diagnosis and treatment decisions rest with licensed physicians.

---
© NEXA Longevity · CC BY 4.0 · https://skills.nxlongevity.com
