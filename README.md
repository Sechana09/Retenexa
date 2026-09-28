# Retenexa

## AI-Powered Customer Churn Prediction & Retention Analytics

Retenexa is an end-to-end machine learning project designed to identify customers at risk of churn, understand the factors influencing their churn predictions, segment customers based on behavior, and generate actionable retention recommendations.

The project combines machine learning, customer segmentation, Explainable AI (SHAP), and a Streamlit dashboard into a single customer retention analytics system.


## Project Overview

Customer churn is an important business problem because losing existing customers can negatively affect revenue, customer lifetime value, and long-term business growth.

Retenexa addresses this problem through a complete analytics pipeline:

Raw Customer Data
        ↓
Data Understanding
        ↓
Data Cleaning
        ↓
Exploratory Data Analysis
        ↓
Feature Engineering
        ↓
Customer Segmentation
        ↓
Churn Prediction
        ↓
Model Explainability
        ↓
Retention Recommendation Engine
        ↓
Streamlit Dashboard

The system combines predictive modeling with customer behavioral analysis to provide both churn risk predictions and customer-specific retention insights.


## Key Features

1.Customer churn prediction using machine learning
2.Comparison of multiple classification models
3.Random Forest-based churn prediction
4.Customer risk classification
5.Customer behavioral segmentation using K-Means clustering
6.Feature engineering from customer transaction and engagement data
7.Global and individual prediction explainability using SHAP
8.Personalized retention recommendations based on churn risk and customer behavior
9.Interactive Streamlit dashboard
10.Customer-level prediction and analysis
11.Segment-level customer insights
12.High-risk customer identification
13.Retention action planning


## Dataset

The project uses an e-commerce customer churn dataset containing **5,630 customer records** and **20 original features**.

The dataset contains customer information related to:

1.Customer tenure
2.Login preferences
3.City tier
4.Warehouse distance
5.Payment preferences
6.Gender
7.App usage
8.Registered devices
9.Preferred order category
10.Satisfaction
11.Marital status
12.Number of addresses
13.Complaints
14.Order amount changes
15.Coupon usage
16.Order count
17.Days since last order
18.Cashback

### Target Variable

The target variable is:
Churn

where:

 `1` = Customer churned
 `0` = Customer retained


## Data Preparation

The data preparation process includes:

1.Checking dataset structure and data types
2.Identifying missing values
3.Handling numerical missing values using median imputation
4.Handling categorical missing values using mode imputation
5.Checking and removing duplicate records where applicable
6.Reviewing potential outliers
7.Preparing the dataset for machine learning and segmentation

Outliers were analyzed during the data exploration process rather than being automatically removed.


## Exploratory Data Analysis

Exploratory Data Analysis was performed to understand:

1.Customer churn distribution
2.Customer tenure
3.Order behavior
4.Cashback patterns
5.Customer satisfaction
6.Complaints
7.Customer engagement
8.Behavioral differences between retained and churned customers

The analysis was used to identify patterns that could contribute to customer churn and to guide subsequent feature engineering and modeling.


## Feature Engineering

Several additional features were created to better represent customer behavior.

### Engineered Features

| Feature                | Description                                      |
| ---------------------- | ------------------------------------------------ |
| `AverageSpendPerOrder` | Average spending associated with customer orders |
| `EngagementScore`      | Combined measure of customer engagement          |
| `LoyaltyLevel`         | Categorization of customer loyalty               |
| `HighValueCustomer`    | Identifies customers with higher-value behavior  |
| `CustomerActivity`     | Represents customer activity level               |
| `CashbackPerOrder`     | Cashback relative to customer order activity     |

These features provide additional behavioral information beyond the original dataset variables.


## Customer Segmentation

Customer segmentation was performed using K-Means clustering.

The segmentation workflow included:

1.Selecting relevant customer behavioral features
2.Encoding categorical variables
3.Standardizing features using `StandardScaler`
4.Evaluating cluster configurations
5.Using the elbow method and silhouette analysis
6.Selecting five customer segments
7.Profiling each resulting segment

### Customer Segments

The five resulting behavioral segments are:

| Cluster | Segment           |
| ------- | ----------------- |
| 0       | New Customers     |
| 1       | Loyal Customers   |
| 2       | Occasional Buyers |
| 3       | Premium Customers |
| 4       | Regular Customers |

These segments allow the retention system to consider customer behavior in addition to individual churn probability.


## Churn Prediction

Multiple machine learning classification models were evaluated:

Logistic Regression
Decision Tree
Random Forest
Gradient Boosting

### Model Comparison

| Model               | Accuracy | Precision | Recall | F1 Score | ROC-AUC |
| ------------------- | -------: | --------: | -----: | -------: | ------: |
| Logistic Regression |   80.02% |    45.01% | 83.16% |   58.41% |  89.30% |
| Decision Tree       |   96.54% |    88.72% | 91.05% |   89.87% |  94.35% |
| Random Forest       |   98.14% |    92.89% | 96.32% |   94.57% |  99.83% |
| Gradient Boosting   |   91.83% |    83.11% | 64.74% |   72.78% |  94.01% |

Random Forest was selected as the final prediction model based on the evaluation results.

### Final Random Forest Performance

The Random Forest model achieved:

 **Accuracy:** 98.14%
 **Precision:** 92.89%
 **Recall:** 96.32%
 **F1 Score:** 94.57%
 **ROC-AUC:** 99.83%

The classification report on the test set showed strong performance for both retained and churned customers.


## Churn Risk Classification

Retenexa converts predicted churn probabilities into three risk levels:

| Risk Level | Churn Probability |
| ---------- | ----------------- |
| High       | ≥ 70%             |
| Medium     | 40% – 69%         |
| Low        | < 40%             |

This allows the prediction results to be translated into easier-to-understand business categories.


## Model Explainability

Retenexa uses SHAP (SHapley Additive exPlanations) to explain the Random Forest predictions.

Explainability is implemented at two levels:

### Global Explainability

Global SHAP analysis identifies the features that have the greatest overall influence on churn predictions across the customer dataset.

Important features include:

1.Tenure
2.Cashback Amount
3.Loyalty Level
4.Complaints
5.Average Spend Per Order
6.Cashback Per Order
7.Warehouse-to-Home Distance
8.Days Since Last Order
9.Number of Addresses
10.Order Amount Increase from Previous Year

### Individual Explainability

For an individual customer, Retenexa calculates local SHAP values to show:

1.Which features increase churn risk
2.Which features decrease churn risk
3.The relative influence of individual features
4.The customer's predicted churn probability

This makes the model's predictions more interpretable rather than treating the model as a black box.


## Retention Recommendation Engine

Retenexa includes a customer retention recommendation engine that converts churn predictions and customer behavior into actionable retention suggestions.

The recommendation engine considers factors such as:

Churn probability
Customer tenure
Complaints
Order activity
Cashback behavior
Loyalty level
Customer engagement

Recommendations are generated using rule-based business logic informed by the machine learning predictions and customer behavioral features.

The system produces:

Customer ID
Churn Probability
Risk Level
Personalized Retention Recommendation

This allows predicted churn risk to be connected to potential retention actions.


## Streamlit Dashboard

Retenexa provides an interactive Streamlit dashboard with five main sections.

### Overview

Provides a high-level view of:

1.Total customers
2.Churned customers
3.Retention rate
4.Average tenure
5.Customer distribution
6.Churn risk distribution
7.Customer metrics
8.High-risk customers

### Prediction

Allows users to search for and analyze individual customers.
The page provides:

1.Churn probability
2.Risk level
3.Customer status
4.Customer profile
5.Behavioral metrics
6.Retention recommendation
7.Business insight

### Segmentation

Provides customer segment analysis using the K-Means clustering results.
Users can explore:

Segment distribution
Segment characteristics
Segment-level KPIs
Customer examples
Business insights

### AI Retention

Provides a retention action center containing:
1.High, medium, and low-risk customer counts
2.Risk filtering
3.Retention recommendations
4.Segment-level risk analysis
5.Retention planning
6.Exportable retention data

### Explainability

Provides:

1.Global SHAP feature importance
2.Feature-level influence
3.Individual customer explanations
4.SHAP waterfall visualization
5.Customer behavioral context


## Project Structure

Retenexa/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── features/
│
├── artifacts/
│   ├── churn_model.pkl
│   ├── feature_names.pkl
│   ├── scaler.pkl
│   └── shap_global_importance.csv
│
├── notebooks/
│   ├── 01_Data_Understanding.ipynb
│   ├── 02_Data_Cleaning.ipynb
│   ├── 03_EDA.ipynb
│   ├── 04_Feature_Engineering.ipynb
│   ├── 05_Customer_Segmentation.ipynb
│   ├── 06_Model_Training.ipynb
│   ├── 07_Model_Explainability.ipynb
│   └── 08_AI_Retention_Recommendation.ipynb
│
├── dashboard/
│   ├── utils.py
│   ├── overview.py
│   ├── prediction.py
│   ├── segmentation.py
│   ├── recommendations.py
│   └── explainability.py
│
└── reports/
    ├── ai_retention_system.md
    ├── customer_segmentation.md
    ├── data_cleaning.md
    ├── eda_insights.md
    ├── feature_engineering.md
    ├── model_explainability.md
    └── model_training.md


## Technology Stack

### Programming

Python

### Data Processing

Pandas
NumPy

### Machine Learning

Scikit-learn
Random Forest
Logistic Regression
Decision Tree
Gradient Boosting
K-Means Clustering

### Explainable AI

SHAP

### Visualization

Matplotlib
Seaborn

### Dashboard

Streamlit

### Data & Model Storage

CSV
Excel
Joblib


## How to Run

### 1. Clone the Repository

git clone <your-repository-url>
cd Retenexa


### 2. Create and Activate the Virtual Environment

Windows:

python -m venv venv
venv\Scripts\activate


### 3. Install Dependencies

pip install -r requirements.txt


### 4. Run the Streamlit Dashboard

python -m streamlit run app.py

The dashboard will open in your browser.


## Project Workflow

The complete Retenexa workflow can be summarized as:

Customer Data
     │
     ▼
Data Understanding
     │
     ▼
Data Cleaning
     │
     ▼
EDA
     │
     ▼
Feature Engineering
     │
     ├───────────────┐
     ▼               ▼
Segmentation    Churn Modeling
     │               │
     │               ▼
     │        Model Explainability
     │               │
     └───────┬───────┘
             ▼
Retention Recommendation Engine
             │
             ▼
      Streamlit Dashboard


## Results

Retenexa demonstrates an end-to-end customer retention analytics workflow combining:

1.Predictive machine learning
2.Customer behavioral segmentation
3.Explainable AI
4.Risk classification
5.Retention recommendations
6.Interactive business analytics

The final Random Forest model achieved 98.14% accuracy and 99.83% ROC-AUC on the evaluated test dataset.

The system also provides customer-level explanations and retention recommendations, allowing churn predictions to be connected with customer behavior and potential retention actions.

## Future Improvements

Potential future improvements include:

1.Integration with a real-time customer database
2.Automated model retraining
3.Real-time churn monitoring
4.Time-series customer behavior analysis
5.A/B testing of retention strategies
6.Customer lifetime value prediction
7.Automated campaign integration
8.Advanced recommendation models
9.Deployment to a cloud platform
10.Monitoring model performance after deployment


## Author

Sechana Venkatesh
Computer Science and Engineering

Interested in:

Data Analytics
Artificial Intelligence
Machine Learning
Cloud Computing
Data Science


## License

This project is intended for educational, portfolio, and demonstration purposes.