import pytest
import pandas as pd
from pathlib import Path

base_dir = Path(__file__).resolve().parent.parent
golden_dir = base_dir / "data" / "golden"

def test_dim_accounts_pk_unique():
    df = pd.read_csv(golden_dir / "dim_accounts.csv")
    assert df["account_id"].is_unique

def test_golden_payments_success_only():
    df = pd.read_csv(golden_dir / "fct_payments.csv")
    assert (df["payment_status"].str.upper() == "SUCCESS").all()

def test_golden_payments_no_dup_refs():
    df = pd.read_csv(golden_dir / "fct_payments.csv")
    assert not df["payment_reference"].duplicated().any()

def test_golden_payments_positive_amount():
    df = pd.read_csv(golden_dir / "fct_payments.csv")
    assert (df["amount"] > 0).all()

def test_fct_payments_referential_integrity():
    df_p = pd.read_csv(golden_dir / "fct_payments.csv")
    df_a = pd.read_csv(golden_dir / "dim_accounts.csv")
    assert df_p["account_id"].isin(df_a["account_id"]).all()
