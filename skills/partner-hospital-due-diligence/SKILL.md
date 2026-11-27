---
name: partner-hospital-due-diligence
description: "Run a structured due-diligence checklist before onboarding a partner hospital or clinic: licences and scope, international services, pricing transparency, complaint handling, data practices and site visit notes, with sources and dates. Use before any new partnership."
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

# 合作医院尽职调查 · Partner Hospital Due Diligence

## 用途 · Purpose

新合作医院或诊所上线前，按统一清单做尽职调查：执业许可与诊疗科目、医生资质抽查、国际服务能力、价格透明度、投诉与纠纷处理、病历与数据管理、实地考察记录。每项写明来源与日期，形成可复核的档案。

Before onboarding a partner hospital or clinic, run one checklist: licence and approved scope, spot checks on doctors, international services, pricing transparency, complaint handling, records and data practices, and site-visit notes, each with source and date.

## 何时使用 · When to use

- 签合作协议前
- 合作满 12 个月复核时
- 出现投诉或负面信息时

## 输入 · Inputs

| 字段 Field | 说明 Description | 必需 Required |
|---|---|---|
| facility | 机构名称与城市 | 是 |
| type | 公立 / 民营 / 外资 | 是 |
| services | 拟合作的服务方向 | 是 |
| site_visit | 是否已实地考察 | 否 |

## 步骤 · Steps

1. **资质**：用 credential-verification 核验执业许可、诊疗科目（医美核对医疗美容科目）。
2. **医生抽查**：拟合作方向的主要医生，抽查执业注册。
3. **国际服务**：国际部、外语能力、口译、国际支付与保险直付。
4. **价格透明**：是否提供书面报价与明细、预交金与退款规则。
5. **质量与投诉**：公开的行政处罚信息（所在地卫健委、市场监管公开渠道）、投诉处理流程。
6. **数据**：病历传输方式、对跨境数据的处理与同意。
7. **实地考察**：环境、流程、接待能力，照片存档。
8. **结论与复核日期**。

## 输出格式 · Output format

```
【机构 / Facility】
【检查表 / Checklist】
| 维度 | 检查项 | 来源 | 日期 | 结果 |
【风险 / Risks】
【结论 / Result】通过 / 有条件通过 / 不通过；下次复核日期
```

## 边界与禁止事项 · Boundaries

- 只记录可查证的事实，不传播未经核实的负面传闻。
- 查不到的信息写"未查到"。
- 结论供内部决策，不对外公开评级。

## 医学声明 · Disclaimer

本 Skill 仅提供信息整理与流程支持，不构成医疗建议，诊断与治疗决定以执业医生意见为准。This Skill organises information and supports workflows only; it is not medical advice. Diagnosis and treatment decisions rest with licensed physicians.

---
© NEXA Longevity · CC BY 4.0 · https://skills.nxlongevity.com
