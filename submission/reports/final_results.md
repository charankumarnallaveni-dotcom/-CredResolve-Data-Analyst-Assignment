# Final Verified Results & Audit Summary

**Project**: Data Analyst Assessment — Collections Audit & Analytics Platform  
**Data Scope**: 12-Month Collections Dataset (30,000 Accounts, 18 Systems)  
**Execution Timestamp**: 2026-08-21  

---

## 1. Core Audit Results Summary

```
+---------------------------------------------------------------------------------------------------+
| FINAL VERIFIED RESULTS SUMMARY                                                                    |
+------------------------------------+-----------------------+--------------------------------------+
| Audit Metric                       | Verified Output Value | Business Meaning / Impact            |
+------------------------------------+-----------------------+--------------------------------------+
| Claimed Recovery Improvement       | +11.0% MoM            | Legacy C-suite narrative (Cherry-picked)|
| Actual Recovery Trend (Jan ➔ Jul)  | **-19.9% Net Decline**| Recovery Rate dropped 9.01% ➔ 7.22%  |
| Monthly Recovery Rate Average      | -1.95% MoM            | Growth was negative in 4 of 6 months |
| Reported Gross Recovery            | ₹1,917,258,617.15     | Raw uncleaned payment payload sum    |
| Independent Clean Recovery         | ₹1,149,909,180.16     | Verified net SUCCESS bank settlements|
| Gross Over-Reporting Bias          | **+₹767,349,437**     | **+66.73% Over-Reporting Inflation** |
+------------------------------------+-----------------------+--------------------------------------+
```

---

## 2. Main Operational Drivers

1. **Portfolio DPD Mix Deterioration (FACT - 55% of Net Drop)**: Queue volume shifted toward >60 DPD accounts, causing a **-14.3% drop in recovery yield per account**.
2. **Uncollected & Duplicate Payment Ingestion (FACT - 100% of Inflation)**: Raw data contained **₹575.8M in FAILED/PENDING payments** and **₹64.2M in duplicate payment reference retries**.
3. **March End-of-Quarter Cherry-Picking (FACT)**: The +11% claim was based on March 2026 (+12.23% gross), ignoring declines in Feb (-9.57%), Apr (-5.83%), and Jun (-4.55%).
4. **Digital Channel Misattribution (STRONG EVIDENCE)**: 38.4% of digital-attributed recoveries had human calls within 5 preceding days.

---

## 3. Counterfactual Analysis Result

* **Question**: What would recovery have looked like if targeting strategy had NOT changed in April 2026?
* **Method**: Difference-in-Differences (DiD) on $N=9,828$ treatment accounts (Strategy v3) vs $N=5,809$ control accounts (Strategy v2).
* **Observed Post-Period Recovery**: **₹192.38 Million**.
* **Counterfactual Post-Period Baseline**: **₹153.87 Million**.
* **Estimated Impact of Strategy Shift**: **+₹38.52 Million (+25.03% volume lift)**.
* **DiD Estimator**: **+₹3,492.80 per account** (95% CI: [+₹2,668, +₹4,317], $p < 0.001$).

---

## 4. Final ₹10 Crore Investment Recommendation

* **Recommended Option**: **OPTION 4 — BETTER BORROWER TARGETING**
* **Expected 12-Month Net Incremental Recovery**: **₹168,480,000** (INR 168.48 Million)
* **Expected 12-Month Base ROI**: **+68.5%** (Base Case) | **+110.6%** (Upside Case)
* **Break-Even Period**: **7.1 Months**
* **Downside Scenario ROI**: **+15.2%** (Only option with positive downside ROI)
* **Confidence Level**: **HIGH** (Backed by DiD model & Golden Dataset DPD shift audit)

---

## 5. Key Limitations

1. **Telephony Call Duration Skew**: Call duration logs vary across 3 vendors; 1.5% of calls lacked end-of-call timestamps.
2. **14-Day Lookback Attribution Window**: 14-day lookback is an analytical convention; short-window digital nudges may have lower attribution weight.
3. **Macro-Economic Unobservables**: Macro-economic borrower liquidity shifts could not be directly observed in operational logs.
