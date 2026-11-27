---
name: china-practical-guide
description: "Step-by-step practical guide for patients and companions in a Chinese hospital: registration, international departments, paying, escorts, phone and data, mobile pay with foreign cards and common phrases. Use before arrival and during the stay."
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

# 在华就医实用指南 · Practical Guide to Care in China

## 用途 · Purpose

给患者和陪同人一份按步骤走的在华就医实用手册：挂号与实名、国际医疗部与普通门诊的区别、缴费与预交金、陪诊、手机与上网（含 eSIM）、绑定外卡的移动支付、常用语。合并了首批规划中的"在华就医陪同手册"。

A step-by-step practical handbook for patients and companions: registration and real-name rules, international departments versus general clinics, paying and deposits, escorts, phones and data (including eSIM), mobile pay with foreign cards, and common phrases. It absorbs the planned 'hospital companion handbook'.

## 何时使用 · When to use

- 行前一周发给患者和陪同人
- 第一次到医院前一天
- 住院期间遇到缴费、取报告等具体问题时

## 输入 · Inputs

| 字段 Field | 说明 Description | 必需 Required |
|---|---|---|
| hospital | 医院与院区 | 是 |
| visit_type | 门诊 / 住院 / 体检 | 是 |
| patient_language | 语言 | 是 |
| has_escort | 是否有陪诊或口译 | 否 |
| phone_plan | 是否已有可在中国使用的手机号或 eSIM | 否 |

## 步骤 · Steps

1. **到院前**：确认院区和楼层；准备护照原件；在医院官方公众号、小程序或国际医疗部完成实名建档（外籍患者通常可用护照）。
2. **国际医疗部 vs 普通门诊**：国际部或特需门诊一般可预约、可英文沟通，费用较高；普通门诊挂号紧张、以中文为主。按预算与语言选择，具体以医院说明为准。
3. **缴费**：多数医院支持窗口刷卡、自助机和移动支付；住院需预交金，出院时多退少补。保留每一张收据与发票。
4. **手机与上网**：出发前购买可用的国际漫游或 eSIM；部分境外应用在中国大陆可能无法正常使用，提前下载离线地图与翻译工具。
5. **移动支付**：出发前在常用移动支付应用绑定境外银行卡并完成实名，单笔限额与手续费以应用内显示为准。
6. **陪诊与口译**：说明陪诊员与医学口译的区别；医学决定由患者本人与医生沟通确定。
7. **常用语卡**：生成患者语言 + 中文 + 拼音的常用语卡（挂号、缴费、疼痛程度、过敏、紧急求助）。
8. **紧急情况**：急救 120；告知酒店前台医院名称与地址；保存使领馆联系方式（查询官网）。

## 输出格式 · Output format

```
【到院前清单 / Before you go】☐ …
【就医当天流程 / On the day】1. … 2. …
【缴费与发票 / Paying】
【手机、网络与支付 / Phone, data & payment】
【常用语卡 / Phrase card】
| 患者语言 | 中文 | 拼音 |
【紧急信息 / Emergency】
```

## 边界与禁止事项 · Boundaries

- 流程描述为通用做法，具体以所去医院公布为准，注明"请向医院确认"。
- 不推荐具体手机卡、支付或叫车品牌，只说明类型和准备方法。
- 不鼓励使用非官方黄牛或号贩。
- 陪诊员不得代替患者做医疗决定。

## 医学声明 · Disclaimer

本 Skill 仅提供信息整理与流程支持，不构成医疗建议，诊断与治疗决定以执业医生意见为准。This Skill organises information and supports workflows only; it is not medical advice. Diagnosis and treatment decisions rest with licensed physicians.

---
© NEXA Longevity · CC BY 4.0 · https://skills.nxlongevity.com
