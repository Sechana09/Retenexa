import streamlit as st
import plotly.express as px
def show(df):

    st.markdown(
        """
<div style="
background: linear-gradient(135deg, #2563EB 0%, #3B82F6 55%, #60A5FA 100%);
padding: 32px 36px;
border-radius: 18px;
margin-bottom: 24px;
box-shadow: 0 8px 25px rgba(37, 99, 235, 0.18);
">

<div style="
font-size: 38px;
font-weight: 750;
color: white;
margin-bottom: 8px;
">
Retenexa
</div>

<div style="
font-size: 20px;
font-weight: 600;
color: white;
margin-bottom: 12px;
">
Customer Retention Intelligence
</div>

<div style="
font-size: 15px;
color: rgba(255,255,255,0.92);
line-height: 1.6;
max-width: 900px;
">
Predict customer churn, identify high-risk customers,
understand customer segments, and generate targeted
retention recommendations using machine learning.
</div>

</div>
""",
        unsafe_allow_html=True
    )

    risk_options = ["All"] + sorted(
        df["RiskLevel"].dropna().unique()
    )

    risk = st.selectbox(
        "Filter by Risk Level",
        risk_options
    )

    if risk != "All":
        df = df[df["RiskLevel"] == risk].copy()

    st.markdown("## Business Overview")

    total_customers = len(df)

    churned_customers = int(df["Churn"].sum())

    retained_customers = (
        total_customers - churned_customers
    )

    retention_rate = (
        retained_customers / total_customers * 100
        if total_customers > 0
        else 0
    )

    avg_tenure = (
        df["Tenure"].mean()
        if total_customers > 0
        else 0
    )
    # KPI CARDS

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "Total Customers",
            f"{total_customers:,}"
        )

    with col2:
        st.metric(
            "Churned Customers",
            f"{churned_customers:,}"
        )

    with col3:
        st.metric(
            "Retention Rate",
            f"{retention_rate:.2f}%"
        )

    with col4:
        st.metric(
            "Average Tenure",
            f"{avg_tenure:.1f} months"
        )

    st.write("")

    st.markdown("## Customer Health")

    col1, col2 = st.columns(2)

    with col1:

        churn = (
            df["Churn"]
            .value_counts()
            .reindex([0, 1], fill_value=0)
            .reset_index()
        )

        churn.columns = [
            "Churn",
            "Customers"
        ]

        churn["Status"] = churn["Churn"].map({
            0: "Retained",
            1: "Churned"
        })

        fig = px.pie(
            churn,
            names="Status",
            values="Customers",
            hole=0.62
        )

        fig.update_traces(
            textposition="inside",
            textinfo="percent+label",
            hovertemplate=(
                "<b>%{label}</b>"
                "<br>Customers: %{value:,}"
                "<extra></extra>"
            )
        )

        fig.update_layout(
            title={
                "text": "Customer Distribution",
                "x": 0,
                "xanchor": "left"
            },
            height=400,
            margin=dict(
                t=60,
                b=20,
                l=20,
                r=20
            ),
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            font=dict(size=14),
            legend=dict(
                orientation="h",
                y=-0.05
            )
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    with col2:

        risk_df = (
            df["RiskLevel"]
            .value_counts()
            .reindex(
                ["High", "Medium", "Low"],
                fill_value=0
            )
            .reset_index()
        )

        risk_df.columns = [
            "Risk",
            "Customers"
        ]

        fig2 = px.bar(
            risk_df,
            x="Risk",
            y="Customers",
            text="Customers"
        )

        fig2.update_traces(
            textposition="outside",
            hovertemplate=(
                "<b>%{x}</b>"
                "<br>Customers: %{y:,}"
                "<extra></extra>"
            )
        )

        fig2.update_layout(
            title={
                "text": "Churn Risk Distribution",
                "x": 0,
                "xanchor": "left"
            },
            height=400,
            margin=dict(
                t=60,
                b=20,
                l=20,
                r=20
            ),
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            showlegend=False,
            xaxis_title="Risk Level",
            yaxis_title="Customers"
        )

        st.plotly_chart(
            fig2,
            use_container_width=True
        )

    st.markdown("## Customer Metrics")

    metric1, metric2, metric3, metric4 = st.columns(4)

    avg_orders = (
        df["OrderCount"].mean()
        if "OrderCount" in df.columns
        and total_customers > 0
        else 0
    )

    avg_cashback = (
        df["CashbackAmount"].mean()
        if "CashbackAmount" in df.columns
        and total_customers > 0
        else 0
    )

    complaint_rate = (
        df["Complain"].mean() * 100
        if "Complain" in df.columns
        and total_customers > 0
        else 0
    )

    avg_satisfaction = (
        df["SatisfactionScore"].mean()
        if "SatisfactionScore" in df.columns
        and total_customers > 0
        else 0
    )

    with metric1:
        st.metric(
            "🛒 Avg Orders",
            f"{avg_orders:.1f}"
        )

    with metric2:
        st.metric(
            " Avg Cashback",
            f"{avg_cashback:.1f}"
        )

    with metric3:
        st.metric(
            " Complaint Rate",
            f"{complaint_rate:.1f}%"
        )

    with metric4:
        st.metric(
            " Avg Satisfaction",
            f"{avg_satisfaction:.2f}/5"
        )

    st.write("")

    # ==========================================
    # BUSINESS INSIGHTS
    # ==========================================

    with st.expander(
        " Business Insights",
        expanded=True
    ):

        if total_customers > 0:

            high_risk_count = int(
                (df["RiskLevel"] == "High").sum()
            )

            high_risk_percentage = (
                high_risk_count
                / total_customers
                * 100
            )

            st.markdown(
                f"""
**Current customer base**

- **{total_customers:,}** customers are included in the current view.
- **{churned_customers:,}** customers are classified as churned.
- The current retention rate is **{retention_rate:.2f}%**.
- **{high_risk_count:,}** customers are currently classified as high risk
  ({high_risk_percentage:.1f}% of the displayed customer base).
- Average customer tenure is **{avg_tenure:.1f} months**.

These metrics provide a high-level view of customer health.
The Prediction, Segmentation, AI Retention and Explainability
sections can be used to investigate individual customers
and understand the factors associated with churn.
"""
            )

    st.markdown("##  High-Risk Customers")

    high = df[
        df["RiskLevel"] == "High"
    ].copy()

    if not high.empty:

        display_cols = [
            "CustomerID",
            "RiskLevel",
            "ChurnProbability",
            "RetentionRecommendation"
        ]

        available_cols = [
            col
            for col in display_cols
            if col in high.columns
        ]

        high_display = high[
            available_cols
        ].head(15).copy()

        if "ChurnProbability" in high_display.columns:

            high_display[
                "ChurnProbability"
            ] = (
                high_display[
                    "ChurnProbability"
                ] * 100
            ).round(1).astype(str) + "%"

        st.dataframe(
            high_display,
            use_container_width=True,
            hide_index=True
        )

    else:

        st.info(
            "No high-risk customers are present "
            "in the current filter."
        )

    # ==========================================
    # ABOUT RETENEXA
    # ==========================================

    with st.expander(" About Retenexa"):

        st.markdown(
            """
### Platform Capabilities

**Retenexa** is a customer churn analytics and
retention platform that combines machine learning,
customer segmentation and model explainability.

### Core Technologies

- Python
- Pandas & NumPy
- Scikit-learn
- Random Forest
- K-Means Clustering
- SHAP
- Plotly
- Streamlit

### Core Capabilities

- Customer churn prediction
- Customer risk classification
- Customer segmentation
- Personalized retention recommendations
- Machine learning explainability

The platform is designed to help businesses identify
customers who may be at risk of churn and support
data-driven retention decisions.
"""
        )

    st.markdown("---")

    st.caption(
        "Retenexa • Developed by Sechana Venkatesh"
    )

    st.caption(
        "Random Forest • K-Means • SHAP • Plotly • Streamlit"
    )