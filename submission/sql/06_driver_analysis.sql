-- SQL 06: DRIVER ANALYSIS & SEGMENT PERFORMANCE
-- Analyzes recovery rates and performance across DPD, Channels, Agents, and Risk Segments

-- 1. Recovery Performance by DPD Bucket
CREATE OR REPLACE TABLE driver_dpd_performance AS
SELECT 
    CASE 
        WHEN a.dpd <= 30 THEN '1-30 DPD'
        WHEN a.dpd <= 60 THEN '31-60 DPD'
        WHEN a.dpd <= 90 THEN '61-90 DPD'
        ELSE '90+ DPD'
    END AS dpd_bucket,
    COUNT(DISTINCT a.account_id) AS total_accounts,
    SUM(a.outstanding_amount) AS total_outstanding_inr,
    COUNT(DISTINCT p.payment_id) AS total_payments,
    SUM(COALESCE(p.amount, 0)) AS clean_recovery_amount_inr,
    ROUND(SUM(COALESCE(p.amount, 0)) / SUM(a.outstanding_amount) * 100, 2) AS recovery_rate_pct,
    ROUND(SUM(COALESCE(p.amount, 0)) / COUNT(DISTINCT a.account_id), 2) AS recovery_per_account_inr
FROM dim_accounts a
LEFT JOIN fct_payments p ON a.account_id = p.account_id
GROUP BY 1
ORDER BY dpd_bucket;

-- 2. Recovery Performance by Attributed Channel
CREATE OR REPLACE TABLE driver_channel_performance AS
SELECT 
    attributed_channel,
    attribution_type,
    COUNT(DISTINCT payment_id) AS payment_count,
    COUNT(DISTINCT account_id) AS paying_accounts,
    SUM(amount) AS clean_recovery_amount_inr,
    ROUND(SUM(amount) / (SELECT SUM(amount) FROM fct_payments) * 100, 2) AS recovery_share_pct
FROM fct_payments
GROUP BY 1, 2
ORDER BY clean_recovery_amount_inr DESC;

-- 3. Recovery Performance by Risk Segment & Loan Type
CREATE OR REPLACE TABLE driver_risk_segment_performance AS
SELECT 
    loan_type,
    risk_segment,
    COUNT(DISTINCT a.account_id) AS account_count,
    SUM(a.outstanding_amount) AS total_outstanding_inr,
    SUM(COALESCE(p.amount, 0)) AS clean_recovery_amount_inr,
    ROUND(SUM(COALESCE(p.amount, 0)) / SUM(a.outstanding_amount) * 100, 2) AS recovery_rate_pct
FROM dim_accounts a
LEFT JOIN fct_payments p ON a.account_id = p.account_id
GROUP BY 1, 2
ORDER BY clean_recovery_amount_inr DESC;
