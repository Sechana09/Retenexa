import pandas as pd
import joblib

def load_data():
    return pd.read_csv(
        "data/features/customer_retention_recommendations.csv"
    )

def load_model():
    model = joblib.load(
        "artifacts/churn_model.pkl"
    )

    feature_names = joblib.load(
        "artifacts/feature_names.pkl"
    )
    return model, feature_names