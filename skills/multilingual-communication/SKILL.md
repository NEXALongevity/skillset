---
name: multilingual-communication
description: Translate and adapt medical-travel communication between Chinese and the patient's language using the shared glossary. Use for patient messages, hospital correspondence, appointment notes and interpreting scripts.
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

# 多语言沟通 · Multilingual Communication

## 用途 · Purpose

在中国医生、医院与国际患者之间，提供术语统一、语气得体的医学笔译与口译脚本。所有译名以 `shared/glossary.yaml` 为准，保证不同顾问、不同 Skill 的译法一致。

Provide consistent medical translation and interpreting scripts between Chinese clinicians and international patients, using the shared glossary so every advisor and Skill uses the same terms.

## 何时使用 · When to use

- 把患者的咨询消息译成中文，发给医院国际部或医生
- 把医生的回复、检查要求、术前须知译给患者
- 为远程会诊或现场就诊准备双语口译脚本与常用语
- 检查一段已有译文的术语是否与术语表一致

## 输入 · Inputs

| 字段 Field | 说明 Description | 必需 Required |
|---|---|---|
| source_text | 待翻译的原文 | 是 |
| source_lang / target_lang | 源语言与目标语言（v0.1：zh、en） | 是 |
| audience | 读者：patient（患者）/ clinician（医生）/ hospital-admin（医院行政） | 是 |
| purpose | 用途：message（消息）、notice（须知）、script（口译脚本）、review（译文审校） | 否，默认 message |

## 步骤 · Steps

1. **识别术语**：找出原文中的医学、医院与行政术语，在 `shared/glossary.yaml` 中查找对应译名。
2. **翻译**：按目标读者调整语气。
   - 给患者：用平实语言，专业术语首次出现时括注解释。
   - 给医生：保留专业表达和缩写，信息简洁、按临床习惯排序。
   - 给医院行政：突出时间、材料、费用、联系人。
3. **保真检查**：数字、剂量、日期、检查名称、左右侧位逐项核对原文，不增删医学信息。
4. **标注不确定处**：原文含糊、缺字或术语表中没有的词，用 `[待确认: …]` 标出，不自行猜测。
5. **新术语**：列出术语表中缺少的术语及建议译名，供维护人员补充。

## 输出格式 · Output format

```
【译文 / Translation】
<译文正文>

【术语对照 / Terms used】
- <中文> = <English>

【待确认 / To confirm】
- <不确定之处，若无写"无 / None">

【建议新增术语 / Suggested glossary additions】
- <若无写"无 / None">
```

口译脚本（purpose = script）按"场景 → 顾问说 / 医生说 / 患者可能说"的三栏表格输出。

## 边界与禁止事项 · Boundaries

- 只翻译，不改写医学内容，不补充原文没有的诊断或建议。
- 不翻译、不传播含患者身份信息的内容，除非已取得患者同意；示例中使用虚构信息。
- 涉及用药剂量、手术方式、风险告知时，在输出末尾提示"请由医生或专业医学译员复核"。
- 术语表与原文冲突时以术语表为准，并在"待确认"中说明。

## 医学声明 · Disclaimer

本 Skill 仅提供语言支持，不构成医疗建议，医疗决定以执业医生意见为准。This Skill provides language support only and is not medical advice. Always follow a licensed physician.

---
© NEXA Longevity · CC BY 4.0 · https://skills.nxlongevity.com
