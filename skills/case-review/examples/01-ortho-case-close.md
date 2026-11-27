# 示例 1：骨科案例结案复盘

> 虚构内容 / Fictional content

## 输入 Input

- case_timeline: 首次咨询 D0；匹配方案 D2；预约确认 D9；入境 D30；手术 D33；出院 D40；回国 D55
- outcome_service: 按计划完成，延期 0 天
- issues: 医院国际部联系人变更，预约邮件 5 天无回复
- data_errors: 知识库中该院国际部邮箱已失效

## 输出 Output

```
【案例概要 / Case summary】50–59 岁，大洋洲，骨科，膝关节置换

【指标 / Metrics】首次咨询到匹配方案：2 天（目标 ≤ 2 天，达标）

【复盘 / Review】
- 问题：预约邮件 5 天无回复
- 根因：国际部联系人变更，知识库邮箱失效
- 改进：appointment-booking 的 48 小时电话跟进规则执行；负责人：顾问组

【反哺 / Updates】数据：更新该院 international_dept，附官网来源与核实日期
```
