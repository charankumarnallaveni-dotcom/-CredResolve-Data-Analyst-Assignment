# Production Analytics Reproducibility Guide

**System Target**: Collections Analytics Platform & Audit Engine  
**Execution Environment**: Windows / Linux / macOS (Python 3.12, SQL Engine)  

---

## 1. Environment Setup & Dependency Installation

Clone or navigate to the repository root directory:

```bash
cd c:\Users\HP\Downloads\Assignment-1
```

Install Python dependencies via `requirements.txt`:

```bash
pip install -r requirements.txt
```

---

## 2. Dataset Extraction & Preparation

Ensure the raw zip file `collections_30k_dataset.zip` is located in the root directory. Extract it to `raw_data/`:

```python
import zipfile, os
os.makedirs("raw_data", exist_ok=True)
with zipfile.ZipFile("collections_30k_dataset.zip", "r") as z:
    z.extractall("raw_data")
```

---

## 3. Data Pipeline & Golden Dataset Generation

Execute the master pipeline script (`scratch/build_pipeline_v5.py`):

```bash
python scratch/build_pipeline_v5.py
```

### What this script executes:
1. Copies raw files to `data/raw/`.
2. Standardizes schemas, data types, and timezones (Asia/Dubai & UTC ➔ IST) in `data/staging/`.
3. Runs deduplication and logs 46,253 audit actions to `data/clean/data_quality_actions.csv`.
4. Executes 14-day multi-touch payment attribution.
5. Exports analytical data marts to `data/golden/` (`dim_borrowers`, `dim_accounts`, `dim_agents`, `dim_campaigns`, `fct_payments`, `fct_calls`, `fct_daily_targeting`).
6. Runs 6 automated data quality tests in `tests/test_data_quality.py`.

---

## 4. Running Data Quality Tests

Execute pytest on the automated DQ test suite:

```bash
pytest tests/test_data_quality.py
```

Expected result: **6 PASSED (100% Pass Rate)**.

---

## 5. Executing Analysis & Models

Run the claim validation, driver analysis, counterfactual model, and investment model scripts:

```bash
# Step 3: Claim Validation & Monthly Performance
python scratch/analyze_11pct_claim.py

# Step 4: Multi-Factor Driver Analysis
python scratch/analyze_drivers.py

# Step 5: Difference-in-Differences Counterfactual Model
python scratch/analyze_counterfactual.py

# Step 6: ₹10 Crore Investment Financial Model
python scratch/analyze_investment.py
```

---

## 6. SQL Repository Execution

The production SQL scripts in `sql/` can be executed against any standard SQL database (PostgreSQL, DuckDB, Snowflake, BigQuery, SQLite):

```bash
sql/01_staging.sql
sql/02_clean_dedup_audit.sql
sql/03_golden_layer.sql
sql/04_payment_attribution.sql
sql/05_claim_validation.sql
sql/06_driver_analysis.sql
sql/07_counterfactual.sql
sql/08_investment_analysis.sql
```

---

## 7. Launching the Interactive Executive Dashboard

Launch the Streamlit Executive Decision Dashboard:

```bash
python -m streamlit run dashboard/app.py
```

Open your browser at `http://localhost:8501`.

---

## 8. Expected Outputs Verification

| Deliverable Path | Expected Output File | Verification Check |
| :--- | :--- | :--- |
| `data/golden/monthly_performance.csv` | Monthly KPI Table | 8 rows (Jan–Aug 2026), 12 columns |
| `reports/recovery_truth_bridge.csv` | Financial Reconciliation | Reported ₹1.917B ➔ Clean ₹1.150B |
| `data/golden/driver_scorecard.csv` | Master Driver Scorecard | 6 ranked operational drivers |
| `data/golden/counterfactual_results.csv` | DiD Model Results | DiD Estimator = +₹3,492.80/account |
| `data/golden/investment_comparison.csv` | ₹10 Cr Financial Model | Winner = Option 4 (+68.5% ROI) |
| `tests/test_results.csv` | Test Suite Output | 6/6 Tests PASS |
