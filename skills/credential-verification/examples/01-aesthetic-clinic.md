# 示例 1：核验一家医美诊所与其注射项目

> 虚构内容 / Fictional content

## 输入 Input

- target_type: facility + aesthetic_doctor + drug
- name: 深圳某医疗美容门诊部；主诊医师 [已隐去]；某品牌玻尿酸
- claimed_items: 可做美容外科、美容皮肤科；医生为主诊医师；产品获批

## 输出 Output

```
【对象 / Subject】深圳某医疗美容门诊部（虚构）

【知识库 / Knowledge base】未收录（v0.1 知识库不含医美机构）

【官方核验 / Official checks】
| 项目 | 渠道 | 查询日期 | 结果 | 存档 |
|---|---|---|---|---|
| 医疗机构执业许可 | 深圳市卫健委公开查询 | 2026-11-27 | 一致 | screenshots/01.png |
| 核准医疗美容科目 | 同上 | 2026-11-27 | 仅核准美容皮肤科，未见美容外科 | screenshots/02.png |
| 医师执业注册 | 国家卫生健康委政务服务平台 | 2026-11-27 | 一致 | screenshots/03.png |
| 主诊医师资格 | 向机构索取证明并向卫健委核实 | — | 待核实 | — |
| 产品注册 | 国家药监局数据查询 | 2026-11-27 | 已注册，核对适应症与注射部位 | screenshots/04.png |

【结论 / Result】部分核实：美容外科项目不得推荐；注射项目待主诊医师资格核实后再推荐
【下一步 / Next】partner-hospital-due-diligence 补充现场与合同审查
```
