import streamlit as st
def show(df):

    st.title(" Customer Churn Prediction")
    st.caption(
        "Analyze an individual customer, understand their churn risk, "
        "and view a personalized retention strategy."
    )

    st.divider()

    st.subheader(" Find a Customer")

    search = st.text_input(
        "Search Customer ID",
        placeholder="Enter Customer ID...",
        label_visibility="collapsed"
    )

    if search:

        results = df[
            df["CustomerID"]
            .astype(str)
            .str.contains(search, case=False, na=False)
        ]

        if len(results) == 0:
            st.warning(
                " No customer found. Please check the Customer ID."
            )
            return

        customer = results.iloc[0]

        if len(results) > 1:
            st.caption(
                f"{len(results)} matching customers found. "
                "Showing the first match."
            )

    else:

        customer_id = st.selectbox(
            "Select Customer",
            sorted(df["CustomerID"].unique())
        )

        customer = df[
            df["CustomerID"] == customer_id
        ].iloc[0]

    st.divider()

    st.subheader(" Prediction Summary")

    churn_probability = float(
        customer["ChurnProbability"]
    )

    risk_level = str(
        customer["RiskLevel"]
    )

    customer_status = (
        "Churned"
        if customer["Churn"] == 1
        else "Retained"
    )

    c1, c2, c3 = st.columns(3)

    c1.metric(
        " Churn Probability",
        f"{churn_probability:.2%}"
    )

    c2.metric(
        " Risk Level",
        risk_level
    )

    c3.metric(
        " Customer Status",
        customer_status
    )

    st.divider()

    if risk_level == "High":

        st.error(
            "🔴 **High Churn Risk** — This customer shows a high "
            "likelihood of churn and should receive targeted "
            "retention attention."
        )

    elif risk_level == "Medium":

        st.warning(
            "🟠 **Medium Churn Risk** — This customer should be "
            "monitored and engaged through appropriate retention "
            "initiatives."
        )

    else:

        st.success(
            "🟢 **Low Churn Risk** — This customer currently shows "
            "relatively stable behaviour."
        )

    st.divider()

    st.subheader(" Customer Profile")

    profile_cols = st.columns(4)

    profile_cols[0].metric(
        "Customer ID",
        str(customer["CustomerID"])
    )

    profile_cols[1].metric(
        "Tenure",
        f"{float(customer['Tenure']):.0f}"
    )

    profile_cols[2].metric(
        "Orders",
        f"{float(customer['OrderCount']):.0f}"
    )

    profile_cols[3].metric(
        "Satisfaction",
        f"{float(customer['SatisfactionScore']):.0f}/5"
    )

    st.markdown("")

    st.subheader(" Customer Behaviour")

    behavior_cols = st.columns(4)

    behavior_cols[0].metric(
        " Cashback",
        f"{float(customer['CashbackAmount']):.2f}"
    )

    behavior_cols[1].metric(
        " City Tier",
        str(customer["CityTier"])
    )

    behavior_cols[2].metric(
        " Addresses",
        f"{float(customer['NumberOfAddress']):.0f}"
    )

    behavior_cols[3].metric(
        " Complaints",
        str(customer["Complain"])
    )

    st.divider()

    st.subheader(" Customer Details")

    display_cols = [
        "CustomerID",
        "Tenure",
        "Gender",
        "CityTier",
        "PreferredLoginDevice",
        "PreferredPaymentMode",
        "PreferedOrderCat",
        "OrderCount",
        "DaySinceLastOrder",
        "CashbackAmount",
        "SatisfactionScore",
        "Complain",
        "RiskLevel",
        "ChurnProbability"
    ]

    available_cols = [
        col
        for col in display_cols
        if col in customer.index
    ]

    details = customer[available_cols].to_frame().T

    # Format churn probability safely
    if "ChurnProbability" in details.columns:

        probability = float(
            customer["ChurnProbability"]
        )

        details["ChurnProbability"] = (
            f"{probability:.2%}"
        )

    st.dataframe(
        details,
        use_container_width=True,
        hide_index=True
    )

    with st.expander(
        " Show Complete Customer Details"
    ):

        complete_details = customer.to_frame().T

        # Make a copy so the original customer data is untouched
        complete_details = complete_details.copy()

        if "ChurnProbability" in complete_details.columns:

            probability = float(
                customer["ChurnProbability"]
            )

            complete_details.at[
                complete_details.index[0],
                "ChurnProbability"
            ] = f"{probability:.2%}"

        st.dataframe(
            complete_details,
            use_container_width=True,
            hide_index=True
        )

    st.divider()

    st.subheader(" Retention Recommendation")

    recommendation_text = str(
        customer["RetentionRecommendation"]
    )

    recommendations = recommendation_text.split("|")

    for recommendation in recommendations:

        recommendation = recommendation.strip()

        if recommendation:

            st.success(
                f"✓ {recommendation}"
            )

    st.caption(
        "Recommendations are generated from the customer's "
        "churn risk and behavioural characteristics."
    )

    st.divider()

    with st.expander(
        " Business Insight",
        expanded=True
    ):

        if risk_level == "High":

            st.write(
                """
                This customer has been classified as **High Risk**.

                The predicted churn probability indicates that this
                customer may require immediate retention attention.
                Targeted offers, proactive customer support and
                personalized engagement can be considered.
                """
            )

        elif risk_level == "Medium":

            st.write(
                """
                This customer has been classified as **Medium Risk**.

                The customer should be monitored and engaged through
                personalized communication, loyalty incentives and
                targeted offers.
                """
            )

        else:

            st.write(
                """
                This customer has been classified as **Low Risk**.

                The customer currently shows relatively stable
                behaviour. Regular engagement and loyalty initiatives
                can help maintain the relationship.
                """
            )

    st.markdown("---")
    st.caption(
        "Retenexa  |  Customer Prediction Module"
    )