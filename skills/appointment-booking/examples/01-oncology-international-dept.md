# 示例 1：印尼患者预约上海肿瘤专科医院国际医疗部

> 虚构病例 / Fictional case

## 输入 Input

- hospital: 上海某肿瘤专科医院（知识库 id 见档案）
- department_or_doctor: 乳腺外科
- preferred_dates: 2027-01-12 至 01-16；或 01-19 至 01-23
- record_summary: 已完成中英文摘要
- patient_language: 印尼语，可用英语，需口译
- identity_doc_type: 护照

## 输出 Output

```
【预约申请 / Request】
Subject: Appointment request – international patient, Breast Surgery
Dear International Medical Department,
We are writing on behalf of an international patient from Indonesia who would like an outpatient consultation with the Breast Surgery department. A bilingual medical summary and the list of recent imaging are attached. Preferred dates: 12–16 Jan 2027, or 19–23 Jan 2027. The patient speaks English; an interpreter would be appreciated. Could you advise on availability, consultation fees and documents to bring?
（中文版同步附上）

【跟进记录 / Tracking】
| 日期 | 动作 | 对方回复 | 下一步 |
|---|---|---|---|
| D0 | 邮件提交 | — | 48 小时后电话跟进 |

【待确认 / To confirm】院区与楼层、是否需空腹抽血、原始影像光盘是否需带、取消规则
```
