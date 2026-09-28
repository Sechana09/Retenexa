# Exploratory Data Analysis

## Objective

The objective of Exploratory Data Analysis (EDA) is to understand customer behavior, identify important patterns in the dataset, and analyze factors that may be associated with customer churn.

EDA was performed before feature engineering and model training to understand the distribution of customer attributes and identify potential relationships between customer behavior and churn.


## Dataset Overview

The dataset contains:

- 5,630 customers
- 20 original features
- Target variable: Churn

The dataset contains customer demographic, behavioral, transactional, and satisfaction-related information.


## Churn Distribution

The target variable contains two classes:

| Churn | Customers |
|-------|-----------|
| 0 | 4,682 |
| 1 | 948 |

Where:

- 0 = Customer retained
- 1 = Customer churned

The dataset therefore contains more retained customers than churned customers, indicating a moderate class imbalance.

The churn rate is approximately 16.8%.

This imbalance was considered during model evaluation, with metrics such as Precision, Recall, F1 Score, and ROC-AUC used alongside accuracy.


## Complaint Analysis

The Complain feature contains:

| Complain | Customers |
|----------|-----------|
| 0 | 4,026 |
| 1 | 1,604 |

Customers with complaints represent a significant portion of the customer base.

Complaint behavior was therefore considered an important potential indicator of customer dissatisfaction and churn.


## Customer Tenure

Tenure represents the length of the customer's relationship with the company.
The analysis indicates that customer tenure varies considerably across the customer base.

Tenure was later identified as one of the most influential features in the Random Forest model and SHAP analysis.

This suggests that the length of the customer relationship plays an important role in churn prediction.


## Order and Engagement Behavior

Several features describe customer purchasing and engagement:

- OrderCount
- CouponUsed
- HourSpendOnApp
- NumberOfDeviceRegistered
- DaySinceLastOrder
- CashbackAmount

These features provide information about customer activity, purchase frequency, digital engagement, and recency.

Customers with lower activity or longer periods since their last order may require greater attention from retention teams.


## Satisfaction and Complaints

The dataset contains:

- SatisfactionScore
- Complain

These features provide insight into customer experience.

Customers experiencing dissatisfaction or submitting complaints may represent potential retention opportunities.


## Cashback and Customer Value

CashbackAmount provides an indication of the value generated through customer transactions and rewards.

Cashback-related features were later found to have substantial influence on churn predictions.

This suggests that customer value and reward behavior can play an important role in retention analysis.


## Categorical Feature Analysis

Categorical variables were explored to understand differences in customer behavior across groups.

Important categorical attributes include:

- PreferredLoginDevice
- PreferredPaymentMode
- Gender
- PreferedOrderCat
- MaritalStatus
- CityTier

These variables help provide additional context about customer preferences and behavior.


## Key EDA Findings

The main observations from the analysis were:

1. The majority of customers are retained, while approximately 16.8% have churned.

2. Customer tenure appears to be an important indicator of customer retention.

3. Complaint behavior is potentially associated with customer dissatisfaction and churn risk.

4. Order frequency and recent purchasing activity provide useful information about customer engagement.

5. Cashback amount provides an indication of customer value and was later found to be an important predictive feature.

6. Customer satisfaction and behavioral features provide useful signals for identifying potential churn.

7. The dataset contains a combination of demographic, behavioral, transactional, and satisfaction-related information, making it suitable for both churn prediction and customer segmentation.


## Business Insights

The EDA suggests several areas where businesses can focus their retention efforts:

- Monitor customers with complaints.
- Re-engage customers with declining purchase activity.
- Monitor customers with long periods since their last order.
- Maintain engagement with long-term customers.
- Use cashback and loyalty programs strategically.
- Identify dissatisfied customers before they churn.


## Relationship to Machine Learning

The findings from EDA were used to guide the subsequent stages of the project.

Important behavioral variables were retained for feature engineering and model development.

EDA also helped identify variables that could be transformed into meaningful customer-level features such as:

- AverageSpendPerOrder
- EngagementScore
- LoyaltyLevel
- HighValueCustomer
- CustomerActivity
- CashbackPerOrder


## Conclusion

Exploratory Data Analysis provided an understanding of the customer population and identified behavioral characteristics that may influence churn.
The findings were used to guide feature engineering, customer segmentation, churn prediction, and retention recommendation development.