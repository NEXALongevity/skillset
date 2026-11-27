# 示例 2：投诉复盘

> 虚构内容 / Fictional content

## 输入 Input

- issues: 患者投诉报价中未包含复查费
- outcome_service: 已沟通，按合同处理

## 输出 Output

```
【复盘 / Review】
- 问题：报价单未写明复查费不包含
- 根因：cost-estimate 漏项检查未覆盖出院后复查
- 改进：MCP cost_checklist 骨科清单加入"出院后复查"；quote-builder 的"不包含"栏必须填写

【反哺 / Updates】Skill：quote-builder、cost-estimate
```
