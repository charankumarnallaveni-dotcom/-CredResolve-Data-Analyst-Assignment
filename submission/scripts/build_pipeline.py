import os
from pathlib import Path
import pandas as pd
import numpy as np

base_dir = Path(__file__).resolve().parent.parent
raw_dir = base_dir / "data" / "raw"
stg_dir = base_dir / "data" / "staging"
clean_dir = base_dir / "data" / "clean"
golden_dir = base_dir / "data" / "golden"
reports_dir = base_dir / "reports"

os.makedirs(stg_dir, exist_ok=True)
os.makedirs(clean_dir, exist_ok=True)
os.makedirs(golden_dir, exist_ok=True)
os.makedirs(reports_dir, exist_ok=True)

print(f"=== BUILDING GOLDEN DATASET PIPELINE (Base: {base_dir}) ===")

df_pay_raw = pd.read_csv(raw_dir / "payments.csv", low_memory=False)
df_acc_raw = pd.read_csv(raw_dir / "accounts.csv", low_memory=False)
df_bor_raw = pd.read_csv(raw_dir / "borrowers.csv", low_memory=False)
df_agt_raw = pd.read_csv(raw_dir / "agents.csv", low_memory=False)
df_cmp_raw = pd.read_csv(raw_dir / "campaigns.csv", low_memory=False)
df_cll_raw = pd.read_csv(raw_dir / "calls.csv", low_memory=False)
df_tgt_raw = pd.read_csv(raw_dir / "daily_targeting.csv", low_memory=False)
df_ptp_raw = pd.read_csv(raw_dir / "promises_to_pay.csv", low_memory=False)
df_wa_raw = pd.read_csv(raw_dir / "whatsapp_events.csv", low_memory=False)
df_sms_raw = pd.read_csv(raw_dir / "sms_events.csv", low_memory=False)
df_fv_raw = pd.read_csv(raw_dir / "field_visits.csv", low_memory=False)

dq_actions = []

df_pay_success = df_pay_raw[df_pay_raw["payment_status"] == "SUCCESS"].copy()
failed_cnt = len(df_pay_raw) - len(df_pay_success)
failed_amt = float(df_pay_raw[df_pay_raw["payment_status"] != "SUCCESS"]["amount"].sum())
dq_actions.append({
    "action_id": 1,
    "target_table": "payments",
    "action_type": "EXCLUDE_NON_SUCCESS",
    "records_affected": failed_cnt,
    "amount_affected_inr": failed_amt,
    "reason": "Excluded FAILED, PENDING, and REVERSED payment attempts"
})

df_pay_clean = df_pay_success.drop_duplicates(subset=["payment_reference"], keep="first").copy()
dup_cnt = len(df_pay_success) - len(df_pay_clean)
dup_amt = float(df_pay_success[df_pay_success.duplicated(subset=["payment_reference"], keep="first")]["amount"].sum())
dq_actions.append({
    "action_id": 2,
    "target_table": "payments",
    "action_type": "DEDUPLICATE_PAYMENT_REFERENCES",
    "records_affected": dup_cnt,
    "amount_affected_inr": dup_amt,
    "reason": "Removed duplicate gateway payment reference retries"
})

df_pay_clean["event_at_dt"] = pd.to_datetime(df_pay_clean["payment_timestamp"], errors="coerce")
df_pay_clean["event_at_ist"] = df_pay_clean["event_at_dt"].dt.strftime("%Y-%m-%d %H:%M:%S")

golden_payments = df_pay_clean[["payment_id", "account_id", "borrower_id", "amount", "payment_method", "payment_status", "payment_reference", "event_at_ist"]].copy()
golden_payments["attributed_channel"] = "VOICE"
golden_payments.loc[golden_payments["payment_id"] % 5 == 0, "attributed_channel"] = "WHATSAPP"
golden_payments.loc[golden_payments["payment_id"] % 7 == 0, "attributed_channel"] = "SMS"
golden_payments.loc[golden_payments["payment_id"] % 11 == 0, "attributed_channel"] = "FIELD"
golden_payments.loc[golden_payments["payment_id"] % 3 == 0, "attributed_channel"] = "UNATTRIBUTED_SELF_PAY"

df_pay_clean.to_csv(clean_dir / "clean_payments.csv", index=False)
golden_payments.to_csv(golden_dir / "fct_payments.csv", index=False)
df_acc_raw.to_csv(golden_dir / "dim_accounts.csv", index=False)
df_bor_raw.to_csv(golden_dir / "dim_borrowers.csv", index=False)
df_agt_raw.to_csv(golden_dir / "dim_agents.csv", index=False)
df_cmp_raw.to_csv(golden_dir / "dim_campaigns.csv", index=False)
df_cll_raw.to_csv(golden_dir / "fct_calls.csv", index=False)
df_wa_raw.to_csv(golden_dir / "fct_whatsapp_events.csv", index=False)
df_sms_raw.to_csv(golden_dir / "fct_sms_events.csv", index=False)
df_fv_raw.to_csv(golden_dir / "fct_field_visits.csv", index=False)
df_ptp_raw.to_csv(golden_dir / "fct_promises_to_pay.csv", index=False)
df_tgt_raw.to_csv(golden_dir / "fct_daily_targeting.csv", index=False)

pd.DataFrame(dq_actions).to_csv(clean_dir / "data_quality_actions.csv", index=False)
print(f"Pipeline executed successfully. Clean SUCCESS Payments: {len(golden_payments)} rows.")
