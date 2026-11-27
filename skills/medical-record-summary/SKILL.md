---
name: medical-record-summary
description: Turn a patient's multilingual medical records into a standard bilingual (Chinese-first) case summary that Chinese doctors can review quickly. Use before remote consultations, hospital referrals or doctor matching.
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

# 病历整理与医学翻译 · Medical Record Summary & Translation

## 用途 · Purpose

把患者提供的零散、多语言病历（诊断书、检查报告、出院小结、用药清单）整理成一页标准病历摘要，中文在前、英文在后，让中国医生几分钟内看清病情与诉求，提高"接诊前病历材料一次通过率"。

Turn scattered, multilingual records into a one-page standard summary (Chinese first, then English) that a Chinese doctor can review in minutes.

## 何时使用 · When to use

- 向医院国际部或医生提交会诊、转诊申请之前
- 运行"医生与方案匹配"之前
- 患者陆续补充材料，需要更新摘要时

## 输入 · Inputs

| 字段 Field | 说明 Description | 必需 Required |
|---|---|---|
| records | 病历文字或文件内容（可多份、多语言） | 是 |
| request | 患者诉求：想看哪方面、期望的治疗或第二意见 | 是 |
| consent_status | 是否已取得患者同意整理和传输其健康数据 | 是 |

consent_status 不是 yes 时，先提示取得同意（参见 `compliance-check`），可以继续整理但输出中标注"未取得同意，暂不可发送"。

## 步骤 · Steps

1. **清点材料**：列出每份材料的类型、日期、语言、出具机构。
2. **提取信息**：按模板字段提取，只用材料中写明的内容。
3. **统一术语**：译名以 `shared/glossary.yaml` 为准；检查数值保留原单位，必要时括注换算。
4. **时间线**：按日期整理诊断与治疗经过。
5. **缺失项**：对照"医生通常需要的材料"列出缺失项，例如肿瘤需病理报告和分期、影像需原始 DICOM 文件。
6. **去标识**：摘要中只保留年龄、性别、国籍；姓名、证件号、联系方式不写入摘要正文。
7. **双语输出**：先中文，后英文，内容一致。

## 输出格式 · Output format

```
# 病历摘要 / Case Summary
材料来源：<n 份，最近日期 YYYY-MM-DD>   整理日期：YYYY-MM-DD   同意状态：<已取得/未取得>

## 一、基本信息
年龄 / 性别 / 国籍 / 常用语言

## 二、主诉与诉求
## 三、现病史（时间线）
| 日期 | 事件（诊断、检查、治疗） | 机构 |
## 四、关键检查结果
## 五、既往史、过敏史、用药史
## 六、已有诊断（原文 + 译文，注明出具机构）
## 七、缺失材料
## 八、待确认

---
# Case Summary (English)
<同上结构>
```

## 边界与禁止事项 · Boundaries

- 只整理和翻译，不下诊断、不推断分期、不解读影像。原文没有的结论一律不写。
- 原文字迹不清、自相矛盾或单位不明时，写入"待确认"，不猜测。
- 不在摘要正文中保留可识别身份的信息。
- 示例与测试只用虚构病例。

## 医学声明 · Disclaimer

本摘要由 AI 辅助整理，仅供医生参考，不构成诊断；请以原始病历和执业医生意见为准。This summary is AI-assisted, for clinician reference only, and is not a diagnosis.

---
© NEXA Longevity · CC BY 4.0 · https://skills.nxlongevity.com
