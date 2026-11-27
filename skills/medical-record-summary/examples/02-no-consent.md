# 示例 2：未取得同意时的处理

> 虚构病例 / Fictional case

## 输入 Input

- consent_status: unknown
- request: "Knee replacement in Shanghai, please summarise."
- records: X-ray report (English, Sydney, 2026-10-05): severe right knee osteoarthritis, Kellgren-Lawrence grade 4.

## 输出 Output

```
⚠ 未取得患者同意，暂不可发送。请先按 compliance-check 取得书面同意，写明接收医院、用途与数据范围。

# 病历摘要 / Case Summary
材料来源：1 份，最近日期 2026-10-05   整理日期：2026-11-27   同意状态：未取得

## 一、基本信息
年龄、性别：材料未提供 / 国籍：澳大利亚（据报告出具地推测，待确认）

## 二、主诉与诉求
希望在上海行膝关节置换。

## 三、现病史（时间线）
| 日期 | 事件 | 机构 |
|---|---|---|
| 2026-10-05 | X 线：右膝重度骨关节炎，K-L 分级 4 级 | 悉尼某影像中心 |

## 七、缺失材料
- 年龄、性别、身高体重
- 既往史、用药史（尤其抗凝药）、过敏史
- 骨科门诊意见、既往保守治疗经过
- 心肺功能等术前评估资料（如有）

## 八、待确认
- 国籍与常用语言
```

本摘要由 AI 辅助整理，仅供医生参考，不构成诊断。
