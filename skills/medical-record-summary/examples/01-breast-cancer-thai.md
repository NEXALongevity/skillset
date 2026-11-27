# 示例 1：泰国乳腺癌患者求第二意见

> 虚构病例 / Fictional case

## 输入 Input

- consent_status: yes
- request: "Second opinion on whether surgery or neoadjuvant therapy first; considering treatment in Guangzhou."
- records（节选）:
  - Intake form: female, 47, Thai national, speaks Thai and English.
  - Mammogram report, Bangkok, 2026-09-02 (English): left breast mass 2.8 cm, BI-RADS 5.
  - Core biopsy pathology, 2026-09-10 (English): invasive ductal carcinoma, grade 2, ER 90%+, PR 60%+, HER2 1+, Ki-67 25%.
  - Clinic note (Thai), 2026-09-15: axillary ultrasound, one suspicious left axillary lymph node; surgeon recommends surgery.
  - Medications: metformin 500 mg twice daily. Allergy: penicillin (rash).

## 输出 Output

```
# 病历摘要 / Case Summary
材料来源：4 份，最近日期 2026-09-15   整理日期：2026-11-27   同意状态：已取得

## 一、基本信息
47 岁 / 女 / 泰国 / 泰语、英语

## 二、主诉与诉求
左乳肿物，已活检确诊。希望获得第二意见：先手术还是先行新辅助治疗；考虑赴广州治疗。

## 三、现病史（时间线）
| 日期 | 事件 | 机构 |
|---|---|---|
| 2026-09-02 | 乳腺 X 线：左乳肿物 2.8 cm，BI-RADS 5 类 | 曼谷某医院 |
| 2026-09-10 | 穿刺活检病理：浸润性导管癌 | 同上 |
| 2026-09-15 | 腋窝超声：左腋窝 1 枚可疑淋巴结；外科建议手术 | 同上 |

## 四、关键检查结果
- 病理：浸润性导管癌，组织学 2 级；ER 90%+，PR 60%+，HER2 1+，Ki-67 25%

## 五、既往史、过敏史、用药史
- 用药：二甲双胍 500 mg，每日 2 次
- 过敏：青霉素（皮疹）
- 既往史：材料未提及

## 六、已有诊断
- Invasive ductal carcinoma, left breast（左乳浸润性导管癌）— 曼谷某医院病理科

## 七、缺失材料
- 乳腺 MRI 或超声原始影像（DICOM）
- 腋窝淋巴结是否穿刺及结果
- 全身分期检查（如胸部 CT、骨扫描），如已做
- 糖尿病相关近期化验（如糖化血红蛋白）

## 八、待确认
- 泰文门诊记录中淋巴结大小未写明
- 二甲双胍的用药原因（推测为糖尿病，需患者确认）

---
# Case Summary (English)
<结构同上，英文版略>
```

本摘要由 AI 辅助整理，仅供医生参考，不构成诊断。
