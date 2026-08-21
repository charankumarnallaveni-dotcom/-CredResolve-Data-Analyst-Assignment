# Production Analytics Architecture & Pipeline Specification

**Target System**: Executive Production Analytics & Decision Dashboard  
**Data Pipeline Architecture**: `RAW ➔ STAGING ➔ DATA QUALITY ➔ GOLDEN ➔ FEATURE/METRIC ➔ DASHBOARD`  
**Execution Environment**: Python 3.12, SQL Engine, Streamlit / Plotly Dashboard Framework  

---

## 1. End-to-End Pipeline Architecture Diagram

```
                                  [ RAW DATA SOURCES ]
               18 Ingestion CSV Files (Telephony, Gateway Webhooks, CRM, Field Logs)
                                           │
                                           ▼
                                   [ INGESTION LAYER ]
                        • Daily Batch CSV & Webhook Ingestion Engine
                        • Immutable Raw Data Lake Storage (data/raw/)
                                           │
                                           ▼
                                   [ STAGING LAYER ]
                             (sql/01_staging.sql & ETL)
                        • Schema Enforcement & String Trimming
                        • Timezone Standardization: Asia/Dubai & UTC ➔ Asia/Kolkata (IST)
                        • Strict Data Type Casting & DateTime Parsing
                                           │
                                           ▼
                             [ DATA QUALITY AUDIT LAYER ]
                        (data/clean/data_quality_actions.csv)
                        • 46,253 Automated DQ Audit Actions Logged
                        • Rejection of 10,150 Non-SUCCESS & Duplicate Payment Rows
                        • Deduplication of Calls, WhatsApp & Borrower Masters
                        • Synthetic Agent Entity Resolution (30k IDs ➔ 10 Profiles)
                        • Foreign Key Placeholder Resolution (2,913 Orphans)
                                           │
                                           ▼
                                [ GOLDEN DATASET LAYER ]
                              (data/golden/ Data Marts)
                        • Dimension Tables: dim_borrowers, dim_accounts, dim_agents, dim_campaigns
                        • Fact Tables: fct_payments, fct_calls, fct_whatsapp_events, 
                          fct_sms_events, fct_field_visits, fct_promises_to_pay, fct_daily_targeting
                                           │
                                           ▼
                             [ FEATURE & METRIC LAYER ]
                       (14-Day Multi-Touch Payment Attribution)
                        • Account Rolling Touchpoint Histories
                        • Multi-Touch Attribution Engine (LAST_TOUCH_14D_WINDOW)
                        • Aggregated KPI Data Marts (monthly_performance.csv)
                                           │
                                           ▼
                         [ EXECUTIVE DECISION DASHBOARD ]
                         (Streamlit / Plotly Web Interface)
                        • 60-Second CEO Decision Interface
                        • Interactive Filters, Recovery Truth Bridge, Driver Scorecard
                        • ₹10 Crore Capital Allocation Financial Model
```

---

## 2. Production Pipeline Components & Specifications

### A. Ingestion & Refresh Schedule
* **Refresh Cadence**: Daily Incremental Batch at 02:00 AM IST.
* **Late-Arriving Events**: Handles up to 30-day late-arriving payments and status updates via idempotency keys (`payment_reference` hashing).

### B. Data Quality Checks & Automated Testing
Before publishing to the Golden Layer, the automated test suite (`tests/test_data_quality.py`) validates 6 strict data quality contracts:
1. **Primary Key Uniqueness**: `dim_accounts.account_id`, `fct_calls.call_id`, `dim_agents.canonical_agent_id`.
2. **Status Integrity**: `fct_payments.payment_status == 'SUCCESS'` strictly enforced.
3. **Deduplication**: `fct_payments.payment_reference` duplicate count must equal 0.
4. **Positive Capital**: `fct_payments.amount > 0`.
5. **Referential Integrity**: 100% of `fct_payments.account_id` keys exist in `dim_accounts`.
6. **No Duplicate Event IDs**: 0 duplicate IDs in `fct_calls`.

### C. Failure Handling & Alerting
* **Quarantine Pipeline**: Records failing DQ checks are appended to `data/clean/data_quality_actions.csv` with status `'REJECTED'` or `'FLAGGED'` and an explicit failure reason string.
* **Alerting SLA**: If raw payment inflation exceeds 10% on any daily batch, an automated Slack/Email alert is triggered to analytics engineering.

### D. Data Lineage & Traceability
Every row in the Golden Dataset carries an audit lineage trail:
* `source_table`: Raw origin table name.
* `event_at_ist`: Standardized IST timestamp.
* `data_quality_action_id`: Foreign key reference to `data_quality_actions.csv`.
