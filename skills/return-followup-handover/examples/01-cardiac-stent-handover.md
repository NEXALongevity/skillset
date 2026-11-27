# 示例 1：心脏支架术后回国交接

> 虚构病例 / Fictional case

## 输入 Input

- discharge_docs: 出院小结、冠脉造影与支架植入记录、处方
- home_doctor: 新加坡某医院心内科
- followup_orders: 双联抗血小板治疗，疗程按医嘱；1 个月后门诊复查
- language: 英语

## 输出 Output

```
【交接包 / Handover pack】
☐ 出院小结（中英） ☐ 手术记录（中英） ☐ 造影影像光盘 ☐ 支架信息卡 ☐ 处方（中英）

【给本地医生的信 / Letter to home doctor】
Dear Doctor, Your patient underwent coronary angiography and stent implantation at [hospital] on [date]. Enclosed are the translated discharge summary, procedure report, imaging and prescription. The discharging team advised dual antiplatelet therapy for the duration stated in the discharge summary and an outpatient review in one month. The Chinese team can be reached via [official channel]. The patient has consented to this exchange.

【用药清单 / Medications】按处方原文列出（通用名、剂量、疗程）
【随访时间表 / Follow-up】1 个月：本地心内科门诊
```
