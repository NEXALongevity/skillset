# 示例 2：中文出院小结译为英文

> 虚构病例 / Fictional case

## 输入 Input

- source_lang / target_lang: zh → en
- doc_type: 出院小结
- document:
  出院诊断：右膝骨关节炎（K-L Ⅳ级），右全膝关节置换术后。出院医嘱：1. 利伐沙班 10mg qd，口服 至术后 35 天；2. 术后 2 周拆线；3. 不适随诊。

## 输出 Output

```
【译文 / Translation】
Discharge diagnosis: Right knee osteoarthritis (Kellgren-Lawrence grade IV), status post right total knee arthroplasty.
Discharge instructions:
1. Rivaroxaban 10 mg once daily (qd), oral, until postoperative day 35;
2. Suture removal at 2 weeks after surgery;
3. Seek medical review if unwell.

【待核项 / Items to verify】
| 位置 | 原文 | 问题 |
|---|---|---|
| 医嘱 2 | 术后 2 周拆线 | 回国后由本地医生拆线还是返院，原文未写明 |

【译者说明 / Translator note】This translation is for reference; the Chinese original prevails.
```
