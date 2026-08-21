-- SQL 05: CLAIM VALIDATION & MONTHLY PERFORMANCE RECONSTRUCTION
-- Evaluates reported vs independent recovery and metrics month-by-month

WITH raw_monthly AS (
    SELECT 
        DATE_FORMAT(event_at, '%Y-%m') AS month_str,
        SUM(amount) AS raw_gross_recovery,
        SUM(CASE WHEN UPPER(payment_status) = 'SUCCESS' THEN amount ELSE 0 END) AS raw_success_recovery
    FROM raw_payments
    GROUP BY 1
),
clean_monthly AS (
    SELECT 
        DATE_FORMAT(event_at_ist, '%Y-%m') AS month_str,
        COUNT(DISTINCT payment_id) AS clean_payment_count,
        COUNT(DISTINCT account_id) AS clean_paying_accounts,
        SUM(amount) AS clean_recovery_amount
    FROM fct_payments
    GROUP BY 1
),
targeting_monthly AS (
    SELECT 
        DATE_FORMAT(target_date, '%Y-%m') AS month_str,
        COUNT(DISTINCT account_id) AS targeted_accounts
    FROM fct_daily_targeting
    GROUP BY 1
)
SELECT 
    t.month_str AS month,
    t.targeted_accounts,
    r.raw_gross_recovery,
    r.raw_success_recovery,
    c.clean_recovery_amount,
    (r.raw_gross_recovery - c.clean_recovery_amount) AS total_inflation_amount,
    ROUND(((r.raw_gross_recovery - c.clean_recovery_amount) / c.clean_recovery_amount * 100), 2) AS inflation_percentage,
    ROUND(c.clean_recovery_amount / t.targeted_accounts, 2) AS clean_recovery_per_account,
    ROUND((c.clean_recovery_amount - LAG(c.clean_recovery_amount) OVER (ORDER BY t.month_str)) / LAG(c.clean_recovery_amount) OVER (ORDER BY t.month_str) * 100, 2) AS independent_mom_growth_pct
FROM targeting_monthly t
LEFT JOIN raw_monthly r ON t.month_str = r.month_str
LEFT JOIN clean_monthly c ON t.month_str = c.month_str
ORDER BY month;
