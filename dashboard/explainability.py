import streamlit as st
import pandas as pd
import numpy as np
import joblib
import shap
import matplotlib.pyplot as plt
from pathlib import Path
def show(df):

    st.title(" Model Explainability")

    st.caption(
        "Understand which customer characteristics influence the "
        "Random Forest churn prediction."
    )

    st.divider()

    PROJECT_ROOT = Path(__file__).resolve().parents[1]

    MODEL_PATH = (
        PROJECT_ROOT
        / "artifacts"
        / "churn_model.pkl"
    )

    FEATURES_PATH = (
        PROJECT_ROOT
        / "artifacts"
        / "feature_names.pkl"
    )

    SHAP_PATH = (
        PROJECT_ROOT
        / "artifacts"
        / "shap_global_importance.csv"
    )

    try:

        model = joblib.load(
            MODEL_PATH
        )

        feature_names = joblib.load(
            FEATURES_PATH
        )

        feature_names = list(
            feature_names
        )

    except FileNotFoundError as e:

        st.error(
            f"Required model artifact was not found:\n\n{e}"
        )

        return

    try:

        importance_df = pd.read_csv(
            SHAP_PATH
        )

    except FileNotFoundError:

        st.error(
            "shap_global_importance.csv was not found "
            "inside the artifacts folder."
        )

        st.info(
            "Run the final cell in "
            "07_Model_Explainability.ipynb "
            "to create the file."
        )

        return

    model_data = df.copy()

    columns_to_remove = [
        "CustomerID",
        "Churn"
    ]

    model_data = model_data.drop(
        columns=[
            col
            for col in columns_to_remove
            if col in model_data.columns
        ],
        errors="ignore"
    )

    # One-hot encoding
    model_data = pd.get_dummies(
        model_data,
        drop_first=False
    )

    # Match exact model features
    X = model_data.reindex(
        columns=feature_names,
        fill_value=0
    )

    # Ensure numeric values
    X = X.apply(
        pd.to_numeric,
        errors="coerce"
    ).fillna(0)

    st.subheader("Customer-Level Explanation")

    st.write(
        "Search for a customer to understand the factors "
        "behind their churn prediction."
    )

    customer_ids = (
        df["CustomerID"]
        .astype(str)
        .tolist()
    )

    search_text = st.text_input(
        " Search Customer ID",
        placeholder="Enter Customer ID..."
    )

    if search_text.strip():

        filtered_ids = [
            customer_id
            for customer_id in customer_ids
            if search_text.strip().lower()
            in customer_id.lower()
        ]

    else:

        filtered_ids = customer_ids

    if len(filtered_ids) == 0:

        st.warning(
            "No customer found with that ID."
        )

        return

    # Avoid an unnecessarily large selectbox
    filtered_ids = filtered_ids[:100]

    selected_customer = st.selectbox(
        "Select Customer",
        filtered_ids
    )

    matching_positions = np.where(
        df["CustomerID"]
        .astype(str)
        .values
        == selected_customer
    )[0]

    if len(matching_positions) == 0:

        st.error(
            "Unable to locate the selected customer."
        )

        return

    x_position = matching_positions[0]

    customer = X.iloc[
        [x_position]
    ]

    original_customer = df.iloc[
        x_position
    ]

    try:

        prediction_probability = (
            model
            .predict_proba(customer)[0][1]
        )

    except Exception as e:

        st.error(
            "Unable to calculate churn probability."
        )

        st.exception(e)

        return

    if prediction_probability >= 0.70:

        risk = "High"

    elif prediction_probability >= 0.40:

        risk = "Medium"

    else:

        risk = "Low"

    st.subheader("Prediction Summary")

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Customer ID",
        selected_customer
    )

    col2.metric(
        "Churn Probability",
        f"{prediction_probability:.1%}"
    )

    col3.metric(
        "Risk Level",
        risk
    )

    # Risk interpretation
    if risk == "High":

        st.error(
            "🔴 **High Risk** — The model assigns this customer "
            "a churn probability of 70% or higher."
        )

    elif risk == "Medium":

        st.warning(
            "🟠 **Medium Risk** — The model assigns this customer "
            "a churn probability between 40% and 69%."
        )

    else:

        st.success(
            "🟢 **Low Risk** — The model assigns this customer "
            "a churn probability below 40%."
        )

    st.divider()

    st.subheader(
        "Global Feature Importance"
    )

    st.caption(
        "Mean absolute SHAP values calculated across "
        "the complete dataset of 5,630 customers."
    )
    if not {
        "Feature",
        "Importance"
    }.issubset(
        importance_df.columns
    ):

        st.error(
            "The global SHAP file does not contain "
            "the expected Feature and Importance columns."
        )

        return

    top_features = (
        importance_df
        .sort_values(
            "Importance",
            ascending=False
        )
        .head(15)
    )

    fig, ax = plt.subplots(
        figsize=(10, 6)
    )

    ax.barh(
        top_features["Feature"].values[::-1],
        top_features["Importance"].values[::-1]
    )

    ax.set_xlabel(
        "Mean |SHAP Value|"
    )

    ax.set_ylabel(
        "Feature"
    )

    ax.set_title(
        "Top Features Influencing Churn"
    )

    plt.tight_layout()

    st.pyplot(
        fig,
        use_container_width=True
    )

    plt.close(fig)

    st.caption(
        "Higher mean absolute SHAP values indicate greater "
        "overall influence on the model's predictions."
    )

    with st.expander(
        "View Top SHAP Features"
    ):

        feature_table = (
            top_features
            .copy()
            .reset_index(drop=True)
        )

        feature_table.index = (
            feature_table.index + 1
        )

        feature_table.columns = [
            "Feature",
            "Mean |SHAP Value|"
        ]

        st.dataframe(
            feature_table,
            use_container_width=True
        )

    st.divider()

    st.subheader(
        "Individual Customer Explanation"
    )

    st.write(
        f"Showing why customer **{selected_customer}** "
        f"received a churn probability of "
        f"**{prediction_probability:.1%}**."
    )

    try:

        explainer = shap.TreeExplainer(
            model
        )

        customer_shap = explainer(
            customer
        )

    except Exception as e:

        st.error(
            "Unable to generate the SHAP explanation."
        )

        st.exception(e)

        return

    shap_array = np.asarray(
        customer_shap.values
    )

    if shap_array.ndim == 3:

        # SHAP 0.52:
        # 1 × 42 × 2

        customer_shap_values = (
            shap_array[0, :, 1]
        )

        expected_values = np.asarray(
            explainer.expected_value
        )

        base_value = float(
            expected_values[1]
        )

    elif shap_array.ndim == 2:

        # 1 × 42

        customer_shap_values = (
            shap_array[0]
        )

        expected_values = np.asarray(
            explainer.expected_value
        )

        base_value = float(
            expected_values.flat[0]
        )

    else:

        st.error(
            f"Unexpected SHAP shape: "
            f"{shap_array.shape}"
        )

        return

    waterfall_explanation = shap.Explanation(
        values=customer_shap_values,
        base_values=base_value,
        data=customer.iloc[0].values,
        feature_names=feature_names
    )

    shap.plots.waterfall(
        waterfall_explanation,
        max_display=12,
        show=False
    )

    st.pyplot(
        plt.gcf(),
        use_container_width=True
    )

    plt.close()

    with st.expander(
        " How to Interpret the SHAP Explanation",
        expanded=True
    ):

        st.markdown(
            """
            ### Understanding the SHAP Waterfall

            **🔴 Red features**

            Push the customer's prediction toward **higher churn
            probability**.

            **🔵 Blue features**

            Push the customer's prediction toward **lower churn
            probability**.

            **📏 Larger bars**

            Represent stronger influence on the model's prediction.

            The waterfall combines the individual feature contributions
            to explain the final churn prediction for the selected
            customer.
            """
        )

    with st.expander(
        " Customer Behaviour Context"
    ):

        context_columns = [
            "Tenure",
            "OrderCount",
            "CashbackAmount",
            "AverageSpendPerOrder",
            "EngagementScore",
            "DaySinceLastOrder",
            "Complain",
            "SatisfactionScore"
        ]

        available_context = [
            col
            for col in context_columns
            if col in original_customer.index
        ]

        context_df = (
            original_customer[
                available_context
            ]
            .to_frame()
            .T
        )

        st.dataframe(
            context_df,
            use_container_width=True,
            hide_index=True
        )

    with st.expander(
        "Business Insight",
        expanded=True
    ):

        st.markdown(
            """
            SHAP explainability helps retention teams understand
            **why** a customer has been identified as a potential
            churn risk.

            Instead of treating the Random Forest as a black box,
            SHAP identifies the customer characteristics that
            contributed to the prediction.

            This information can support more targeted retention
            strategies and help teams understand the behavioural
            factors associated with individual predictions.
            """
        )

    with st.expander(
        " Explainability Methodology"
    ):

        st.markdown(
            """
            **Model:** Random Forest

            **Explainability technique:** SHAP TreeExplainer

            **Global explanation:** Mean absolute SHAP values
            calculated across the complete customer dataset.

            **Local explanation:** SHAP waterfall calculated only
            for the selected customer.

            The global explanation identifies features with the
            greatest overall influence, while the local explanation
            shows how individual features contribute to a specific
            customer's prediction.
            """
        )

    st.markdown("---")
    st.caption(
        "Retenexa  |  Explainable AI  |  Random Forest + SHAP"
    )