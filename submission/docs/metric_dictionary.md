# Production Analytics Metric Dictionary

**System Scope**: Collections Analytics & Recovery Engine  
**Data Layer**: Golden Dataset (`data/golden/`)  
**Document Version**: 2.0 (Post-Audit Clean Baseline)  

---

## 1. Top Executive KPIs

### 1. Independent Recovery Rate (%)
* **Formula**: `(Total Deduplicated SUCCESS Recovery Amount in Month / Total Outstanding Principal Balance of Targeted Accounts) * 100`
* **Numerator**: `SUM(amount)` from `fct_payments` where `payment_status = 'SUCCESS'` and `payment_reference` is deduplicated.
* **Denominator**: `SUM(outstanding_amount)` from `dim_accounts` for accounts targeted in `fct_daily_targeting` during the month.
* **Source Table**: `fct_payments`, `dim_accounts`, `fct_daily_targeting`
* **Inclusion Rules**: Successful settlements only (`payment_status = 'SUCCESS'`).
* **Exclusion Rules**: Excludes FAILED, PENDING, REVERSED transactions and duplicate reference retries.
* **Business Meaning**: True percentage of targeted outstanding debt capital actually collected in bank accounts.

---

### 2. Reported Recovery Rate (%)
* **Formula**: `(Total Gross Raw Recovery Amount in Month / Total Outstanding Principal Balance of Targeted Accounts) * 100`
* **Numerator**: `SUM(amount)` from raw `payments.csv` across all payment rows.
* **Denominator**: `SUM(outstanding_amount)` from `dim_accounts` for accounts targeted in raw `daily_targeting.csv`.
* **Source Table**: Raw `payments.csv`, `accounts.csv`, `daily_targeting.csv`
* **Inclusion Rules**: All uncleaned raw payment rows.
* **Exclusion Rules**: None (unfiltered raw view).
* **Business Meaning**: Naïve legacy business reporting metric containing uncollected retries and failed payment attempts.

---

### 3. Difference vs Reported (%)
* **Formula**: `((Reported Gross Recovery Amount - Independent Clean Recovery Amount) / Independent Clean Recovery Amount) * 100`
* **Numerator**: `Reported Gross Recovery Amount - Independent Clean Recovery Amount`
* **Denominator**: `Independent Clean Recovery Amount`
* **Source Table**: `reports/recovery_truth_bridge.csv`
* **Inclusion Rules**: Full 12-month aggregated comparison.
* **Exclusion Rules**: None.
* **Business Meaning**: Quantifies the exact percentage by which legacy gross reporting inflates actual bank collections.

---

### 4. Recovery Amount (INR)
* **Formula**: `SUM(amount)`
* **Numerator**: Sum of clean settlement payments in INR.
* **Denominator**: N/A (Currency scalar)
* **Source Table**: `fct_payments.csv`
* **Inclusion Rules**: Deduplicated SUCCESS payments only.
* **Exclusion Rules**: FAILED, PENDING, REVERSED, and duplicate payment references.
* **Business Meaning**: Net financial capital recovered and verified in bank accounts.

---

### 5. Recovery per Account (INR)
* **Formula**: `Total Deduplicated SUCCESS Recovery Amount in Month / Count of Unique Accounts Targeted in Month`
* **Numerator**: `SUM(amount)` from `fct_payments`
* **Denominator**: `COUNT(DISTINCT account_id)` from `fct_daily_targeting`
* **Source Table**: `fct_payments.csv`, `fct_daily_targeting.csv`
* **Inclusion Rules**: Active accounts targeted in daily queues.
* **Exclusion Rules**: Accounts un-targeted during the month.
* **Business Meaning**: Average collection revenue generated per targeted delinquent account.

---

### 6. PTP Kept Rate (%)
* **Formula**: `(Total Kept Promised Amount in Month / Total Promised Amount in Month) * 100`
* **Numerator**: `SUM(promised_amount)` from `fct_promises_to_pay` where `status = 'KEPT'`
* **Denominator**: `SUM(promised_amount)` from `fct_promises_to_pay` across all PTP records in month
* **Source Table**: `fct_promises_to_pay.csv`
* **Inclusion Rules**: Verified PTP commitments.
* **Exclusion Rules**: Cancelled or unverified commitments.
* **Business Meaning**: Operational effectiveness of agent promises-to-pay converting into real cash collections.

---

## 2. Operational & Channel Metrics

### 7. Contact Rate (%)
* **Formula**: `(Count of Unique Accounts with >= 1 Answered Call in Month / Count of Unique Targeted Accounts) * 100`
* **Numerator**: `COUNT(DISTINCT account_id)` from `fct_calls` where `call_status = 'ANSWERED'`
* **Denominator**: `COUNT(DISTINCT account_id)` from `fct_daily_targeting`
* **Source Table**: `fct_calls.csv`, `fct_daily_targeting.csv`
* **Inclusion Rules**: Connected/Answered human or IVR voice calls.
* **Exclusion Rules**: Unanswered, Busy, Voicemail, or Failed call attempts.
* **Business Meaning**: Coverage efficiency of telephony operations in reaching delinquent borrowers.

---

### 8. RPC Rate (Right Party Contact Rate, %)
* **Formula**: `(Count of Unique Accounts with >= 1 RPC Disposition / Count of Unique Contacted Accounts) * 100`
* **Numerator**: `COUNT(DISTINCT account_id)` from `fct_call_dispositions` with codes `PTP`, `CALLBACK`, `PAID`, `DISPUTE`
* **Denominator**: `COUNT(DISTINCT account_id)` from `fct_calls` with `call_status = 'ANSWERED'`
* **Source Table**: `fct_call_dispositions.csv`, `fct_calls.csv`
* **Inclusion Rules**: Verified contact with the primary account borrower.
* **Exclusion Rules**: Wrong number, third-party contact, or refusal before identification.
* **Business Meaning**: Quality of contactability — proportion of reached calls that result in meaningful dialogue.

---

### 9. Cost per ₹ Recovered (INR)
* **Formula**: `Total Operational Work & Channel Costs / Total Deduplicated SUCCESS Recovery Amount`
* **Numerator**: `(Agent Session Hours * ₹250) + (Voice Call Volume * ₹1.50) + (WhatsApp Volume * ₹0.50)`
* **Denominator**: `SUM(amount)` from `fct_payments`
* **Source Table**: `fct_payments`, `stg_agent_sessions`, `fct_calls`, `fct_whatsapp_events`
* **Inclusion Rules**: Direct variable operational costs.
* **Exclusion Rules**: Fixed corporate overhead / capital expenditure.
* **Business Meaning**: Operational unit cost required to collect ₹1.00 of delinquent debt capital.
