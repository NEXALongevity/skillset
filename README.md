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

## Skills（共 34 个）

| 阶段 Stage | Skill | 目录 Directory | 版本 | MCP |
|---|---|---|---|---|
| 了解 Learn | 中医康养目的地 TCM & Wellness Destinations | `skills/tcm-wellness-destinations` | v0.2 |  |
| 了解 Learn | 中国医疗体系导览 China Healthcare Guide | `skills/china-healthcare-guide` | v0.1 |  |
| 了解 Learn | 医生与机构档案查询 Hospital & Doctor Lookup | `skills/hospital-lookup` | v0.1 |  |
| 了解 Learn | 治疗方案对比 Treatment Option Comparison | `skills/treatment-comparison` | v0.2 |  |
| 评估 Assess | 中医体质辨识 TCM Body Constitution Self-Assessment | `skills/tcm-constitution` | v0.2 |  |
| 评估 Assess | 体检报告解读 Check-up Report Explainer | `skills/checkup-report-explainer` | v0.2 |  |
| 评估 Assess | 初步需求评估 Initial Needs Assessment | `skills/needs-assessment` | v0.1 |  |
| 评估 Assess | 病历整理与医学翻译 Medical Record Summary & Translation | `skills/medical-record-summary` | v0.1 |  |
| 评估 Assess | 病历翻译 Medical Record Translation | `skills/medical-record-translation` | v0.2 |  |
| 评估 Assess | 第二诊疗意见准备 Second Opinion Preparation | `skills/second-opinion-prep` | v0.2 |  |
| 评估 Assess | 长寿与生物年龄评估 Longevity & Biological Age Assessment | `skills/longevity-bioage` | v0.2 |  |
| 匹配 Match | 医生与方案匹配 Doctor & Treatment Matching | `skills/doctor-matching` | v0.1 |  |
| 匹配 Match | 医生与机构资质核验 Doctor & Facility Credential Check | `skills/credential-verification` | v0.2 | ★ MCP |
| 匹配 Match | 医生号源查询与预约 Specialist Appointment Booking | `skills/appointment-booking` | v0.2 |  |
| 匹配 Match | 医美项目对比与资质核验 Aesthetic Procedure Comparison & Verification | `skills/aesthetics-compare-verify` | v0.2 | ★ MCP |
| 匹配 Match | 报价单生成 Quote Builder | `skills/quote-builder` | v0.2 |  |
| 匹配 Match | 费用预估与比价 Cost Estimate & Quote Comparison | `skills/cost-estimate` | v0.2 | ★ MCP |
| 匹配 Match | 远程会诊安排 Teleconsultation Coordination | `skills/teleconsult-coordination` | v0.2 |  |
| 就医 Travel | 在华就医实用指南 Practical Guide to Care in China | `skills/china-practical-guide` | v0.2 |  |
| 就医 Travel | 家属陪同指南 Family Companion Guide | `skills/family-companion-guide` | v0.2 |  |
| 就医 Travel | 签证与入境政策查询 Visa & Entry Policy Lookup | `skills/visa-entry-policy` | v0.2 | ★ MCP |
| 就医 Travel | 签证与行程规划 Visa & Itinerary Planning | `skills/visa-itinerary` | v0.1 |  |
| 就医 Travel | 跨境支付与保险理赔 Cross-border Payment & Insurance Claims | `skills/payment-insurance-claims` | v0.2 |  |
| 康复 Recover | 回国随访交接 Return-home Follow-up Handover | `skills/return-followup-handover` | v0.2 |  |
| 康复 Recover | 慢病随访 Chronic Care Follow-up | `skills/chronic-care-followup` | v0.2 |  |
| 康复 Recover | 术后康复行程 Post-operative Recovery Itinerary | `skills/post-op-recovery-itinerary` | v0.2 |  |
| 康复 Recover | 营养与运动 Nutrition & Exercise Planning | `skills/nutrition-exercise` | v0.2 |  |
| 全程 All | 合作医院尽职调查 Partner Hospital Due Diligence | `skills/partner-hospital-due-diligence` | v0.2 |  |
| 全程 All | 合同风险检查 Contract Risk Check | `skills/contract-risk-check` | v0.2 |  |
| 全程 All | 合规与风险检查 Compliance & Risk Check | `skills/compliance-check` | v0.1 |  |
| 全程 All | 多语言沟通 Multilingual Communication | `skills/multilingual-communication` | v0.1 |  |
| 全程 All | 多语言沟通话术 Multilingual Communication Scripts | `skills/multilingual-scripts` | v0.2 |  |
| 全程 All | 案例记录与复盘 Case Record & Review | `skills/case-review` | v0.2 |  |
| 全程 All | 药物与保健品相互作用 Drug & Supplement Interaction Check | `skills/drug-supplement-interactions` | v0.2 |  |

睡眠管理由易见康按自身节奏推进，不在本库范围内。

## MCP · 实时信息与计算

Skill 引流，MCP 连接。三个只读 MCP 服务部署在 Cloudflare，免登录，每条结果附官方来源与核实日期：

- 签证与入境政策查询：`https://mcp.nxlongevity.com/mcp/visa`
- 费用预估与比价（不含任何价格数据，只做计算与漏项检查）：`https://mcp.nxlongevity.com/mcp/cost`
- 医生与机构资质核验（知识库 + 官方核验渠道）：`https://mcp.nxlongevity.com/mcp/credentials`

```bash
claude mcp add --transport http nexa-travel https://mcp.nxlongevity.com/mcp
```

详见 [mcp/README.md](mcp/README.md)。

基础 MCP 可直接使用。需要审核的 MCP 接入由 NEXA Care 接收申请，入口启用状态由 MCP 服务返回。申请仅用于评估业务用途与接入需求，使用 [MCP 申请说明](mcp/README.md#applications-for-reviewed-mcp-access)。

知识库 v0.1：六个方向各前 10 家医院，共 60 条，取自复旦大学医院管理研究所《2023年度中国医院专科声誉排行榜》，见 `data/hospitals/`。

| 方向 | 对应榜单专科 |
|---|---|
| 肿瘤 oncology | 肿瘤学 |
| 心脑血管 cardio-cerebrovascular | 心血管病（脑血管相关专科 v0.2 补充） |
| 生殖 reproductive | 生殖医学 |
| 体检与抗衰老 checkup-longevity | 健康管理 |
| 骨科 orthopedics | 骨科 |
| 医疗美容 aesthetics | 整形外科 |

中医方向：该榜单没有中医专科，v0.2 选定权威公开名单后加入。

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

## 社区 · Community

- 💬 [GitHub Discussions](https://github.com/NEXALongevity/skillset/discussions)：提问、提需求、分享用法 · Q&A, ideas and show-and-tell
- 微信交流群筹建中，开放后会在这里贴二维码 · WeChat group coming soon
