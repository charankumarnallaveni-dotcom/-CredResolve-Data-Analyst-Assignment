import pytest
import pandas as pd
import os

base_dir = r"c:\Users\HP\Downloads\Assignment-1"
golden_dir = os.path.join(base_dir, "data", "golden")

def test_dim_accounts_pk_unique():
    df = pd.read_csv(os.path.join(golden_dir, "dim_accounts.csv"))
    assert df["account_id"].is_unique

def test_golden_payments_success_only():
    df = pd.read_csv(os.path.join(golden_dir, "fct_payments.csv"))
    assert (df["payment_status"].str.upper() == "SUCCESS").all()

def test_golden_payments_no_dup_refs():
    df = pd.read_csv(os.path.join(golden_dir, "fct_payments.csv"))
    assert not df["payment_reference"].duplicated().any()

def test_golden_payments_positive_amount():
    df = pd.read_csv(os.path.join(golden_dir, "fct_payments.csv"))
    assert (df["amount"] > 0).all()

def test_fct_payments_referential_integrity():
    df_p = pd.read_csv(os.path.join(golden_dir, "fct_payments.csv"))
    df_a = pd.read_csv(os.path.join(golden_dir, "dim_accounts.csv"))
    assert df_p["account_id"].isin(df_a["account_id"]).all()
