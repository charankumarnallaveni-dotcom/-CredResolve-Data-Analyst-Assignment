# Data Analyst Assessment: Collections Audit, Data Forensics & Production Analytics Platform

An enterprise-grade data audit, analytics engineering pipeline, statistical investigation, and executive decision system built on 12 months of collections data (30,000 accounts, 18 raw systems).

---

## 1. Project Objective & Core Business Questions

The business currently reports: **"Recovery has improved by 11% month-on-month."**  
The executive leadership team was skeptical. This repository contains the complete forensic investigation, data hygiene pipeline, statistical modeling, and capital allocation framework that answers four core questions:

1. **What happened?**: Reconstructed actual business performance over 12 months.
2. **Why did it happen?**: Identified operational drivers across 13 dimensions.
3. **Is the 11% improvement real?**: Independently tested the business claim against bank-settled collections data.
4. **Where to invest ₹10 Crore?**: Evaluated 6 investment options using financial models, scenario analysis, and counterfactual DiD estimation.

---

## 2. Key Findings & Executive Summary

* **11% Claim Refuted (FALSE NARRATIVE)**: Recovery is **NOT** compounding at +11% MoM. Month-on-month growth was negative in 4 out of 6 full months. The 11% figure represented a single cherry-picked month (March 2026 at +12.23% gross).
* **Operational Performance is Declining (-19.9% Net Drop)**: Verified clean recovery rate dropped from **9.01% in Jan 2026 to 7.22% in Jul 2026**, while clean recovery per account dropped from **₹31,522 to ₹25,948 (-17.7%)**.
* **Massive Over-Reporting Bias (+66.7% Inflation)**: Raw legacy reporting included **₹575.8 Million in FAILED/PENDING payment attempts** and **₹64.2 Million in duplicate payment reference retries**, inflating reported collections from **₹1.150 Billion (clean) to ₹1.917 Billion (raw)**.
* **April 2026 Performance Cliff**: Performance dropped sharply in April (-9.2% single-month yield drop) due to a **Portfolio DPD Mix Shift** (targeted accounts >60 DPD grew from 18% to 32% of active queues).

---

## 3. Final ₹10 Crore Investment Recommendation

> **RECOMMENDED OPTION**: **OPTION 4 — BETTER BORROWER TARGETING**

* **12-Month Net Incremental Recovery**: **₹168,480,000** (INR 168.48 Million)
* **12-Month Base ROI**: **+68.5%** (Base Case) | **+110.6%** (Upside Case)
* **Break-Even Period**: **7.1 Months**
* **Downside Scenario ROI**: **+15.2%** (Only candidate option with positive downside ROI)
* **Confidence Level**: **HIGH** (Empirically validated via Difference-in-Differences counterfactual model)

---

## 4. Final Project Folder Structure

```
Assignment-1/
│
├── data/                           # Production Data Layers
│   ├── raw/                        # Read-only copy of 18 raw CSV tables
│   ├── staging/                    # Standardized schemas & IST timezone normalized tables
│   ├── clean/                      # Deduplicated tables & data_quality_actions.csv audit log
│   └── golden/                     # Analytical Golden Dataset (dim_* and fct_* data marts)
│
├── sql/                            # Production SQL Repository (01 to 08)
│   ├── 01_staging.sql              # Timezone & schema standardization
│   ├── 02_clean_dedup_audit.sql    # Deduplication & quarantine logic
│   ├── 03_golden_layer.sql         # Dimension and fact table DDL
│   ├── 04_payment_attribution.sql  # 14-day multi-touch attribution
│   ├── 05_claim_validation.sql     # Claim testing & monthly performance
│   ├── 06_driver_analysis.sql      # Multi-factor dimensional audit
│   ├── 07_counterfactual.sql       # Difference-in-Differences model
│   └── 08_investment_analysis.sql  # ₹10 Cr financial model
│
├── notebooks/                      # Executable Python Notebooks (01 to 05)
│   ├── 01_data_forensics_audit.ipynb
│   ├── 02_claim_validation.ipynb
│   ├── 03_driver_analysis.ipynb
│   ├── 04_counterfactual.ipynb
│   └── 05_investment_model.ipynb
│
├── reports/                        # Deliverables & Technical Reports
│   ├── executive_memo.md           # 2-Page C-Suite Executive Memo
│   ├── golden_dataset_report.md    # Pipeline hygiene & DQ report
│   ├── 11_percent_claim.md         # Claim testing & truth bridge report
│   ├── driver_analysis.md          # Dimensional driver report
│   ├── counterfactual.md           # Targeting strategy DiD report
│   ├── investment_case.md          # ₹10 Cr capital allocation report
│   ├── final_results.md            # Verified final audit results summary
│   └── recovery_truth_bridge.csv   # Step-by-step financial reconciliation
│
├── dashboard/                      # Production C-Suite Dashboard
│   └── app.py                      # Interactive Streamlit Executive Interface (Port 8501)
│
├── docs/                           # Architecture & Governance Documentation
│   ├── metric_dictionary.md        # Formulae & definitions for all 9 KPIs
│   ├── architecture.md             # Data pipeline specification
│   ├── architecture.png            # High-resolution pipeline diagram
│   ├── reproducibility.md          # Step-by-step reproduction guide
│   └── assessment_checklist.md     # Assignment requirement mapping checklist
│
├── tests/                          # Automated Data Quality Test Suite
│   ├── test_data_quality.py        # PyTest suite (6 DQ contracts, 100% pass)
│   └── test_results.csv            # Automated test execution results
│
├── requirements.txt                # Python environment dependencies
└── README.md                       # Master Project README
```

---

## 5. Technology Stack

* **Language**: Python 3.12, ANSI SQL
* **Data Processing**: Pandas, NumPy, Bisect (vectorized attribution)
* **Visualization & Web App**: Streamlit 1.62, Plotly Express 6.9, Matplotlib 3.11
* **Testing & Quality Control**: PyTest 7.4

---

## 6. How to Reproduce the Analysis

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 2: Run Data Pipeline (RAW ➔ STAGING ➔ CLEAN ➔ GOLDEN)
```bash
python scratch/build_pipeline_v5.py
```

### Step 3: Run Automated Data Quality Tests
```bash
pytest tests/test_data_quality.py
```

### Step 4: Run Analysis & Modeling Scripts
```bash
python scratch/analyze_11pct_claim.py
python scratch/analyze_drivers.py
python scratch/analyze_counterfactual.py
python scratch/analyze_investment.py
```

### Step 5: Launch the Executive Dashboard
```bash
python -m streamlit run dashboard/app.py
```
Open browser at `http://localhost:8501`.

---

## 7. Metric Definitions & Data Quality Approach

All metric definitions are documented in [`docs/metric_dictionary.md`](file:///c:/Users/HP/Downloads/Assignment-1/docs/metric_dictionary.md).

### Core Data Quality Rules Applied:
* **Payment Settlement Integrity**: Excluded 7,620 non-SUCCESS rows (`FAILED`, `PENDING`, `REVERSED`).
* **Payment Reference Deduplication**: Removed 2,530 gateway retry duplicate references.
* **Timezone Standardization**: Converted `Asia/Dubai` (+1.5h) and `UTC` (+5.5h) to standard `Asia/Kolkata` (IST).
* **Agent Entity Consolidation**: Grouped 30,000 synthetic IDs into 10 canonical profiles.
* **Audit Trail**: Every modification logged to `data/clean/data_quality_actions.csv` (46,253 total actions).

---

## 8. Assumptions & Limitations

1. **Successful Payment Deduplication**: Payments sharing identical `payment_reference` strings represent gateway retries or ingestion duplicates.
2. **14-Day Lookback Window**: Multi-touch attribution assumes an interaction occurring >14 days prior to a payment had minimal causal impact.
3. **Macro-Economic Variables**: Unobserved macroeconomic borrower cash flow shifts could not be directly controlled for in operational logs.
