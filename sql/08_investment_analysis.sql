-- SQL 08: INR 10 CRORE INVESTMENT DECISION MODEL
-- Compares 6 investment options on expected incremental recovery, ROI, and break-even

CREATE OR REPLACE TABLE investment_comparison_model AS
SELECT 
    4 AS option_id,
    'Better Borrower Targeting' AS option_name,
    30000 AS addressable_accounts,
    100000000.00 AS total_investment_inr,
    168480000.00 AS base_incremental_recovery_inr,
    68.48 AS base_roi_pct,
    7.1 AS break_even_month,
    'HIGH' AS confidence_level,
    'RECOMMENDED (WINNER)' AS recommendation_status
UNION ALL
SELECT 3, 'AI Voice Automation', 30000, 100000000.00, 142000000.00, 42.00, 8.5, 'MEDIUM', 'NOT RECOMMENDED'
UNION ALL
SELECT 1, 'Better Telephony Infrastructure', 30000, 100000000.00, 135000000.00, 35.00, 8.9, 'MEDIUM', 'NOT RECOMMENDED'
UNION ALL
SELECT 5, 'WhatsApp / Digital Engagement', 22000, 100000000.00, 128000000.00, 28.00, 9.4, 'MEDIUM', 'NOT RECOMMENDED'
UNION ALL
SELECT 2, 'More Collection Agents', 30000, 100000000.00, 112000000.00, 12.00, 10.7, 'LOW-MEDIUM', 'NOT RECOMMENDED'
UNION ALL
SELECT 6, 'Field Operations', 5500, 100000000.00, 95000000.00, -5.00, 12.6, 'LOW', 'NOT RECOMMENDED'
ORDER BY base_roi_pct DESC;
