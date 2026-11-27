---
name: tcm-wellness-destinations
description: Introduce China's TCM and wellness destinations, including the Hainan Boao Lecheng International Medical Tourism Pilot Zone, with what each offers, entry and policy notes to verify, and selection criteria. Use when a client wants wellness or special-access care in China.
metadata:
  version: 0.1.0
  stage: learn
  owner: NEXA Longevity
  reviewed_by: ""
  reviewed_on: ""
  languages: [zh, en]
  license: CC-BY-4.0
  author: NEXA Longevity
---

# 中医康养目的地 · TCM & Wellness Destinations

## 用途 · Purpose

介绍中国的中医康养与特色医疗目的地，包括海南博鳌乐城国际医疗旅游先行区：各自提供什么、政策要点（需核实）、适合哪些客户、如何选择机构。所有政策描述附官方来源与核实日期。

Introduce China's TCM, wellness and special-access destinations, including the Hainan Boao Lecheng International Medical Tourism Pilot Zone: what each offers, policy points to verify, who it suits and how to choose a provider. Every policy statement carries an official source and as-of date.

## 何时使用 · When to use

- 客户希望把康养、中医调理与旅行结合时
- 客户询问在中国使用境外已上市、国内未上市的药械时（博鳌乐城）
- 为中东、东南亚高端客户设计康养行程时

## 输入 · Inputs

| 字段 Field | 说明 Description | 必需 Required |
|---|---|---|
| interest | 中医调理 / 康养度假 / 特许药械 / 体检 | 是 |
| nationality | 国籍（海南有单独入境政策） | 是 |
| duration | 可停留天数 | 是 |
| health_status | 健康状况，是否有在治疾病 | 是 |

## 步骤 · Steps

1. **需求归类**：养生康养（非治疗）、中医门诊调理（需执业中医师）、特许药械使用（属于医疗行为，需医生评估）。
2. **目的地介绍**：
   - 博鳌乐城：国家批准设立的国际医疗旅游先行区，政策允许在区内指定医疗机构按规定使用境外已上市、国内尚未注册的部分药品和医疗器械。具体品种、适用条件与流程以先行区管理部门公布为准。
   - 其他中医康养目的地：只介绍公开可查的机构信息，标注来源。
3. **入境**：调用 visa-entry-policy；海南另有 30 天入境免签政策（国家移民管理局公布适用国家名单），需核实国籍与目的。
4. **机构选择标准**：执业许可、中医师资质（credential-verification）、是否有国际服务、费用透明。
5. **设计行程**：交给 visa-itinerary。

## 输出格式 · Output format

```
【需求归类 / Need】
【推荐方向 / Options】
| 目的地 | 提供什么 | 适合 | 政策要点（需核实） | 来源 | 核实日期 |
【入境提示 / Entry】
【选择标准 / How to choose】
【下一步 / Next】
```

## 边界与禁止事项 · Boundaries

- 不宣称中医或康养项目能治愈疾病。
- 特许药械是医疗行为，是否适用由医生评估，不向客户承诺可以使用某药械。
- 政策描述必须附官方来源；未核实的内容写"待核实"。

## 医学声明 · Disclaimer

本 Skill 仅提供信息整理与流程支持，不构成医疗建议，诊断与治疗决定以执业医生意见为准。This Skill organises information and supports workflows only; it is not medical advice. Diagnosis and treatment decisions rest with licensed physicians.

---
© NEXA Longevity · CC BY 4.0 · https://skills.nxlongevity.com
