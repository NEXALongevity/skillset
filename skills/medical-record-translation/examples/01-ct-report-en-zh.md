# 示例 1：英文 CT 报告译为中文

> 虚构病例 / Fictional case

## 输入 Input

- source_lang / target_lang: en → zh
- doc_type: 检查报告
- document:
  CT CHEST WITH CONTRAST. FINDINGS: A 2.3 x 1.8 cm spiculated nodule in the right upper lobe. No mediastinal lymphadenopathy. IMPRESSION: Suspicious for malignancy; recommend tissue sampling. Dr [已隐去], 14 Oct 2026

## 输出 Output

```
【译文 / Translation】
胸部增强 CT。
所见：右肺上叶见一 2.3 × 1.8 cm 毛刺状结节。纵隔未见淋巴结肿大。
印象：可疑恶性；建议组织取样。
医生 [已隐去]，2026 年 10 月 14 日

【待核项 / Items to verify】无

【译者说明 / Translator note】本译文仅供参考，以原文为准
```
