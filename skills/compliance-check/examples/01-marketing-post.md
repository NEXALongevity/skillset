# 示例 1：社交媒体宣传文案

> 虚构内容 / Fictional content

## 输入 Input

- content_type: marketing
- patient_region: 阿联酋 UAE

```
Come to China for the BEST cancer hospital in the world! Our partner doctors cured Mr. Ahmed's stage IV liver cancer in just 3 months — 100% success rate, no side effects. Book now and save 50%!
```

## 输出 Output

```
【检查结论 / Result】需修改

【逐项结果 / Checklist】
| 编号 | 检查项 | 结果 | 说明 |
|---|---|---|---|
| 1 | 可识别个人信息 | 风险 | 出现患者姓名 [已隐去] |
| 2 | 跨境数据同意 | 不适用 | |
| 4 | 告知费用与关系 | 风险 | "save 50%" 未说明折扣对象与条件 |
| 6 | 医学结论 | 风险 | "cured … in 3 months" 属于疗效结论 |
| 7 | 医学声明 | 风险 | 缺少 |
| 8 | 承诺疗效 | 风险 | "BEST""cured""100% success rate""no side effects" |
| 9 | 患者证言 | 风险 | 以具体患者案例证明疗效 |
| 10 | 数据来源 | 风险 | "100%" 无来源 |

【修改建议 / Suggested fixes】
- "the BEST cancer hospital in the world" → "leading cancer centres listed in China's public specialty rankings (source: …)"
- 删除患者姓名和治愈案例
- "100% success rate, no side effects" → 删除
- "save 50%" → 写明具体服务项目与条件，或删除
- 结尾加上标准医学声明

【适用法规提示 / Regulations to consider】
- 中国医疗广告相关规定（不得保证疗效、不得使用患者名义作证明）
- 患者所在地（阿联酋）的医疗广告与消费者保护规定，请当地确认

【提醒 / Note】本检查为自检工具，重大事项请咨询律师。
```
