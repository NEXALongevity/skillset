---
name: aesthetics-compare-verify
description: Compare medical-aesthetic options (surgical, injectables, energy devices, dental, TCM aesthetics) on recovery, trips needed and risks to discuss, and verify the clinic, doctor and product credentials before booking. Use for any aesthetics enquiry.
metadata:
  version: 0.1.0
  stage: match
  owner: NEXA Longevity
  reviewed_by: ""
  reviewed_on: ""
  languages: [zh, en]
  license: CC-BY-4.0
  author: NEXA Longevity
  mcp: nexa-travel-mcp/verification_guide
---

# 医美项目对比与资质核验 · Aesthetic Procedure Comparison & Verification

## 用途 · Purpose

按《医疗美容服务管理办法》的四个科目（美容外科、美容皮肤科、美容牙科、美容中医科），对比客户关心的项目：恢复期、需要几次行程、需要和医生讨论的风险；并在预约前核验机构科目、主诊医师资格和产品注册。核验部分调用资质核验 MCP。

Compare aesthetic options across the four regulated categories (surgery, dermatology, dentistry, TCM aesthetics) on recovery, number of trips and risks to discuss, and verify the clinic's approved scope, the lead physician and product registration before booking, using the credential MCP.

## 何时使用 · When to use

- 客户咨询医美项目、想在中国做时
- 客户已选定机构、预约前核验时
- 医美与体检、旅行同程安排时

## 输入 · Inputs

| 字段 Field | 说明 Description | 必需 Required |
|---|---|---|
| procedures | 感兴趣的项目 | 是 |
| candidate_clinics | 候选机构与医生 | 否 |
| trip_constraints | 可停留天数、可往返次数 | 是 |
| health_history | 过敏、既往手术、在用药物 | 是 |

## 步骤 · Steps

1. **归类**：把每个项目归入四个科目之一，确定需要什么科目核准与什么资格的医生。
2. **对比**：列出恢复期（以机构医生说明为准）、是否需多次行程、术后多久可乘机（待医生确认）、需要与医生讨论的风险。
3. **核验**：调用 credential-verification（MCP `verification_guide`）：机构执业许可与医疗美容科目、主诊医师资格、注射产品和器械的国家药监局注册与适应症。
4. **排除**：生活美容机构、无资质工作室、未获批产品，一律不列入方案。
5. **行程**：手术类交 post-op-recovery-itinerary；牙科多次往返交 visa-itinerary。
6. 对外沟通文案用 compliance-check 检查，禁止承诺效果。

## 输出格式 · Output format

```
【项目对比 / Comparison】
| 项目 | 科目 | 恢复期（待医生确认） | 行程次数 | 需讨论的风险 |
【资质核验 / Credentials】（见 credential-verification 输出）
【不建议 / Excluded】
【下一步 / Next】
```

## 边界与禁止事项 · Boundaries

- 不承诺效果，不使用前后对比照片作疗效证明。
- 未核实资质的机构和医生不得推荐。
- 不推荐未获国家药监局批准的产品，不推荐超出注册适应症的用法。
- 恢复期与能否乘机由医生确认。

## 医学声明 · Disclaimer

本 Skill 仅提供信息整理与流程支持，不构成医疗建议，诊断与治疗决定以执业医生意见为准。This Skill organises information and supports workflows only; it is not medical advice. Diagnosis and treatment decisions rest with licensed physicians.

---
© NEXA Longevity · CC BY 4.0 · https://skills.nxlongevity.com
