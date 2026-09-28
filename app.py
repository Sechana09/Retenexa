import streamlit as st
from dashboard.utils import load_data
from dashboard.overview import show as overview
from dashboard.prediction import show as prediction
from dashboard.segmentation import show as segmentation
from dashboard.recommendations import show as recommendations
from dashboard.explainability import show as explainability


st.set_page_config(
    page_title="Retenexa | Customer Retention Analytics",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>

/* Main application background */
.stApp {
    background-color: var(--background-color);
}

/* Main content */
.main .block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
    max-width: 1400px;
}

section[data-testid="stSidebar"] {
    background-color: var(--secondary-background-color);
    border-right: 1px solid rgba(128, 128, 128, 0.20);
}

section[data-testid="stSidebar"] * {
    color: var(--text-color);
}

/* Sidebar divider */
section[data-testid="stSidebar"] hr {
    border-color: rgba(128, 128, 128, 0.25);
}

h1, h2, h3, h4, h5, h6 {
    color: var(--text-color);
}

p, label, span, div {
    color: inherit;
}

div[data-testid="stMetric"] {
    background-color: var(--secondary-background-color);
    border: 1px solid rgba(128, 128, 128, 0.20);
    border-radius: 14px;
    padding: 18px;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.06);
}

div[data-testid="stMetric"] label {
    color: var(--text-color) !important;
}

div[data-testid="stMetric"] [data-testid="stMetricValue"] {
    color: var(--text-color) !important;
}

div[data-baseweb="select"] > div {
    background-color: var(--secondary-background-color);
    color: var(--text-color);
    border-color: rgba(128, 128, 128, 0.25);
}

div[data-baseweb="select"] span {
    color: var(--text-color);
}

input,
textarea {
    background-color: var(--secondary-background-color) !important;
    color: var(--text-color) !important;
}

.stButton > button {
    border-radius: 8px;
    border: 1px solid rgba(128, 128, 128, 0.25);
    background-color: var(--secondary-background-color);
    color: var(--text-color);
    font-weight: 600;
}

.stButton > button:hover {
    border-color: var(--primary-color);
    color: var(--primary-color);
}

div[data-testid="stDataFrame"] {
    border-radius: 10px;
    overflow: hidden;
}

div[data-testid="stAlert"] {
    border-radius: 10px;
}

div[data-testid="stExpander"] {
    border: 1px solid rgba(128, 128, 128, 0.20);
    border-radius: 10px;
}


hr {
    border-color: rgba(128, 128, 128, 0.20);
}

</style>
""", unsafe_allow_html=True)

df = load_data()

# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.title("Retenexa")

    st.caption(
        "AI-powered customer churn prediction "
        "and retention analytics"
    )

    st.markdown("---")

    st.markdown("### Navigation")

    page = st.radio(
        "Navigation",
        [
            "Overview",
            "Prediction",
            "Segmentation",
            "AI Retention",
            "Explainability"
        ],
        label_visibility="collapsed"
    )

    st.markdown("---")

    st.markdown("### Model")

    st.info(
        """
        **Random Forest**

        **Accuracy:** 98%

        **Customers:** 5,630
        """
    )

    st.markdown("---")

    st.caption(
        "Retenexa · Customer Intelligence Platform"
    )

# PAGE ROUTING

if page == "Overview":
    overview(df)

elif page == "Prediction":
    prediction(df)

elif page == "Segmentation":
    segmentation(df)

elif page == "AI Retention":
    recommendations(df)

elif page == "Explainability":
    explainability(df)