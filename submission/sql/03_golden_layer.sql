-- SQL 03: GOLDEN LAYER DIMENSIONS & FACTS
CREATE OR REPLACE TABLE dim_agents AS
SELECT DISTINCT
    agent_name,
    team,
    vendor_id,
    DENSE_RANK() OVER (ORDER BY agent_name, team, vendor_id) AS canonical_agent_id
FROM raw_agents;
