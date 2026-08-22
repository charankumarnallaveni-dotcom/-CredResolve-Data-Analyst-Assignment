import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import os

# Page Configuration
st.set_page_config(
    page_title="Executive Collections & Capital Allocation Dashboard",
    page_icon="📊",
    layout="wide"
)

# Custom Styling
st.markdown("""
<style>
    .main-title { font-size: 2.2rem; font-weight: 800; color: #1E293B; margin-bottom: 0px; }
    .sub-title { font-size: 1.0rem; color: #64748B; margin-bottom: 20px; }
    .kpi-card { background-color: #F8FAFC; border: 1px solid #E2E8F0; border-radius: 8px; padding: 15px; text-align: center; }
    .kpi-val { font-size: 1.8rem; font-weight: 700; color: #0F172A; }
    .kpi-label { font-size: 0.85rem; color: #475569; text-transform: uppercase; font-weight: 600; }
    .kpi-sub { font-size: 0.75rem; color: #64748B; }
    .badge-win { background-color: #DCFCE7; color: #166534; padding: 4px 8px; border-radius: 4px; font-weight: 700; }
</style>
""", unsafe_allow_html=True)

# Load Golden Dataset Metrics
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
golden_dir = os.path.join(base_dir, "data", "golden")
reports_dir = os.path.join(base_dir, "reports")

@st.cache_data
def load_data():
    df_perf = pd.read_csv(os.path.join(golden_dir, "monthly_performance.csv"))
    df_bridge = pd.read_csv(os.path.join(reports_dir, "recovery_truth_bridge.csv"))
    df_scorecard = pd.read_csv(os.path.join(golden_dir, "driver_scorecard.csv"))
    df_inv = pd.read_csv(os.path.join(golden_dir, "investment_comparison.csv"))
    return df_perf, df_bridge, df_scorecard, df_inv

try:
    df_perf, df_bridge, df_scorecard, df_inv = load_data()
except Exception as e:
    st.error(f"Error loading Golden Dataset files: {e}")
    st.stop()

# Header Section
st.markdown('<div class="main-title">C-Suite Executive Collections Audit & Capital Allocation Dashboard</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">60-Second CEO Decision Interface | Target Claim Audit: "Recovery improved by 11% MoM"</div>', unsafe_allow_html=True)

# Sidebar Filters
st.sidebar.header("Executive Filters")
sel_month = st.sidebar.selectbox("Select Time Horizon", ["Full 8-Month Window (7 Complete Months + Partial Aug) (Jan-Aug 2026)"] + list(df_perf["month"].unique()))
sel_portfolio = st.sidebar.multiselect("Select Loan Product", ["AUTO", "BNPL", "CONSUMER", "CREDIT_CARD", "PERSONAL"], default=["AUTO", "BNPL", "CONSUMER", "CREDIT_CARD", "PERSONAL"])
sel_dpd = st.sidebar.multiselect("Select DPD Risk Bucket", ["1-30 DPD", "31-60 DPD", "61-90 DPD", "90+ DPD"], default=["1-30 DPD", "31-60 DPD", "61-90 DPD", "90+ DPD"])

# Executive 60-Second Verdict Summary Box
st.warning("""
**60-Second Executive Summary**:
1. **Is the 11% improvement real?** **NO (CLAIM REFUTED)**. The 11% figure represents a single cherry-picked month (March 2026). Actual recovery performance is **declining by -19.9%** (Recovery Rate fell from 9.01% in Jan to 7.22% in Jul).
2. **Why did it happen?** Raw reporting included **INR 575.8M in FAILED/PENDING payments** and **INR 64.2M in duplicate transaction retries**. Operationally, targeting shifted into higher DPD cohorts (>60 DPD grew from 18% to 32%).
3. **Where to invest ₹10 Cr?** **OPTION 4: BETTER BORROWER TARGETING**. Fixes queue misallocation, delivering **+INR 168.5M incremental recovery**, **+68.5% ROI**, and **7.1-month break-even**.
""")

st.markdown("---")

# 1. Top Section - 6 KPI Cards
col1, col2, col3, col4, col5, col6 = st.columns(6)

with col1:
    st.markdown('<div class="kpi-card"><div class="kpi-val" style="color:#059669;">7.22%</div><div class="kpi-label">Independent Rec Rate</div><div class="kpi-sub">Clean Verified Capital</div></div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="kpi-card"><div class="kpi-val" style="color:#DC2626;">11.84%</div><div class="kpi-label">Reported Rec Rate</div><div class="kpi-sub">Legacy Gross Uncleaned</div></div>', unsafe_allow_html=True)

with col3:
    st.markdown('<div class="kpi-card"><div class="kpi-val" style="color:#D97706;">+66.7%</div><div class="kpi-label">Gross Inflation</div><div class="kpi-sub">Over-Reporting Bias</div></div>', unsafe_allow_html=True)

with col4:
    st.markdown('<div class="kpi-card"><div class="kpi-val">₹1.150 B</div><div class="kpi-label">Clean Recovered</div><div class="kpi-sub">Total SUCCESS Net</div></div>', unsafe_allow_html=True)

with col5:
    st.markdown('<div class="kpi-card"><div class="kpi-val">₹25,948</div><div class="kpi-label">Recovery / Account</div><div class="kpi-sub">Down from ₹31,522</div></div>', unsafe_allow_html=True)

with col6:
    st.markdown('<div class="kpi-card"><div class="kpi-val">24.26%</div><div class="kpi-label">PTP Kept Rate</div><div class="kpi-sub">Promises Kept %</div></div>', unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# 2. Main Section - 2 Columns Layout
left_col, right_col = st.columns([1.1, 0.9])

with left_col:
    st.subheader("A. Reported Gross vs Independent Clean Recovery Trend")
    
    fig_trend = go.Figure()
    fig_trend.add_trace(go.Scatter(
        x=df_bridge["month"], y=df_bridge["reported_gross_recovery_inr"] / 1e6,
        mode="lines+markers", name="Reported Gross Recovery (Legacy)",
        line=dict(color="#DC2626", width=3, dash="dash")
    ))
    fig_trend.add_trace(go.Scatter(
        x=df_bridge["month"], y=df_bridge["independent_clean_recovery_inr"] / 1e6,
        mode="lines+markers", name="Independent Clean Recovery (Golden)",
        line=dict(color="#059669", width=4)
    ))
    
    # Annotate April Performance Cliff
    fig_trend.add_vrect(x0="2026-04", x1="2026-08", fillcolor="red", opacity=0.1, line_width=0)
    fig_trend.add_annotation(x="2026-04", y=200, text="April Cliff Drop (-9.2% Yield)", showarrow=True, arrowhead=2, ax=0, ay=-40)
    
    fig_trend.update_layout(
        yaxis_title="Recovery Amount (INR Millions)",
        xaxis_title="Month",
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
        height=380,
        margin=dict(l=20, r=20, t=30, b=20)
    )
    st.plotly_chart(fig_trend, use_container_width=True)

with right_col:
    st.subheader("B. Recovery Truth Bridge (Raw ➔ Golden)")
    
    tot_reported = df_bridge["reported_gross_recovery_inr"].sum() / 1e6
    tot_failed = df_bridge["data_quality_failed_pending_adj_inr"].sum() / 1e6
    tot_dup = df_bridge["deduplication_dup_ref_adj_inr"].sum() / 1e6
    tot_clean = df_bridge["independent_clean_recovery_inr"].sum() / 1e6
    
    fig_waterfall = go.Figure(go.Waterfall(
        name="Truth Bridge", orientation="v",
        measure=["absolute", "relative", "relative", "total"],
        x=["Reported Gross", "Failed/Pending Payments", "Duplicate Reference Retries", "Independent Clean"],
        textposition="outside",
        text=[f"₹{tot_reported:.1f}M", f"₹{tot_failed:.1f}M", f"₹{tot_dup:.1f}M", f"₹{tot_clean:.1f}M"],
        y=[tot_reported, tot_failed, tot_dup, tot_clean],
        connector={"line": {"color": "rgb(63, 63, 63)"}},
        decreasing={"marker": {"color": "#DC2626"}},
        totals={"marker": {"color": "#059669"}}
    ))
    fig_waterfall.update_layout(
        yaxis_title="Capital (INR Millions)",
        height=380,
        margin=dict(l=20, r=20, t=30, b=20)
    )
    st.plotly_chart(fig_waterfall, use_container_width=True)

st.markdown("---")

# 3. Bottom Section - Drivers & Investment Decision
col_drv, col_inv = st.columns([1.0, 1.0])

with col_drv:
    st.subheader("C. Why Did Performance Change? (Top Drivers)")
    st.dataframe(
        df_scorecard[["rank", "driver", "recovery_impact", "evidence_strength", "classification"]],
        use_container_width=True,
        hide_index=True
    )

with col_inv:
    st.subheader("D. ₹10 Crore Capital Allocation Decision Matrix")
    
    st.success("""
    **RECOMMENDED WINNER**: **OPTION 4 — BETTER BORROWER TARGETING**
    * **12-Month Net Incremental Recovery**: **₹168.48 Million**
    * **12-Month Net ROI**: **+68.5%** (Base Case) | **+110.6%** (Upside Case)
    * **Break-Even Period**: **7.1 Months**
    * **Downside Scenario ROI**: **+15.2%** (Only option with positive downside ROI)
    * **Confidence Level**: **HIGH** (Backed by DiD model & Golden Dataset DPD shift audit)
    """)

st.subheader("12-Month ROI & Financial Comparison Across All 6 Candidate Options")
fig_inv = px.bar(
    df_inv.sort_values(by="base_roi_pct", ascending=True),
    x="base_roi_pct", y="option_name", orientation="h",
    text="base_roi_pct", color="confidence_level",
    color_discrete_map={"HIGH": "#059669", "MEDIUM": "#D97706", "LOW-MEDIUM": "#EF4444", "LOW": "#991B1B"},
    labels={"base_roi_pct": "12-Month Base ROI (%)", "option_name": "Investment Option"}
)
fig_inv.update_traces(texttemplate="%{text:.1f}%", textposition="outside")
fig_inv.update_layout(height=320, margin=dict(l=20, r=20, t=30, b=20))
st.plotly_chart(fig_inv, use_container_width=True)

# Data Quality Indicator Footer Bar
st.markdown("---")
st.caption("""
**Data Quality Audit Indicator**: 46,253 total DQ actions logged to `data/clean/data_quality_actions.csv` | 10,150 payments rejected | 2,957 duplicate rows removed | 30,000 synthetic agents consolidated to 10 canonical profiles | 100% Automated DQ Tests PASSing.
""")
