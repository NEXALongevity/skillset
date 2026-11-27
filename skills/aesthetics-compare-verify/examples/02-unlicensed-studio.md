# 示例 2：客户提供的工作室不具备资质

> 虚构病例 / Fictional case

## 输入 Input

- procedures: 光电祛斑
- candidate_clinics: 社交媒体上的某美容工作室

## 输出 Output

```
【资质核验 / Credentials】
| 项目 | 结果 |
|---|---|
| 医疗机构执业许可 | 查不到（以所在地卫健委公开查询为准，查询日期 2026-11-27） |
| 医疗美容科目 | 查不到 |

【不建议 / Excluded】该工作室未查到医疗机构执业许可，光电治疗属于医疗美容，不列入方案
【下一步 / Next】改为在已核准美容皮肤科的机构中选择，走 credential-verification
```
