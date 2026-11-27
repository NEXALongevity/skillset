# 示例 2：出院医嘱不完整

> 虚构病例 / Fictional case

## 输入 Input

- procedure: 腹腔镜胆囊切除
- discharge_orders: 只写"一周后复查"
- return_flight: 术后第 6 天

## 输出 Output

```
【乘机确认 / Fit to fly】出院医嘱未写明可乘机时间，且复查在返程之后。
【待确认 / To confirm】
1. 请医生确认术后第 6 天能否乘机
2. 复查能否提前到返程前，或改在本国做
【改期预案 / Plan B】医生确认前不要锁定不可改签的机票
```
