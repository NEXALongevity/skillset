# NEXA Medical Travel Skills · 跨境医疗旅游 Skills 库

> **Longevity as a Choice.** An open-source library of AI Skills that helps cross-border medical travel professionals guide international patients to the right doctors, hospitals and treatments in China.
>
> 一套开源的 AI Skills，帮助跨境医疗从业人员为国际患者找到中国合适的医生、医院与治疗方案，并精准、及时地完成赴华就医。

Maintained by **[NEXA Longevity](https://nxlongevity.com)** · Site: <https://skills.nxlongevity.com>

---

## 适用对象 · Who it is for

- 跨境医疗从业人员与医疗顾问（首要使用者）
- 国际患者及家属、中国医生与医疗机构、海外合作伙伴
- 在 Claude、Codex 等 AI 工具中调用 Skills 的开发者

## v0.1 包含的 Skills · Skills in v0.1

| 阶段 Stage | Skill | 目录 Directory |
|---|---|---|
| 了解 Learn | 中国医疗体系导览 China healthcare guide | `skills/china-healthcare-guide` |
| 了解 Learn | 医生与机构档案查询 Hospital & doctor lookup | `skills/hospital-lookup` |
| 评估 Assess | 病历整理与医学翻译 Medical record summary & translation | `skills/medical-record-summary` |
| 评估 Assess | 初步需求评估 Initial needs assessment | `skills/needs-assessment` |
| 匹配 Match | 医生与方案匹配 Doctor & treatment matching | `skills/doctor-matching` |
| 就医 Travel | 签证与行程规划 Visa & itinerary planning | `skills/visa-itinerary` |
| 全程 All | 多语言沟通 Multilingual communication | `skills/multilingual-communication` |
| 全程 All | 合规与风险检查 Compliance & risk check | `skills/compliance-check` |

知识库 v0.1：七个重点方向（肿瘤、心脑血管、生殖、体检与抗衰老、中医、骨科、医疗美容）各前 10 家公立头部医院，见 `data/hospitals/`。

## 使用方法 · How to use

每个 Skill 是一个包含 `SKILL.md` 的目录，可直接放入 Claude Code、Claude.ai 或其他支持 Agent Skills 的工具中使用。

```bash
git clone <this-repo>
cp -r skills/doctor-matching ~/.claude/skills/
```

## 医学声明 · Medical disclaimer

本库仅提供信息整理、解释与流程支持，**不提供诊断或治疗决策，一切以执业医生意见为准**。This library provides information and workflow support only. It does not diagnose or recommend treatment. Always follow the advice of a licensed physician.

## 许可证与署名 · License & attribution

- 代码 Code：[Apache-2.0](LICENSE)
- 知识内容 Content (`skills/**/*.md`, `data/`, `shared/`)：[CC BY 4.0](LICENSE-CONTENT)

使用或改编时请署名：**"Based on NEXA Medical Travel Skills by NEXA Longevity (nxlongevity.com)"**。

## 参与贡献 · Contributing

见 [CONTRIBUTING.md](CONTRIBUTING.md)。所有 Skill 上线前须通过医学审核与合规审核。
