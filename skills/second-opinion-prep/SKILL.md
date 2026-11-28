---
name: second-opinion-prep
description: "Prepare a complete, well-framed package for a second opinion from a Chinese specialist: questions, records checklist, timeline and consent. Use when a patient already has a diagnosis or plan and wants an independent review."
metadata:
  version: 0.3.0
  stage: assess
  owner: NEXA Longevity
  reviewed_by: ""
  reviewed_on: ""
  languages: [zh, en]
  license: CC-BY-4.0
  author: NEXA Longevity
---

# 第二诊疗意见准备 · Second Opinion Preparation

## 用途 · Purpose

当患者已有诊断或治疗方案、希望听取中国专家的第二意见时，帮助整理问题清单、病历材料、病程时间线和同意书，让会诊医生在最短时间内拿到判断所需的信息。它只准备材料，不给出第二意见本身。

When a patient already has a diagnosis or plan and wants an independent review from a Chinese specialist, assemble the questions, records, timeline and consent so the reviewing doctor gets what they need quickly. It prepares the package; it never gives the opinion itself.

## 何时使用 · When to use

- 患者在本国已确诊，想确认诊断或比较治疗方案时
- 本国方案已无更多选择，想了解中国是否有其他路径时
- 远程会诊（teleconsult-coordination）之前

## 输入 · Inputs

| 字段 Field | 说明 Description | 必需 Required |
|---|---|---|
| current_diagnosis | 现有诊断（来自原始报告） | 是 |
| current_plan | 本国医生建议的方案 | 是 |
| records | 病理、影像、化验、既往治疗记录 | 是 |
| patient_questions | 患者最想问的问题 | 是 |
| deadline | 需要答复的时间（如治疗开始前） | 否 |
| recipient_and_channel | 拟接收机构及已确认的资料传输渠道 / Proposed recipient and approved records channel | 交接前 / Before handoff |
| consent_status | 有效同意范围及核验状态 / Verified scope and status of consent | 交接前 / Before handoff |

## 步骤 · Steps

1. **框定问题 / Frame the request.** 将诉求整理成最多 5 个中立问题，注明需要答复的时间和来源。Turn the request into up to five neutral questions, and record the deadline and who supplied it.
2. **整理材料 / Inventory records.** 优先按拟接收方的材料要求整理。按语言、日期和来源记录每份材料，区分已收到、待补、待翻译与待接收方确认。缺少对方清单时，将专科材料列为建议核对项。Use the recipient's checklist when available. Track language, date and source, and separate received, missing, translation needed and recipient confirmation needed.
3. **整理时间线 / Build the timeline.** 逐项记录事件和原始来源。日期或结论冲突时并列保留，标为待澄清。Link each event to its source and flag conflicting dates or statements for clarification.
4. **检查交接条件 / Assess handoff readiness.** 确认已取得有效同意，接收机构与传输渠道已确认，且接收方要求的材料齐备。未确认时，输出「暂缓交接」和缺项、补件责任人及下一步。满足后标记「可交接」，交给人工负责人处理。Verify valid consent, recipient, approved channel and required materials. Hold the handoff when any condition is missing, and provide the action and owner. When ready, hand off to the responsible person for review.
5. **生成申请包 / Prepare the package.** 输出请求语言版本，缺省为中英双语；保留原文术语和未确认项。交接后才更新发送状态，收到接诊方确认后才标记已接案。Use the requested language, defaulting to Chinese and English. Retain source terms and uncertainties. Mark sent or accepted only with evidence of that event.

## 输出格式 · Output format

```
【会诊问题 / Questions for the reviewer】1. … 2. …
【病程时间线 / Timeline】
| 日期 | 事件 | 来源文件 |
【材料清单 / Records】☐ 已有 … ☐ 缺失 …
【同意状态 / Consent】
【交接状态 / Handoff】暂缓 / 可交接 / 已发送 / 已接案 | 依据 / Evidence
【缺项与下一步 / Blockers and next action】事项 / Item | 责任人 / Owner | 时间 / Due
```

## 边界与禁止事项 · Boundaries

- 不提供第二意见，不评价原诊断或原方案是否正确。
- 不暗示中国方案一定更好，问题表述保持中立。
- 材料缺失时如实标注，不用推测补齐。
- 切片、蜡块等实物寄送需遵守双方国家规定，提示向医院确认。
- 材料保留在获准处理病历的工作环境；公共 MCP、公开社群和 MCP 准入申请均不用于传输病例。Keep records in the approved environment for clinical documents. Public MCP, community channels and MCP access applications are separate from medical-record transfer.

## 医学声明 · Disclaimer

本 Skill 仅提供信息整理与流程支持，不构成医疗建议，诊断与治疗决定以执业医生意见为准。This Skill organises information and supports workflows only; it is not medical advice. Diagnosis and treatment decisions rest with licensed physicians.

---
© NEXA Longevity · CC BY 4.0 · https://skills.nxlongevity.com
