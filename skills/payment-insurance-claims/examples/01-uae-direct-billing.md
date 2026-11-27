# 示例 1：阿联酋患者申请保险直付

> 虚构病例 / Fictional case

## 输入 Input

- payer: 保险直付
- insurer: 某国际医疗保险（全球计划，不含美国）
- hospital: 广州某三甲医院国际医疗部
- estimated_amount: 约 80,000 CNY（cost-estimate 结果）
- payment_tools: Visa 信用卡

## 输出 Output

```
【付款方案 / Payment plan】
| 阶段 | 金额 | 方式 | 需提前准备 |
|---|---|---|---|
| 入院前 | 担保函覆盖部分 | 保险直付 | 担保函（Guarantee of Payment） |
| 入院时 | 预交金（金额向医院确认） | Visa 信用卡 | 确认医院是否接受外卡 |
| 出院 | 保险未覆盖部分 | 信用卡 | — |

【保险 / Insurance】请患者向保险公司申请担保函，并确认该医院是否在直付网络；未获书面确认前按自费准备资金。
【理赔材料清单 / Claim pack】☐ 发票 ☐ 费用明细 ☐ 出院小结（中英） ☐ 诊断证明 ☐ 付款凭证
【待确认 / To confirm】医院是否可直接与保险公司结算；担保函有效期
```
