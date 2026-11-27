# 示例 2：回国后远程复查

> 虚构病例 / Fictional case

## 输入 Input

- hospital_doctor: 原手术医生
- package: 本地复查 CT 报告与影像
- time_zones: 悉尼 UTC+11（夏令时）
- interpreter: 不需要

## 输出 Output

```
【会诊安排 / Booking】北京时间 9:00 / 悉尼 12:00（注意夏令时）
【会诊纪要 / Summary】医生意见：…（以医院书面意见为准）
【下一步 / Next】把纪要译文发给本地医生（return-followup-handover）
```
