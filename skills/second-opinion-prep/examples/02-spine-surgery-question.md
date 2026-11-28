# 示例 2：脊柱手术前听取第二意见

> 虚构病例 / Fictional case

## 输入 Input

- current_diagnosis: 腰椎间盘突出伴神经根压迫
- current_plan: 腰椎融合术
- records: MRI 报告与影像、神经电生理
- patient_questions: 是否一定要做融合？
- deadline: 无硬性期限
- recipient_and_channel: 拟接收骨科团队已确认其安全接收渠道，且确认可先审阅现有材料。
- consent_status: 已核对书面同意，覆盖该接收方和用途。

## 输出 Output

```
【会诊问题 / Questions for the reviewer】
1. 影像与症状是否支持当前诊断？
2. 融合与非融合手术、继续保守治疗，各自适用条件是什么？
3. 需要补充哪些检查（如动力位 X 光）？

【病程时间线 / Timeline】检查日期待核实，影像与电生理以原始报告为准。
【材料清单 / Records】已有：MRI（含 DICOM）、神经电生理。其他材料由接收方审阅后确认。
【同意状态 / Consent】书面同意已核验。
【交接状态 / Handoff】可交接 / Ready for handoff。接收团队、渠道及初审材料均已确认。
【缺项与下一步 / Blockers and next action】协调员复核检查日期，通过已确认渠道交接，等待接收方确认。
```
