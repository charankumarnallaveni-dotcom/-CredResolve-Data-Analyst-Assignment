-- SQL 02: DEDUPLICATION & CLEANING
CREATE OR REPLACE TABLE clean_payments AS
WITH ranked_payments AS (
    SELECT 
        payment_id,
        account_id,
        borrower_id,
        event_at,
        payment_reference,
        amount,
        UPPER(payment_status) AS payment_status,
        ROW_NUMBER() OVER (
            PARTITION BY payment_reference 
            ORDER BY event_at ASC
        ) AS ref_rank
    FROM raw_payments
    WHERE UPPER(payment_status) = 'SUCCESS'
)
SELECT 
    payment_id,
    account_id,
    borrower_id,
    event_at,
    payment_reference,
    amount,
    payment_status
FROM ranked_payments
WHERE ref_rank = 1;
