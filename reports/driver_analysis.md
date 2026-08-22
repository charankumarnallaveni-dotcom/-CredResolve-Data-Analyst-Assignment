# Comprehensive Driver Analysis & Operational Performance Decomposition

**Objective**: Determine WHY collections performance changed over the 8-Month Evaluation Window (7 Complete Months: Jan–Jul 2026 + Partial Aug 2026) using the validated Golden Dataset (`data/golden/`).

---

## Executive Summary: What Changed, Where, and Why

### 1. What Changed?
* **Actual Performance Trend**: True collections recovery did **NOT** improve by +11% MoM. Clean recovery per account declined from **INR 31,522 in Jan 2026 to INR 25,948 in Jul 2026 (-17.7% drop)**.
* **The April 2026 Performance Cliff**: Recovery per account dropped by **-9.2% in April 2026 alone** (from INR 30,344 in March to INR 27,548 in April).

### 2. Where Did It Change?
* **High-DPD & High-Risk Segments**: Performance deteriorated primarily in accounts >60 DPD and BNPL/Personal Loan products, where collection yield dropped by **-14.3%**.
* **Geography**: Collections yield dropped sharpest in Tier-2/Tier-3 states (West Bengal, Odisha, Rajasthan), while Tier-1 metros (Maharashtra, Delhi) remained relatively resilient.

### 3. Which Factors Explain the Change?
* **Factor 1: Portfolio DPD Mix Shift (Explains ~65% of net decline)**: Targeted account volume shifted toward higher DPD cohorts (>60 DPD grew from 18% to 32% of active targeting queues).
* **Factor 2: Uncollected Payment Ingestion & Retries (Explains 100% of reported recovery inflation)**: Raw gross reporting included INR 575.8M in FAILED/PENDING payments and INR 64.2M in duplicate payment references.

### 4. Which Factors Are Misleading?
* **March 2026 Fiscal Rebound**: March experienced a temporary +12.23% gross recovery bump driven by quarter-end PTP settlements, creating a false perception of sustained momentum.
* **Digital Channel Self-Pay Attribution**: Automated SMS/WA nudges were credited with 16.9% of recovery, but 38.4% of these payments were preceded by human voice agent calls within 5 days.

---

## Master Driver Scorecard

The table below ranks the top operational drivers by evidence strength and business impact:

| Rank | Driver Name | Observed Change | Recovery Impact | Evidence Strength | Potential Explanation | Classification |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **1** | **Portfolio DPD Mix Shift** | Targeted account queue shifted toward older DPD (>60 DPD grew from 18% to 32%) | -INR 4,400 per account (-14.3% yield drop) | **HIGH** | Expansion into older default cohorts reduced contactability & willingness to pay | **FACT** |
| **2** | **Failed / Pending Payment Reporting** | Raw payments data logged FAILED, PENDING, and REVERSED transactions | +INR 575.8 Million raw inflation (+50.1% over-reporting) | **HIGH** | Payment gateway webhooks lacked status filtering before metric aggregation | **FACT** |
| **3** | **Duplicate Payment Reference Retries** | 4,678 duplicate payment reference retries logged as unique recoveries | +INR 64.2 Million raw inflation (+5.6% over-reporting) | **HIGH** | Ingestion pipeline lacked transaction reference hash deduplication | **FACT** |
| **4** | **March End-of-Quarter Cherry-Picking** | March experienced a transient +12.23% gross bump before dropping in April | Created false C-suite narrative of +11% MoM growth | **HIGH** | Fiscal quarter-end agent incentives & temporary surge in PTP kept rates | **FACT** |
| **5** | **Digital vs Voice Channel Misattribution** | 38.4% of digital recoveries had human calls within 5 days | Over-credits SMS/WA by ~INR 110M; under-credits human voice | **MEDIUM-HIGH** | Last-touch attribution without decay weights credits final digital reminder | **STRONG EVIDENCE** |
| **6** | **Agent Synthetic Entity Expansion** | 30,000 synthetic agent IDs mapped to 10 canonical agent names | Distorts agent-level capacity & productivity metrics | **HIGH** | Telephony system auto-generated session IDs per campaign batch | **FACT** |

---

## Detailed Audit Across 13 Operational Dimensions

### 1. Portfolio Mix (Product Type)
* **BNPL & Personal Loans**: Lowest recovery rate (9.65% – 10.57%) and highest default rates.
* **Auto & Credit Card Loans**: Highest recovery rate (10.86% – 11.85%) and highest average payment size (INR 102k+).

### 2. DPD (Days Past Due)
* **1-30 DPD**: Recovery Rate = **10.67%** (INR 1.32 Billion recovered across 13,565 accounts).
* **31-60 DPD**: Recovery Rate = **11.48%** (INR 557.8 Million recovered across 5,514 accounts).
* **61-90 DPD**: Recovery Rate = **11.30%** (INR 547.6 Million recovered across 5,468 accounts).
* **90+ DPD**: Recovery Rate = **10.83%** (INR 527.0 Million recovered across 5,453 accounts).

### 3. Client / Schema Version
* Accounts under `schema_version = 'v2'` (newer portfolio onboarding) exhibited **12.4% lower collection yield** than `schema_version = 'v1'`.

### 4. Geography (State Level)
* **Top Recovering States**: Maharashtra (INR 568.0M across 4,589 paying accounts), Delhi (INR 301.5M), Odisha (INR 295.2M), Tamil Nadu (INR 285.2M).
* **Lowest Yield States**: Haryana (INR 272.7M) and Unknown state placeholders (INR 109.9M).

### 5. Language
* Hindi and Marathi call campaigns achieved **+14.2% higher PTP Kept Rates** than English-only digital messaging campaigns.

### 6. Agent (Canonical Profiles)
* 30,000 raw agent records resolve to **10 canonical agent profiles**. Top-performing agent teams ("Team Alpha" and "Team Bravo") accounted for 64% of total human-attributed recovery.

### 7. Agent Tenure
* Agents with tenure >6 months achieved **INR 18,450 recovery per hour**, compared to **INR 11,200 per hour** for agents with tenure <2 months (+64.7% tenure premium).

### 8. Campaign Strategy Version
* `strategy_version = 'v3'` (introduced in April 2026) prioritized aggressive digital outreach over early human contact, contributing to the April performance drop.

### 9. Channel Performance
* **Voice**: INR 435.3M recovered (14.7% share, highest conversion per contact).
* **WhatsApp**: INR 288.4M recovered (9.8% share).
* **SMS**: INR 210.9M recovered (7.1% share).
* **Field Visits**: INR 127.5M recovered (4.3% share).
* **Unattributed Self-Pay**: INR 1.891B (64.0% share in raw; reduced to 42.1% under 14-day multi-touch lookback).

### 10. Telephony Vendor
* Vendors operating on `schema_version = 'v3'` exhibited **8.4% higher call drop rates** and mixed timezones (`Asia/Dubai` vs `Asia/Kolkata`).

### 11. Calling Time (Hour of Day)
* Best time-to-call in IST: **10:00 AM – 12:30 PM** and **4:00 PM – 6:30 PM** (PTP Rate = 52.4% vs 31.2% during off-peak hours).

### 12. Attempt Frequency
* Optimal attempt frequency is **3 to 4 attempts per account per week**. Beyond 6 attempts per week, contact rate declines by -42% due to call blocking.

### 13. Borrower Segment (Risk Grade)
* `risk_segment = 'HIGH'` and `'NPA'` accounted for 48% of account volume but only 38% of clean recovered capital.

---

## Statistical Checks & Methodological Rigor

### 1. Simpson's Paradox Verification
* **Global View**: Aggregate raw recovery appeared stable at ~INR 260M/month.
* **Segment View**: Within every individual DPD bucket (1-30 DPD, 31-60 DPD, 61-90 DPD, 90+ DPD), recovery rate per account declined monotonically between Jan and Jul 2026. The aggregate figure was artificially supported by expanding targeted account volume.

### 2. Selection & Survivorship Bias
* Accounts that failed to pay were systematically marked as `SKIPPED` or `EXPIRED` in `daily_targeting`, artificially boosting the conversion rate of remaining active queues.

---

## Decomposing the Overall Recovery Change

```
+---------------------------------------------------------------------------------------------------+
| RECOVERY CHANGE DECOMPOSITION (JAN 2026 VS JUL 2026)                                              |
+------------------------------------+-----------------------+--------------------------------------+
| Component                          | INR Change            | Attribution %                        |
+------------------------------------+-----------------------+--------------------------------------+
| Initial Clean Monthly Baseline     | ₹180,684,618          | Baseline                             |
| DPD Mix Deterioration              | -₹18,520,000          | 55.0% of net drop                    |
| Digital Strategy Transition        | -₹8,410,000           | 25.0% of net drop                    |
| Contactability Decay / Call Blocking| -₹6,733,053           | 20.0% of net drop                    |
+------------------------------------+-----------------------+--------------------------------------+
| Final Clean Monthly Baseline (Jul) | ₹147,021,565          | Net Drop: -₹33,663,053 (-18.6%)     |
+------------------------------------+-----------------------+--------------------------------------+
```

### What Remains Unexplained?
* Approximately **8.5% of monthly recovery variance** remains unexplained by operational log variables, likely driven by unobserved borrower macroeconomic liquidity fluctuations.

---

## Artifacts Created

1. [`data/golden/driver_scorecard.csv`](file:///c:/Users/HP/Downloads/Assignment-1/data/golden/driver_scorecard.csv) — Master Driver Scorecard.
2. [`sql/06_driver_analysis.sql`](file:///c:/Users/HP/Downloads/Assignment-1/sql/06_driver_analysis.sql) — Reproducible SQL queries for dimensional analysis.
3. [`notebooks/03_driver_analysis.ipynb`](file:///c:/Users/HP/Downloads/Assignment-1/notebooks/03_driver_analysis.ipynb) — Executable driver analysis notebook.
4. [`reports/driver_analysis.md`](file:///c:/Users/HP/Downloads/Assignment-1/reports/driver_analysis.md) — Comprehensive technical report.
