# Churn Prediction Model Training

## Objective

The objective of this module is to develop a machine learning model capable of predicting whether a customer is likely to churn.
Multiple classification algorithms were trained and evaluated to identify the model that provides the best overall performance for customer churn prediction.


## Dataset

The model was trained using the engineered customer dataset containing customer behavioral, transactional, satisfaction, and derived features.
The target variable is:

Churn

Where:

- 0 = Customer retained
- 1 = Customer churned


## Feature Preparation

Before model training:

- Categorical variables were encoded using One-Hot Encoding.
- Numerical features were standardized where required.
- Engineered customer features were included.
- The target variable was separated from the input features.
- The dataset was divided into training and testing sets.

The final model feature set contained 42 features.


## Models Evaluated

Four classification algorithms were trained:

1. Logistic Regression
2. Decision Tree
3. Random Forest
4. Gradient Boosting

These models were selected to compare a simple linear classification approach with tree-based ensemble methods.


## Model Evaluation

The models were evaluated using:

- Accuracy
- Precision
- Recall
- F1 Score
- ROC-AUC

These metrics provide a more complete evaluation than accuracy alone, particularly because the dataset contains fewer churned customers than retained customers.


## Model Performance

| Model | Accuracy | Precision | Recall | F1 Score | ROC-AUC |
|---|---:|---:|---:|---:|---:|
| Logistic Regression | 80.02% | 45.01% | 83.16% | 58.41% | 89.30% |
| Decision Tree | 96.54% | 88.72% | 91.05% | 89.87% | 94.35% |
| **Random Forest** | **98.14%** | **92.89%** | **96.32%** | **94.57%** | **99.83%** |
| Gradient Boosting | 91.83% | 83.11% | 64.74% | 72.78% | 94.01% |


## Model Selection

The Random Forest classifier was selected as the final churn prediction model.

It achieved the strongest overall performance across the evaluation metrics.

### Random Forest Performance

- Accuracy: 98.14%
- Precision: 92.89%
- Recall: 96.32%
- F1 Score: 94.57%
- ROC-AUC: 99.83%

The high recall is particularly valuable for customer retention because it indicates that the model identifies a large proportion of customers who are actually at risk of churn.

The strong precision also helps reduce the number of retained customers incorrectly targeted as churn risks.


## Final Model

The trained Random Forest model was saved as:
`artifacts/churn_model.pkl`

The corresponding feature names were saved as:
`artifacts/feature_names.pkl`

The scaler used during preprocessing was saved as:
`artifacts/scaler.pkl`


## Business Interpretation

The selected model can be used to:

- Identify customers at risk of churn.
- Prioritize retention efforts.
- Estimate individual churn probability.
- Support targeted retention campaigns.
- Provide inputs to the AI Retention Recommendation System.

The model predictions are subsequently combined with customer behavior and segmentation information to generate personalized retention strategies.


## Integration with Explainable AI

The Random Forest model is further analyzed using SHAP.

SHAP provides:

- Global feature importance.
- Individual customer explanations.
- Feature-level contribution to churn predictions.

This allows the final system to provide not only a churn prediction but also an explanation for that prediction.


## Conclusion

Multiple machine learning algorithms were evaluated for customer churn prediction.

Random Forest achieved the strongest overall performance and was selected as the final model.

The trained model forms the core predictive component of Retenexa and is integrated with customer segmentation, SHAP explainability, and AI-powered retention recommendations.