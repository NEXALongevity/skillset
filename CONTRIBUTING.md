# 开发规范 · Contributing Guide

本规范面向 NEXA 技术人员、Claude、Codex 及外部贡献者。所有 Skills 按同一结构开发，保证可以互相调用、统一审核。

## 1. 目录结构

```
skills/<skill-name>/
  SKILL.md          # 必需：frontmatter + 使用说明
  references/       # 可选：该 Skill 专用的知识与数据
  examples/         # 必需：至少 2 个输入输出示例（兼作测试用例）
shared/
  glossary.yaml     # 医学术语表（全库共用）
  disclaimer.md     # 标准医学声明
data/
  hospitals/<direction>.yaml   # 按方向的医院档案
  schema/hospital.schema.json  # 数据格式
scripts/
  validate.py       # 校验 SKILL.md 与数据文件
```

- 目录名：英文小写加连字符，如 `doctor-matching`。
- 从 `skills/_template/` 复制开始。

## 2. SKILL.md 要求

frontmatter 必须包含：

```yaml
---
name: doctor-matching            # 与目录名一致
description: <一句话，说明何时使用，英文，≤ 300 字符>
metadata:
  version: 0.1.0
  stage: learn | assess | match | travel | recover | cross-cutting
  owner: <负责人>
  reviewed_by: <审核人>
  reviewed_on: YYYY-MM-DD
  languages: [zh, en]
  license: CC-BY-4.0
  author: NEXA Longevity
---
```

正文必须包含以下部分：**用途、何时使用、输入、步骤、输出格式、边界与禁止事项、医学声明**。正文用中英双语书写（中文在前）。

## 3. 数据格式

医院档案遵循 `data/schema/hospital.schema.json`，每条记录至少包括：名称（中、英）、所属方向、类型（public / private / foreign）、城市、优势科室、国际部联系方式（若公开）、信息来源链接、来源名单与年份、核实日期。

- 只采用官方公开资料或经机构书面确认的内容。
- 每条记录必须有 `source_url` 和 `verified_on`。
- 不确定的字段留空，不推测。

## 4. 术语

所有译名引用 `shared/glossary.yaml`。新术语先加入术语表，再在 Skill 中使用，不在单个 Skill 中另起译名。

## 5. 开源边界

- 仓库中不得出现任何真实患者个人信息；示例一律使用虚构病例，并标注"虚构病例 / Fictional case"。
- 不得写入未公开的价格协议、合作机构内部联系方式。
- 不得夸大疗效或承诺结果，符合中国医疗广告相关规定。

## 6. 审核与发布

1. 提交 PR，运行 `python scripts/validate.py` 通过。
2. 医学审核：内容准确、不越过医学边界。
3. 合规审核：隐私、宣传用语、声明齐全。
4. 审核人填写 `reviewed_by` 和 `reviewed_on` 后合并。内容变更需重新审核并升级版本号。
