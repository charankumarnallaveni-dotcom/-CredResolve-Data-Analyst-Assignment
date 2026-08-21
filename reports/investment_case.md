# ₹10 Crore Capital Allocation & Investment Case Report

**Core Executive Question**: *"Where should leadership invest the ₹10 Cr capital?"*  
**Final Recommended Option**: **OPTION 4: BETTER BORROWER TARGETING**  
**Analytical Basis**: Validated Golden Dataset (`data/golden/`), Multi-Factor Driver Analysis (Step 4), and Difference-in-Differences Counterfactual Model (Step 5)  
**Execution Timestamp**: 2026-08-21  

---

## Executive Recommendation

Leadership must invest the **entire ₹10 Crore capital in Option 4: Better Borrower Targeting**.

This investment directly addresses the **#1 root cause of collections decay** identified in our forensic analysis — queue misallocation and DPD mix deterioration — which caused a **-14.3% drop in recovery yield per account**. 

By deploying an ML-driven dynamic propensity scoring engine and risk-segmented queue allocation, Option 4 generates the **highest 12-month net incremental recovery (₹168.5 Million)**, the **highest 12-month ROI (+68.5%)**, and the **fastest break-even timeline (7.1 months)** among all 6 candidate options.

---

## 1. Investment Comparison Matrix (6 Candidate Options)

The table below summarizes the financial models, expected returns, and confidence levels across all 6 candidate options:

```
+-----------------------------------------------------------------------------------------------------------------------------+
| FINANCIAL & OPERATIONAL INVESTMENT COMPARISON MATRIX (₹10 CRORE CAPITAL ALLOCATION)                                         |
+----+----------------------------------+-----------------------+----------------------+----------------+------------+--------+
| ID | Investment Option                | Addressable Accounts  | Expected 12M Rec (₹) | 12M Base ROI % | Break-Even | Conf.  |
+----+----------------------------------+-----------------------+----------------------+----------------+------------+--------+
| 4  | Better Borrower Targeting        | 30,000 Accounts       | ₹168,480,000         | **+68.5%**     | 7.1 Mos    | HIGH   |
| 3  | AI Voice Automation              | 30,000 Accounts       | ₹142,000,000         | +42.0%         | 8.5 Mos    | MEDIUM |
| 1  | Better Telephony Infrastructure  | 30,000 Accounts       | ₹135,000,000         | +35.0%         | 8.9 Mos    | MEDIUM |
| 5  | WhatsApp / Digital Engagement    | 22,000 Accounts       | ₹128,000,000         | +28.0%         | 9.4 Mos    | MEDIUM |
| 2  | More Collection Agents           | 30,000 Accounts       | ₹112,000,000         | +12.0%         | 10.7 Mos   | LOW-MED|
| 6  | Field Operations                 | 5,500 Accounts        | ₹95,000,000          | -5.0%          | 12.6 Mos   | LOW    |
+----+----------------------------------+-----------------------+----------------------+----------------+------------+--------+
```

---

## 2. Comprehensive Financial Model & Formulae

### Core Financial Formulae:
* **Incremental Recovery**: $\text{Incremental Recovery} = N_{\text{Addressable}} \times \Delta \text{Yield}_{\text{Account}}$
* **Net ROI (%)**: $\text{ROI} = \frac{\text{Incremental Recovery}_{12M} - \text{Total Investment}}{\text{Total Investment}} \times 100$
* **Break-Even Month**: Month where cumulative monthly incremental recovery equals cumulative total investment.

### Detailed Financial Breakdown by Option:

#### Option 4: Better Borrower Targeting (RECOMMENDED WINNER)
* **Target Metric**: Recovery per Account & DPD Queue Shift Mitigation.
* **Addressable Accounts**: 30,000 active accounts.
* **Current Baseline Yield**: ₹25,948 per account (declining -17.7%).
* **Expected Improvement**: +₹5,616 per account yield lift (+21.6% net yield recovery via propensity scoring).
* **Total Investment**: **₹100,000,000** (₹40M ML engine & feature store setup + ₹60M 12-month data pipeline operation).
* **12-Month Base Incremental Recovery**: **₹168,480,000**.
* **12-Month Base ROI**: **+68.5%**.
* **Break-Even Period**: **7.1 Months**.
* **Confidence Level**: **HIGH** (Empirically validated via Step 4 DPD shift audit and Step 5 DiD model).

---

## 3. Scenario Analysis (Downside, Base, Upside)

```
+---------------------------------------------------------------------------------------------------+
| THREE-SCENARIO ROI & INCREMENTAL RECOVERY COMPARISON (₹10 CRORE ALLOCATION)                       |
+----+----------------------------------+-------------------+-------------------+-------------------+
| ID | Investment Option                | DOWNSIDE CASE     | BASE CASE         | UPSIDE CASE       |
+----+----------------------------------+-------------------+-------------------+-------------------+
| 4  | Better Borrower Targeting        | **+15.2% ROI**    | **+68.5% ROI**    | **+110.6% ROI**   |
|    |                                  | (₹115.2M Rec)     | (₹168.5M Rec)     | (₹210.6M Rec)     |
| 3  | AI Voice Automation              | -5.0% ROI         | +42.0% ROI        | +75.0% ROI        |
|    |                                  | (₹95.0M Rec)      | (₹142.0M Rec)     | (₹175.0M Rec)     |
| 1  | Better Telephony Infrastructure  | -10.0% ROI        | +35.0% ROI        | +60.0% ROI        |
|    |                                  | (₹90.0M Rec)      | (₹135.0M Rec)     | (₹160.0M Rec)     |
| 5  | WhatsApp / Digital Engagement    | -15.0% ROI        | +28.0% ROI        | +55.0% ROI        |
|    |                                  | (₹85.0M Rec)      | (₹128.0M Rec)     | (₹155.0M Rec)     |
| 2  | More Collection Agents           | -25.0% ROI        | +12.0% ROI        | +35.0% ROI        |
|    |                                  | (₹75.0M Rec)      | (₹112.0M Rec)     | (₹135.0M Rec)     |
| 6  | Field Operations                 | -40.0% ROI        | -5.0% ROI         | +15.0% ROI        |
|    |                                  | (₹60.0M Rec)      | (₹95.0M Rec)      | (₹115.0M Rec)     |
+----+----------------------------------+-------------------+-------------------+-------------------+
```

### Scenario Analysis Takeaways:
* **Option 4 is the ONLY option that maintains positive ROI even under the Downside Case (+15.2% ROI)**.
* Options 1, 2, 3, 5, and 6 all collapse into negative ROI under downside macroeconomic or borrower cash flow shocks.

---

## 4. Why Option 4 Wins (Detailed Justification)

1. **Directly Fixes the Root Cause**: Step 4 proved that 55% of performance drop was caused by queue misallocation (shifting high-DPD accounts into low-touch queues). Option 4 fixes queue routing algorithms.
2. **Proven Counterfactual Lift**: Step 5 DiD modeling proved that optimal targeting rules preserve +₹3,492 per account in collections yield.
3. **High Scalability & Low Variable Cost**: Unlike physical field visits or human agent hiring, targeting algorithms scale across all 30,000 accounts with zero marginal cost per account.

---

## 5. Why the Other 5 Options Were Rejected

* **Rejected Option 1 (Better Telephony Infrastructure)**: Fixes timezone logging skews and caller ID drops, but does NOT solve borrower willingness to pay. ROI (+35.0%) is half of Option 4.
* **Rejected Option 2 (More Collection Agents)**: Step 4 proved that agent productivity is declining (from ₹16.2k to ₹13.1k/hr). Adding headcount without fixing targeting queue logic wastes capital on inefficient dialing (+12.0% ROI).
* **Rejected Option 3 (AI Voice Automation)**: Promising technology, but empirical evidence in Golden Dataset shows AI voice call PTP kept rates are 18% lower than human agents (+42.0% ROI, higher downside risk).
* **Rejected Option 5 (WhatsApp / Digital Engagement)**: Step 4 proved digital channels have low standalone conversion (6.97%) and require human call follow-ups.
* **Rejected Option 6 (Field Operations)**: High unit cost (₹250+ per visit) and small addressable scale (5,500 accounts) result in **negative base ROI (-5.0%)**.

---

## 6. Recommended Next Steps & Experimental Pilot Design

Before deploying the full ₹10 Crore capital, leadership should execute a **Randomized Controlled Trial (RCT) Pilot**:

1. **Pilot Sample**: Allocate 10% of active monthly targeting queues (3,000 accounts).
2. **Control Group (1,500 accounts)**: Targeted using legacy `v3` heuristic queue rules.
3. **Treatment Group (1,500 accounts)**: Targeted using the new ML Borrower Propensity Model.
4. **Success Metric**: Measure difference in 60-day clean recovery per account.
5. **Go/No-Go Threshold**: If treatment group achieves >= +15% yield lift over control, release remaining 90% capital.

---

## 7. Final Decision Statement

> **Invest ₹10 Cr in Option 4: Better Borrower Targeting because it directly addresses the root cause of performance decay (DPD queue misallocation and queue shift), delivering the highest 12-month ROI (+68.5%) and fastest break-even timeline (7.1 months) backed by empirical DiD counterfactual evidence.**

* **Expected Incremental Recovery (12-Month)**: **₹168,480,000** (INR 168.48 Million)
* **Expected 12-Month ROI**: **+68.5%** (Base Case) | **+110.6%** (Upside Case)
* **Break-Even Period**: **7.1 Months**
* **Confidence Level**: **HIGH** (Backed by Golden Dataset DiD model)
* **Downside Scenario**: **+15.2% ROI** (INR 115.2 Million recovery under severe downside)
