import streamlit as st
import plotly.express as px
def show(df):

    st.title(" Customer Segmentation")

    st.caption(
        "Explore customer groups discovered using K-Means clustering "
        "and understand the behavioural characteristics of each segment."
    )

    st.divider()
    # ACTUAL CLUSTER MAPPING

    cluster_names = {
        0: "New Customers",
        1: "Loyal Customers",
        2: "Occasional Buyers",
        3: "Premium Customers",
        4: "Regular Customers"
    }

    df = df.copy()

    df["ClusterName"] = df["Cluster"].map(cluster_names)


    st.subheader(" Segment Overview")

    cluster_counts = (
        df["ClusterName"]
        .value_counts()
        .reindex(
            [
                "New Customers",
                "Loyal Customers",
                "Occasional Buyers",
                "Premium Customers",
                "Regular Customers"
            ]
        )
        .fillna(0)
    )

    c1, c2, c3, c4, c5 = st.columns(5)

    c1.metric(
        "New Customers",
        f"{int(cluster_counts['New Customers']):,}"
    )

    c2.metric(
        "Loyal Customers",
        f"{int(cluster_counts['Loyal Customers']):,}"
    )

    c3.metric(
        "Occasional Buyers",
        f"{int(cluster_counts['Occasional Buyers']):,}"
    )

    c4.metric(
        "Premium Customers",
        f"{int(cluster_counts['Premium Customers']):,}"
    )

    c5.metric(
        "Regular Customers",
        f"{int(cluster_counts['Regular Customers']):,}"
    )

    st.divider()

    st.subheader(" Customer Distribution")

    distribution = (
        cluster_counts
        .reset_index()
    )

    distribution.columns = [
        "Segment",
        "Customers"
    ]

    fig = px.bar(
        distribution,
        x="Segment",
        y="Customers",
        text="Customers"
    )

    fig.update_traces(
        textposition="outside"
    )

    fig.update_layout(
        xaxis_title="Customer Segment",
        yaxis_title="Number of Customers",
        showlegend=False,
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

    st.subheader(" Segment Explorer")

    selected_segment = st.selectbox(
        "Select a segment to explore",
        [
            "New Customers",
            "Loyal Customers",
            "Occasional Buyers",
            "Premium Customers",
            "Regular Customers"
        ]
    )

    segment_df = df[
        df["ClusterName"] == selected_segment
    ]

    # SELECTED SEGMENT KPIs

    st.markdown(
        f"### {selected_segment}"
    )

    k1, k2, k3, k4 = st.columns(4)

    k1.metric(
        "Customers",
        f"{len(segment_df):,}"
    )

    k2.metric(
        "Avg Tenure",
        f"{segment_df['Tenure'].mean():.1f}"
    )

    k3.metric(
        "Avg Orders",
        f"{segment_df['OrderCount'].mean():.1f}"
    )

    k4.metric(
        "Avg Cashback",
        f"{segment_df['CashbackAmount'].mean():.1f}"
    )

    st.markdown("")

    k5, k6, k7, k8 = st.columns(4)

    k5.metric(
        "Avg Spend / Order",
        f"{segment_df['AverageSpendPerOrder'].mean():.2f}"
    )

    k6.metric(
        "Avg Engagement",
        f"{segment_df['EngagementScore'].mean():.2f}"
    )

    k7.metric(
        "Churn Rate",
        f"{segment_df['Churn'].mean():.2%}"
    )

    k8.metric(
        "High Value Rate",
        f"{segment_df['HighValueCustomer'].mean():.2%}"
    )

    st.divider()

    st.subheader("Segment Profile")

    profile_columns = [
        "Tenure",
        "OrderCount",
        "CashbackAmount",
        "AverageSpendPerOrder",
        "EngagementScore",
        "Churn",
        "HighValueCustomer"
    ]

    available_profile_columns = [
        col
        for col in profile_columns
        if col in df.columns
    ]

    summary = (
        df.groupby("ClusterName")[available_profile_columns]
        .mean()
        .reindex(
            [
                "New Customers",
                "Loyal Customers",
                "Occasional Buyers",
                "Premium Customers",
                "Regular Customers"
            ]
        )
        .round(2)
    )

    summary = summary.rename(
        columns={
            "Tenure": "Avg Tenure",
            "OrderCount": "Avg Orders",
            "CashbackAmount": "Avg Cashback",
            "AverageSpendPerOrder": "Avg Spend / Order",
            "EngagementScore": "Avg Engagement",
            "Churn": "Churn Rate",
            "HighValueCustomer": "High Value Rate"
        }
    )

    if "Churn Rate" in summary.columns:
        summary["Churn Rate"] = (
            summary["Churn Rate"] * 100
        ).round(2)

    if "High Value Rate" in summary.columns:
        summary["High Value Rate"] = (
            summary["High Value Rate"] * 100
        ).round(2)

    st.dataframe(
        summary,
        use_container_width=True
    )

    st.caption(
        "Churn Rate and High Value Rate are shown as percentages."
    )

    st.divider()
    st.subheader(" Customers in Selected Segment")

    customer_columns = [
        "CustomerID",
        "Tenure",
        "OrderCount",
        "CashbackAmount",
        "AverageSpendPerOrder",
        "Churn"
    ]

    available_customer_columns = [
        col
        for col in customer_columns
        if col in segment_df.columns
    ]

    customer_preview = (
        segment_df[available_customer_columns]
        .head(10)
        .copy()
    )

    if "Churn" in customer_preview.columns:

        customer_preview["Churn"] = (
            customer_preview["Churn"]
            .map({
                0: "Retained",
                1: "Churned"
            })
        )

    st.dataframe(
        customer_preview,
        use_container_width=True,
        hide_index=True
    )

    with st.expander(
        "Business Insight",
        expanded=True
    ):

        if selected_segment == "New Customers":

            st.write(
                """
                **New Customers** represent customers with relatively
                shorter tenure. Retention efforts can focus on improving
                early engagement, encouraging repeat purchases and
                helping customers build familiarity with the platform.
                """
            )

        elif selected_segment == "Loyal Customers":

            st.write(
                """
                **Loyal Customers** show stronger engagement and
                purchasing activity. Loyalty programs, personalized
                rewards and relationship-focused campaigns can help
                maintain their long-term engagement.
                """
            )

        elif selected_segment == "Occasional Buyers":

            st.write(
                """
                **Occasional Buyers** demonstrate relatively lower
                purchasing activity. Targeted offers, reminders and
                personalized product recommendations can encourage
                more frequent purchases.
                """
            )

        elif selected_segment == "Premium Customers":

            st.write(
                """
                **Premium Customers** represent high-value customers
                with strong purchasing characteristics. Retention
                strategies can focus on maintaining service quality,
                exclusive benefits and personalized experiences.
                """
            )

        elif selected_segment == "Regular Customers":

            st.write(
                """
                **Regular Customers** form a substantial customer
                segment with recurring purchasing behaviour. Consistent
                engagement, loyalty incentives and relevant offers can
                help maintain their relationship with the business.
                """
            )

    st.markdown("---")
    st.caption(
        "Retenexa  |  Customer Segmentation Module"
    )