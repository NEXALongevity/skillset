# 示例 1：血脂与肝功能异常的体检报告

> 虚构病例 / Fictional case

## 输入 Input

- age_sex: 52 岁男性
- report:
  低密度脂蛋白胆固醇 4.6 mmol/L（参考 <3.4）↑
  丙氨酸氨基转移酶 68 U/L（参考 9–50）↑
  腹部超声：脂肪肝（轻度）
- language: 英语

## 输出 Output

```
【Read first】No item requires urgent care according to the report.

【Flagged items】
| Item | Result | Reference | What it generally means | Suggested |
|---|---|---|---|---|
| LDL cholesterol | 4.6 mmol/L | <3.4 | "Bad" cholesterol; higher levels are linked with cardiovascular risk | Discuss with a GP or cardiologist; repeat test as advised |
| ALT | 68 U/L | 9–50 | A liver enzyme; raised levels can relate to fatty liver, alcohol, medicines and other causes | Ask whether repeat liver tests are needed |
| Ultrasound | Mild fatty liver | — | Fat build-up in the liver | Review with your doctor together with ALT |

【Questions for your doctor】
1. Do I need repeat lipid and liver tests, and when?
2. Could any of my current medicines affect the liver result?
3. What lifestyle changes would you recommend for me?

【Note】This explanation is not a diagnosis.
```
