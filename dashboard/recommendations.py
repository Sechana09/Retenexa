import streamlit as st
import plotly.express as px
def show(df):

    st.title(" Retention Action Center")

    st.caption(
        "Turn churn predictions into targeted customer retention actions."
    )

    st.divider()

    # RISK COUNTS

    high_count = len(
        df[df["RiskLevel"] == "High"]
    )

    medium_count = len(
        df[df["RiskLevel"] == "Medium"]
    )

    low_count = len(
        df[df["RiskLevel"] == "Low"]
    )

    total_customers = len(df)

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "🔴 High Risk",
        f"{high_count:,}"
    )

    c2.metric(
        "🟡 Medium Risk",
        f"{medium_count:,}"
    )

    c3.metric(
        "🟢 Low Risk",
        f"{low_count:,}"
    )

    c4.metric(
        " Total Customers",
        f"{total_customers:,}"
    )

    st.divider()

    # PRIORITY MESSAGE

    if high_count > 0:

        high_percentage = (
            high_count / total_customers
        )

        st.warning(
            f" **{high_count:,} customers ({high_percentage:.1%}) "
            "are classified as High Risk.** "
            "These customers can be prioritized for retention intervention."
        )

    # RISK FILTER

    st.subheader(" Customer Risk Filter")

    risk = st.selectbox(
        "Select Risk Level",
        [
            "All",
            "High",
            "Medium",
            "Low"
        ]
    )

    filtered_df = df.copy()

    if risk != "All":

        filtered_df = filtered_df[
            filtered_df["RiskLevel"] == risk
        ]

    st.write(
        f"Showing **{len(filtered_df):,} customers**"
    )

    # CUSTOMER RECOMMENDATION TABLE

    display_cols = [
        "CustomerID",
        "RiskLevel",
        "ChurnProbability",
        "BehaviorSegment",
        "RetentionRecommendation"
    ]

    available_cols = [
        col
        for col in display_cols
        if col in filtered_df.columns
    ]

    table_df = filtered_df[
        available_cols
    ].copy()

    if "ChurnProbability" in table_df.columns:

        table_df["ChurnProbability"] = (
            table_df["ChurnProbability"]
            .astype(float)
            .map(lambda x: f"{x:.2%}")
        )

    table_df = table_df.rename(
        columns={
            "CustomerID": "Customer ID",
            "RiskLevel": "Risk Level",
            "ChurnProbability": "Churn Probability",
            "BehaviorSegment": "Customer Segment",
            "RetentionRecommendation":
                "Retention Recommendation"
        }
    )

    st.dataframe(
        table_df,
        use_container_width=True,
        hide_index=True
    )

    st.divider()
    # RISK DISTRIBUTION

    st.subheader(" Retention Priority Distribution")

    risk_order = [
        "High",
        "Medium",
        "Low"
    ]

    risk_data = (
        df["RiskLevel"]
        .value_counts()
        .reindex(risk_order)
        .fillna(0)
        .reset_index()
    )

    risk_data.columns = [
        "RiskLevel",
        "Customers"
    ]

    fig = px.bar(
        risk_data,
        x="RiskLevel",
        y="Customers",
        text="Customers"
    )

    fig.update_traces(
        textposition="outside"
    )

    fig.update_layout(
        height=400,
        showlegend=False,
        xaxis_title="Risk Level",
        yaxis_title="Number of Customers",
        margin=dict(
            l=20,
            r=20,
            t=30,
            b=20
        )
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.divider()
    # RETENTION STRATEGY

    st.subheader(" Recommended Retention Strategy")

    if risk == "High":

        st.error(
            """
            ### 🔴 High-Risk Customers

            These customers have a predicted churn probability of
            **70% or higher**.

            **Potential actions:**

            - Resolve unresolved customer complaints
            - Launch targeted retention campaigns
            - Provide personalized incentives
            - Offer cashback or loyalty rewards
            - Encourage repeat purchases
            - Monitor subsequent customer engagement
            """
        )

    elif risk == "Medium":

        st.warning(
            """
            ### 🟡 Medium-Risk Customers

            These customers have a predicted churn probability between
            **40% and 69%**.

            **Potential actions:**

            - Provide targeted discounts
            - Recommend relevant products
            - Encourage repeat purchases
            - Increase customer engagement
            - Monitor changes in customer activity
            """
        )

    elif risk == "Low":

        st.success(
            """
            ### 🟢 Low-Risk Customers

            These customers have a predicted churn probability below
            **40%**.

            **Potential actions:**

            - Continue loyalty engagement
            - Provide personalized product recommendations
            - Encourage repeat purchases
            - Maintain positive customer relationships
            - Offer loyalty benefits where appropriate
            """
        )

    else:

        st.info(
            """
            ###  Risk-Based Retention Strategy

            **High Risk → Immediate retention intervention**

            **Medium Risk → Engagement and targeted incentives**

            **Low Risk → Loyalty and relationship maintenance**

            The risk classification helps retention teams allocate
            attention according to predicted churn probability.
            """
        )

    st.divider()

    # SEGMENT + RISK ANALYSIS

    if "BehaviorSegment" in df.columns:

        st.subheader(" Risk Across Customer Segments")

        segment_risk = (
            df.groupby("BehaviorSegment")["ChurnProbability"]
            .mean()
            .sort_values(ascending=False)
            .reset_index()
        )

        segment_risk.columns = [
            "Customer Segment",
            "Average Churn Probability"
        ]

        segment_risk[
            "Average Churn Probability"
        ] = (
            segment_risk[
                "Average Churn Probability"
            ] * 100
        ).round(2)

        segment_risk = segment_risk.rename(
            columns={
                "Average Churn Probability":
                    "Avg Churn Probability (%)"
            }
        )

        st.dataframe(
            segment_risk,
            use_container_width=True,
            hide_index=True
        )

        st.caption(
            "Average churn probability is calculated across customers "
            "within each behavioural segment."
        )

    st.divider()

    st.subheader(" Export Retention Plan")

    csv = filtered_df.to_csv(
        index=False
    )

    st.download_button(
        label=" Download Customer Recommendations",
        data=csv,
        file_name="retention_recommendations.csv",
        mime="text/csv"
    )

    st.caption(
        f"Export contains {len(filtered_df):,} customer records "
        "based on the selected risk filter."
    )

    with st.expander(
        "How Retenexa Generates Retention Actions"
    ):

        st.write(
            """
            Retenexa combines the Random Forest churn prediction with
            customer behavioural characteristics to create actionable
            retention recommendations.

            The workflow is:

            **Churn Model → Churn Probability → Risk Level → "
            "Behaviour Analysis → Retention Recommendation**

            Risk levels are based on the predicted churn probability:

            - **High:** ≥ 70%
            - **Medium:** 40% – 69%
            - **Low:** < 40%

            The recommendation engine considers characteristics such as
            tenure, complaint history, order count, cashback, customer
            activity and loyalty characteristics.
            """
        )

    st.markdown("---")
    st.caption(
        "Retenexa  |  Retention Action Center"
    )