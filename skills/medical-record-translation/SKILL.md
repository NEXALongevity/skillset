---
name: medical-record-translation
description: Translate full medical documents (reports, discharge summaries, prescriptions) between Chinese and the patient's language using the shared glossary, keeping numbers, units and dates exact and flagging uncertain terms. Use when a full document, not a summary, is needed.
metadata:
  version: 0.1.0
  stage: assess
  owner: NEXA Longevity
  reviewed_by: ""
  reviewed_on: ""
  languages: [zh, en]
  license: CC-BY-4.0
  author: NEXA Longevity
---

# 病历翻译 · Medical Record Translation

## 用途 · Purpose

把完整的医疗文件（检查报告、病理、出院小结、处方）在中文与患者语言之间逐段翻译，术语统一引用共享术语表，数字、单位、日期原样保留，不确定处显式标出。与 medical-record-summary 的区别：这里翻译全文，不做摘要。

Translate full medical documents (reports, pathology, discharge summaries, prescriptions) paragraph by paragraph between Chinese and the patient's language, using the shared glossary, keeping numbers, units and dates exact and flagging anything uncertain. Unlike medical-record-summary, this translates the whole text.

## 何时使用 · When to use

- 医院要求提供原始报告的中文译文时
- 出院后需要把出院小结、处方翻译给患者或本国医生时
- 保险理赔需要译文时

## 输入 · Inputs

| 字段 Field | 说明 Description | 必需 Required |
|---|---|---|
| document | 原文（文字或 OCR 结果） | 是 |
| source_lang / target_lang | 源语言与目标语言 | 是 |
| doc_type | 检查报告 / 病理 / 出院小结 / 处方 / 其他 | 是 |
| purpose | 给医生 / 给患者 / 理赔 | 否 |

## 步骤 · Steps

1. **去标识**：翻译前确认已获患者同意；示例与存档中用 [已隐去] 替换姓名、证件号、病历号。
2. **术语对照**：优先使用 `shared/glossary.yaml`；术语表没有的词保留原文并加"[术语待核]"。
3. **逐段翻译**：保持原有标题、表格结构；数值、单位、参考范围、日期不改写不换算。
4. **标记不确定**：手写或 OCR 识别不清处写"[原文不清]"，缩写不确定写"[缩写待核：XXX]"。
5. **质控**：逐项核对数字与原文一致；列出所有"待核"项。
6. 给患者看的版本可在文末附"常见术语解释"，但不加入原文没有的结论。

## 输出格式 · Output format

```
【译文 / Translation】（保持原文结构）
【待核项 / Items to verify】
| 位置 | 原文 | 问题 |
【译者说明 / Translator note】本译文仅供参考，以原文为准
```

## 边界与禁止事项 · Boundaries

- 只翻译，不解读、不补充原文没有的诊断或建议。
- 不改动数值、单位、日期，不做单位换算（如需换算，另起说明并标注）。
- 不确定处必须标出，不猜测。
- 正式公证或认证翻译需由有资质机构完成。

## 医学声明 · Disclaimer

本 Skill 仅提供信息整理与流程支持，不构成医疗建议，诊断与治疗决定以执业医生意见为准。This Skill organises information and supports workflows only; it is not medical advice. Diagnosis and treatment decisions rest with licensed physicians.

---
© NEXA Longevity · CC BY 4.0 · https://skills.nxlongevity.com
