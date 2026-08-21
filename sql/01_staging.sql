-- SQL 01: STAGING & TIMEZONE NORMALIZATION
CREATE OR REPLACE TABLE stg_calls AS
SELECT 
    call_id,
    account_id,
    borrower_id,
    event_at,
    timezone,
    CASE 
        WHEN timezone = 'Asia/Dubai' THEN DATE_ADD(event_at, INTERVAL '1 hour 30 minute')
        WHEN timezone = 'UTC' THEN DATE_ADD(event_at, INTERVAL '5 hour 30 minute')
        ELSE event_at 
    END AS event_at_ist,
    agent_id,
    campaign_id,
    direction,
    vendor_id,
    call_status,
    duration_sec
FROM raw_calls;
