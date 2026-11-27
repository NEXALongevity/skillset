# 示例 1：泰国患者淋巴瘤诊断复核

> 虚构病例 / Fictional case

## 输入 Input

- current_diagnosis: 弥漫大 B 细胞淋巴瘤（本国病理）
- current_plan: R-CHOP 6 周期
- records: 病理报告（英文）、PET-CT 报告、血常规；无免疫组化全套
- patient_questions: 诊断是否确定？是否有其他方案？
- deadline: 3 周后开始化疗

## 输出 Output

```
【会诊问题 / Questions for the reviewer】
1. 现有病理与免疫组化是否足以确认诊断与亚型？是否需要病理会诊？
2. 在现有分期信息下，标准方案之外是否有值得考虑的选择？
3. 开始治疗前是否需要补充检查？

【病程时间线 / Timeline】
| 日期 | 事件 | 来源文件 |
|---|---|---|
| 2026-09 | 颈部淋巴结肿大 | 门诊记录 |
| 2026-10 | 淋巴结活检 | 病理报告 |
| 2026-11 | PET-CT 分期 | PET-CT 报告 |

【材料清单 / Records】☐ 已有：病理报告、PET-CT 报告、血常规 ☐ 缺失：完整免疫组化结果、切片是否可寄送
【同意状态 / Consent】待签署
【交付去向 / Next】teleconsult-coordination，时间要求：3 周内
```
