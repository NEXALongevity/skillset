# 示例 1：试管婴儿咨询，适合推进

> 虚构病例 / Fictional case

## 输入 Input

```
Hi, I'm 36 and my husband is 39, we live in Singapore. We've had 2 failed IVF cycles here. A friend did IVF in China. Can you help us find a good reproductive centre? Budget around SGD 30,000. We could come in February or March. We speak English and Mandarin.
```

## 输出 Output

```
【标记 / Flag】适合推进
【理由 / Reason】诉求明确（生殖方向，曾两次试管失败），时间与预算已给出，无紧急或不宜出行情况。

【需求档案 / Needs profile】
| 项目 | 内容 |
|---|---|
| 方向 | 生殖 |
| 病情概况 | 女方 36 岁，男方 39 岁；在新加坡两次 IVF 未成功（患者自述） |
| 诉求类型 | 治疗（辅助生殖） |
| 期望时间 | 2 至 3 月（按咨询日期推断为 2027 年，待确认） |
| 预算 | 约 3 万新元，自费 |
| 语言 | 英语、普通话 |
| 国籍与所在地 | 所在地新加坡，国籍待确认 |
| 出行条件 | 未提及限制 |

【下一步 / Next steps】
1. 收集材料：两次 IVF 的周期记录、双方近期检查（激素、精液分析等）、婚姻证明（中国辅助生殖通常要求，需与医院确认）
2. 用 medical-record-summary 整理摘要
3. 用 doctor-matching 匹配生殖方向候选中心

【给患者的回复草稿 / Draft reply to patient】
Thank you for reaching out. We can help you explore reproductive centres in China. To match you with suitable centres, could you share the records from your two IVF cycles and any recent test results for both of you? Please also confirm your nationality, as some documents (such as a marriage certificate) are usually required by Chinese fertility clinics. Final treatment decisions will be made with the doctors.
```
