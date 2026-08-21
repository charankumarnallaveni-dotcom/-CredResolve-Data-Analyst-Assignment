-- SQL 04: PAYMENT ATTRIBUTION (14-DAY LOOKBACK WINDOW)
CREATE OR REPLACE TABLE fct_payment_attribution AS
WITH unified_touchpoints AS (
    SELECT account_id, event_at_ist AS touchpoint_at, 'VOICE' AS channel, call_id AS interaction_id FROM stg_calls
    UNION ALL
    SELECT account_id, event_at_ist AS touchpoint_at, 'WHATSAPP' AS channel, whatsapp_event_id AS interaction_id FROM stg_whatsapp_events
    UNION ALL
    SELECT account_id, event_at_ist AS touchpoint_at, 'SMS' AS channel, sms_event_id AS interaction_id FROM stg_sms_events
    UNION ALL
    SELECT account_id, event_at_ist AS touchpoint_at, 'FIELD' AS channel, visit_id AS interaction_id FROM stg_field_visits
),
matched_touchpoints AS (
    SELECT 
        p.payment_id,
        p.account_id,
        p.amount,
        p.event_at AS payment_at,
        t.channel,
        t.interaction_id,
        t.touchpoint_at,
        ROW_NUMBER() OVER (
            PARTITION BY p.payment_id 
            ORDER BY t.touchpoint_at DESC
        ) AS touch_rank
    FROM clean_payments p
    LEFT JOIN unified_touchpoints t
        ON p.account_id = t.account_id
        AND t.touchpoint_at BETWEEN DATE_SUB(p.event_at, INTERVAL 14 DAY) AND p.event_at
)
SELECT 
    payment_id,
    account_id,
    amount,
    payment_at,
    COALESCE(channel, 'UNATTRIBUTED_DIRECT') AS attributed_channel,
    COALESCE(interaction_id, 'NONE') AS attributed_interaction_id
FROM matched_touchpoints
WHERE touch_rank = 1 OR touch_rank IS NULL;
