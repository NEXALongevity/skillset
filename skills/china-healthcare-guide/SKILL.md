---
name: china-healthcare-guide
description: Explain China's healthcare system to international patients and partners in plain language - hospital grades, public vs private vs foreign-invested hospitals, international departments, how visits and payment work. Use when someone is new to seeking care in China.
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

# 中国医疗体系导览 · China Healthcare Guide

## 用途 · Purpose

用患者听得懂的语言，介绍中国的医院分级、医院类型、国际医疗部、就诊流程与付费方式，帮助第一次考虑来中国就医的患者和海外合作伙伴建立基本认识。

Explain, in plain language, how China's hospitals are graded and organised, what international departments do, and how a visit and payment work, for patients and partners considering care in China for the first time.

## 何时使用 · When to use

- 患者问"中国的医院怎么选""三甲是什么意思""外国人能不能去公立医院"
- 向海外合作伙伴做中国医疗介绍
- 为某个方向（如肿瘤、生殖）的咨询做背景铺垫

## 输入 · Inputs

| 字段 Field | 说明 Description | 必需 Required |
|---|---|---|
| question | 患者或合作伙伴的问题 | 是 |
| audience | patient / partner | 是 |
| language | 输出语言（v0.1：zh、en） | 是 |
| direction | 关注方向，可选七个方向之一 | 否 |

## 步骤 · Steps

1. 判断问题属于以下哪一块，只讲相关部分，不要一次全部倾倒：
   - **医院分级**：中国医院分为一、二、三级，每级再分甲、乙、丙等；三级甲等（三甲）是最高等级，通常是大城市的大型综合或专科医院，疑难重症多集中在这里。
   - **医院类型**：公立医院（主体，专家资源集中）、民营医院（服务体验好、等候短，水平差异大）、外资或中外合资医院（国际化服务、英语沟通、费用较高）。
   - **国际医疗部与特需门诊**：许多大型公立医院设有国际医疗部或特需门诊，提供外语服务、预约和独立收费；不是所有医院都有，服务范围各不相同。
   - **就诊流程**：预约挂号 → 门诊就诊 → 检查 → 复诊看结果 → 住院或治疗。中国门诊量大，名专家需要提前预约。
   - **付费**：外籍患者通常自费，住院一般需要预交金；部分国际医疗部可对接国际商业保险的直付，需事先确认。
   - **中国优势**（按方向）：引用对应专科知识包或公开排名说明，不做疗效比较或承诺。
2. 按 audience 调整：对患者讲"对我意味着什么"，对合作伙伴讲"如何对接"。
3. 每个关键说法都要可核实：涉及具体医院、政策、价格时，提示"以医院或官方最新公布为准"。
4. 用 `shared/glossary.yaml` 的标准译名，首次出现的术语括注解释。
5. 结尾给出下一步建议，例如使用"初步需求评估"或"医生与机构档案查询"Skill。

## 输出格式 · Output format

```
<一句话直接回答>

<分点说明，每点不超过 3 句>

下一步 / Next step：<建议>

<标准医学声明>
```

## 边界与禁止事项 · Boundaries

- 不评价某家具体医院"最好"，只引用公开名单。
- 不给出具体价格数字，只说明费用构成和影响因素；需要报价时转"费用预估与报价"（v0.2）。
- 不承诺可以预约到某位专家或某个时间。
- 政策类信息（签证、收治外籍患者规定）只说明原则，并提示核实。

## 医学声明 · Disclaimer

本 Skill 仅提供信息介绍，不构成医疗建议，一切以执业医生意见为准。This Skill provides general information only and is not medical advice.

---
© NEXA Longevity · CC BY 4.0 · https://skills.nxlongevity.com
