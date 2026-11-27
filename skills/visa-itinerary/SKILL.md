---
name: visa-itinerary
description: Build a visa checklist and day-by-day medical travel itinerary for a patient coming to China, with entry options to verify, documents, accommodation near the hospital, local transport and buffer days for recovery. Use once a hospital and dates are confirmed.
metadata:
  version: 0.1.0
  stage: travel
  owner: NEXA Longevity
  reviewed_by: ""
  reviewed_on: ""
  languages: [zh, en]
  license: CC-BY-4.0
  author: NEXA Longevity
---

# 签证与行程规划 · Visa & Itinerary Planning

## 用途 · Purpose

在医院与就诊时间初步确定后，为患者及陪同人生成入境材料清单和按天排列的就医行程，把就诊、检查、治疗、恢复与返程衔接起来，避免因签证或行程问题耽误就医。

Once the hospital and dates are set, produce an entry-document checklist and a day-by-day itinerary that links appointments, tests, treatment, recovery and the flight home.

## 何时使用 · When to use

- 医院确认接收、就诊日期基本确定后
- 治疗计划变化（如住院延长）需要调整行程时
- 医美、牙科等需要多次往返的项目，规划分次行程时

## 输入 · Inputs

| 字段 Field | 说明 Description | 必需 Required |
|---|---|---|
| nationality | 患者及陪同人的国籍与护照类型 | 是 |
| departure_city | 出发城市 | 是 |
| hospital / city | 目标医院与城市 | 是 |
| treatment_plan | 医院给出的就诊安排：门诊、检查、住院天数、术后复查时间 | 是 |
| mobility | 行动能力：正常 / 需轮椅 / 需医疗转运 | 是 |
| companions | 陪同人数 | 否 |
| budget_level | 住宿档次：经济 / 舒适 / 高端 | 否 |

## 步骤 · Steps

1. **入境方式（必须核实）**：根据国籍列出可能适用的入境方式（如申请签证、单方面免签、过境免签），并明确写"以中国驻外使领馆和国家移民管理局最新公布为准"。停留时长需覆盖整个治疗周期加上恢复缓冲；若可能超出免签停留期，建议办理签证。
2. **材料清单**：护照有效期（建议入境时剩余 6 个月以上）、签证申请所需材料、医院出具的就诊邀请或预约确认（如医院可提供）、病历摘要、医疗保险证明、往返机票与住宿预订。
3. **行程排期**：
   - 抵达日不安排就诊，留出休息与倒时差
   - 门诊和检查之间留出出报告的时间（向医院确认）
   - 手术或住院后按医院建议的恢复期加至少 1 至 2 天缓冲再安排返程
   - 需轮椅或转运时，标注航空公司特殊协助申请和医院接送
4. **住宿与交通**：建议住在医院附近（标注"步行或打车距离待确认"），说明支付方式准备（外卡、移动支付绑定外卡）、手机网络与常用应用。
5. **紧急信息**：列出中国急救电话 120、所在地使领馆（提示查询具体地址）、医院国际部联系方式（来自知识库）。
6. **双语输出**：给顾问的中文版和给患者的英文版。

## 输出格式 · Output format

```
【入境方式 / Entry options】（以官方最新规定为准）
【材料清单 / Document checklist】☐ …
【行程 / Itinerary】
| 日期 | 第几天 | 安排 | 地点 | 备注 |
【住宿与交通 / Stay & transport】
【紧急信息 / Emergency】
【待确认 / To confirm】
```

## 边界与禁止事项 · Boundaries

- 签证与免签政策变化快，不凭记忆断言某国一定免签或可停留多少天；只列出选项并要求核实。
- 不代办签证、不填写官方表格中的个人信息。
- 不安排违背医生建议的行程，如术后过早乘机；医院未给出恢复期时写入"待确认"。
- 不推荐具体航班或酒店品牌，只给选择标准。

## 医学声明 · Disclaimer

本行程为服务规划，不构成医疗或法律建议；出行与恢复安排以执业医生意见为准，入境政策以官方公布为准。This itinerary is a service plan, not medical or legal advice.

---
© NEXA Longevity · CC BY 4.0 · https://skills.nxlongevity.com
