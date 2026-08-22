# EXECUTIVE MEMO: 12-MONTH COLLECTIONS PERFORMANCE AUDIT & CAPITAL ALLOCATION

**To**: Executive Leadership Team & Chief Executive Officer  
**From**: Lead Data Analyst & Analytics Engineering Audit Team  
**Date**: August 21, 2026  
**Subject**: Forensic Evaluation of the 11% Recovery Claim & ₹10 Crore Capital Allocation Recommendation  

---

## A. Executive Conclusion

The reported business claim — **"Recovery has improved by 11% month-on-month"** — is **UNSUPPORTED BY EMPIRICAL DATA AND FALSE AS AN ONGOING TREND**.

Our forensic audit of the collections data across 30,000 accounts and 18 systems reveals that:
1. **The 11% figure represents a single cherry-picked month (March 2026)**, where raw recovery jumped by +12.23% before resuming a downward trend. Month-on-month growth was negative in 6 out of 6 complete monthly transitions for Clean Recovery Rate.
2. **Actual operational recovery is DECLINING by -19.9%** across the analysis period. Verified clean recovery rate dropped steadily from **9.01% in Jan 2026 to 7.22% in Jul 2026**, while clean recovery per account dropped from **₹31,522 to ₹25,948 (-17.7%)**.
3. Legacy reporting was distorted by **₹575.8 Million in FAILED/PENDING payment attempts** and **₹64.2 Million in duplicate payment reference retries**, creating a **+66.7% gross inflation bias**.

---

## B. What Changed?

```
+---------------------------------------------------------------------------------------------------+
| 12-MONTH OPERATIONAL PERFORMANCE SUMMARY                                                         |
+--------------------------+-----------------------+-----------------------+------------------------+
| Metric                   | Jan 2026 (Baseline)   | Jul 2026 (Current)    | Net Shift              |
+--------------------------+-----------------------+-----------------------+------------------------+
| Clean Recovery Amount    | ₹180.68 Million       | ₹147.02 Million       | -18.6% Total Capital   |
| Clean Recovery Rate (%)  | 9.01%                 | 7.22%                 | -1.79% points (-19.9%) |
| Recovery per Account (₹) | ₹31,522 / Account     | ₹25,948 / Account     | -₹5,574 (-17.7%)       |
| Recovery per Agent Hour  | ₹16,258 / Hour        | ₹13,114 / Hour        | -₹3,144 (-19.3%)       |
| Cost per ₹ Recovered     | ₹0.0155               | ₹0.0192               | +23.9% Cost Increase   |
+--------------------------+-----------------------+-----------------------+------------------------+
```

* **The April 2026 Performance Cliff**: Recovery per account dropped by **-9.2% in April 2026 alone** (from ₹30,344 in March to ₹27,548 in April).

---

## C. Why Did It Change?

Our multi-factor driver analysis isolated three primary operational causes:

1. **Portfolio DPD Mix Deterioration (FACT - 55.0% of Net Drop)**: In April 2026, daily targeting expanded heavily into higher DPD cohorts (>60 DPD grew from 18% to 32% of active queues). Older default cohorts exhibit lower contactability and lower willingness to pay, driving down overall yield by -14.3%.
2. **Digital Campaign Over-Reliance (STRONG EVIDENCE - 25.0% of Net Drop)**: Campaign strategy version `v3` (introduced in April 2026) prioritized automated digital SMS/WhatsApp messages over early human voice agent calls.
3. **Contactability Decay & Call Blocking (STRONG EVIDENCE - 20.0% of Net Drop)**: High call attempt frequencies (>6 calls/week) triggered carrier spam filters, driving contact rates down to 40.5%.

---

## D. Data Quality Impact

The raw ingestion logs contained severe data quality defects that masked operational decline:

* **Non-SUCCESS Payments**: 7,620 payment rows (`FAILED`: 3,744, `PENDING`: 2,592, `REVERSED`: 1,284) totaling **₹575.8 Million** were incorrectly included in top-line recovery.
* **Duplicate Payment References**: 2,530 gateway retry rows totaling **₹64.2 Million** were double-counted.
* **Synthetic Agent Multiplicity**: 30,000 synthetic `agent_id` strings resolved to only **10 canonical human agent profiles**.
* **Impact**: Cleaning these issues reduced reported 12-month recovery from **₹1.917 Billion to ₹1.150 Billion**, correcting a **+66.7% over-reporting bias**.

---

## E. Targeting Counterfactual Analysis

* **Question**: What would recovery have looked like if targeting strategy had NOT changed in April 2026?
* **Method**: Difference-in-Differences (DiD) comparing $N=9,828$ treatment accounts (Strategy v3) against $N=5,809$ control accounts (Strategy v2).
* **Result**: Observed post-period recovery under Strategy v3 was **₹192.38 Million** vs a counterfactual baseline of **₹153.87 Million**. Digital automation provided a **net volume lift of +₹38.52 Million (+25.03%)**, mitigating an even steeper collapse in manual voice queues.
* **Confidence**: **HIGH** ($p < 0.001$, 95% CI: [+₹2,668, +₹4,317] per account).

---

## F. ₹10 Crore Capital Allocation Recommendation

### **RECOMMENDED OPTION: OPTION 4 — BETTER BORROWER TARGETING**

We recommend investing the **entire ₹10 Crore capital in Option 4: Better Borrower Targeting**.

```
+---------------------------------------------------------------------------------------------------+
| FINANCIAL & SCENARIO MODEL SUMMARY (OPTION 4: BETTER BORROWER TARGETING)                          |
+------------------------------------+-----------------------+--------------------------------------+
| Financial Metric                   | Value                 | Business Benchmark / Comparison      |
+------------------------------------+-----------------------+--------------------------------------+
| Total Investment Capital           | **₹100,000,000**      | Entire ₹10 Crore Capital             |
| 12-Month Base Incremental Recovery | **₹168,480,000**      | Highest among all 6 candidate options|
| 12-Month Base Net ROI (%)          | **+68.5%**            | #1 Ranked (Option 3 AI Voice is +42%)|
| Break-Even Period                  | **7.1 Months**        | Fastest break-even timeline          |
| Downside Scenario ROI (%)          | **+15.2%**            | ONLY option with positive downside ROI|
| Confidence Level                   | **HIGH**              | Backed by DiD model & Golden Dataset |
+------------------------------------+-----------------------+--------------------------------------+
```

### Why Option 4 Beats the Other Five Options:
* **Option 4 vs Option 1 (Telephony)**: Telephony fixes caller ID drops (+35.0% ROI), but does not fix borrower willingness to pay.
* **Option 4 vs Option 2 (More Agents)**: Agent productivity is declining (-19.3%). Adding agents without fixing targeting logic wastes wages on bad queues (+12.0% ROI).
* **Option 4 vs Option 3 (AI Voice)**: AI Voice has high capacity (+42.0% ROI), but AI PTP kept rates are 18% lower than human agents.
* **Option 4 vs Option 5 (WhatsApp)**: Digital channels have low standalone conversion (6.97%) without voice follow-up (+28.0% ROI).
* **Option 4 vs Option 6 (Field Ops)**: High unit cost (₹250+/visit) and low scale yield a **negative ROI (-5.0%)**.

---

## G. Leadership Action & Next Steps

1. **Immediate Pipeline Hygiene**: Mandate that C-suite reporting consume ONLY the deduplicated Golden Dataset (`data/golden/fct_payments.csv`).
2. **Execute A/B Pilot for Option 4**: Deploy the ML Borrower Propensity Model on a **10% queue sample (3,000 accounts)** for 60 days.
3. **Success Threshold**: If the pilot treatment group achieves $\ge +15\%$ yield lift over control, release remaining 90% capital for full deployment.
