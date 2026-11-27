---
name: credential-verification
description: Check a Chinese doctor's or medical facility's credentials against the NEXA knowledge base and walk through official verification channels (licence, practising registration, aesthetic scope, approved drugs and devices). Use before recommending any provider.
metadata:
  version: 0.1.0
  stage: match
  owner: NEXA Longevity
  reviewed_by: ""
  reviewed_on: ""
  languages: [zh, en]
  license: CC-BY-4.0
  author: NEXA Longevity
  mcp: nexa-travel-mcp/credential_lookup
---

# 医生与机构资质核验 · Doctor & Facility Credential Check

## 用途 · Purpose

推荐任何医生或机构之前，先在 NEXA 知识库中查记录，再按官方渠道核验执业资质：医疗机构执业许可、医师执业注册、医疗美容科目与主诊医师、药品与器械注册。优先调用 NEXA 资质核验 MCP。它给出核验路径和结果记录模板，不替代官方查询。

Before recommending any doctor or facility, check the NEXA knowledge base, then verify credentials through official channels: facility licence, physician registration, approved aesthetic scope and lead physicians, drug and device registration. Call the NEXA credential MCP first. It provides the verification path and a record template; it does not replace the official lookup.

## 何时使用 · When to use

- doctor-matching 或 hospital-lookup 给出候选后、发给患者前
- 患者或合作伙伴推荐了知识库外的机构时
- 医美项目、民营机构、新合作机构上线前（与 partner-hospital-due-diligence 配合）

## 输入 · Inputs

| 字段 Field | 说明 Description | 必需 Required |
|---|---|---|
| target_type | doctor / facility / aesthetic_doctor / drug / device | 是 |
| name | 医生或机构名称；药械名称 | 是 |
| city | 所在城市 | 否 |
| claimed_items | 对方声称的资质（如三甲、主诊医师、某产品获批） | 否 |

## 步骤 · Steps

1. **知识库查询**：调用 MCP `credential_lookup(name)`；命中则返回来源名单、年份与核实日期；未命中写"未收录"。
2. **官方核验路径**：调用 `verification_guide(target_type)`，按返回的官方渠道逐项查询（如国家卫生健康委政务服务平台、所在省市卫健委、国家药监局数据查询）。
3. **逐项记录**：每项写查询渠道、查询日期、结果（一致 / 不一致 / 查不到）、截图存档位置。
4. **医美加查**：机构是否核准开展相应医疗美容科目；医生是否具备医疗美容主诊医师资格；使用的注射产品和器械是否在国家药监局获批，适应症是否一致。
5. **结论分级**：已核实 / 部分核实 / 未核实。未核实的对象不得写入推荐。

## 输出格式 · Output format

```
【对象 / Subject】
【知识库 / Knowledge base】命中 / 未收录（来源、年份、核实日期）
【官方核验 / Official checks】
| 项目 | 渠道 | 查询日期 | 结果 | 存档 |
【结论 / Result】已核实 / 部分核实 / 未核实
【下一步 / Next】
```

## 边界与禁止事项 · Boundaries

- 本 Skill 与 MCP 不能代替官方查询；结论只能基于实际查到的官方记录。
- 查不到不等于无资质，写"未核实"并说明原因，不下负面结论。
- 不公开医生个人联系方式等非公开信息。
- 核验记录需定期复核，超过 12 个月视为过期。

## 医学声明 · Disclaimer

资质核验结果基于查询当日的公开信息，可能变化；本 Skill 不构成法律意见或医疗建议。Verification reflects public records on the day checked and is not legal or medical advice.

---
© NEXA Longevity · CC BY 4.0 · https://skills.nxlongevity.com
