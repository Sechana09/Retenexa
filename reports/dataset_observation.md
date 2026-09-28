# Dataset Understanding

## Dataset Overview

- Dataset Name: E-Commerce Customer Churn Dataset
- Source: Kaggle
- File Format: Excel (.xlsx)
- Number of Rows: 5630
- Number of Columns: 20
- Target Variable: Churn


## Feature Types

### Numerical Features
- CustomerID
- Tenure
- WarehouseToHome
- HourSpendOnApp
- NumberOfDeviceRegistered
- SatisfactionScore
- NumberOfAddress
- OrderAmountHikeFromlastYear
- CouponUsed
- OrderCount
- DaySinceLastOrder
- CashbackAmount

### Categorical Features
- PreferredLoginDevice
- CityTier
- PreferredPaymentMode
- Gender
- PreferedOrderCat
- MaritalStatus
- Complain
- Churn


## Missing Values

Some numerical features contained missing values in the raw dataset. During data cleaning, all missing values were handled using median imputation for numerical features and mode imputation for categorical features.



## Duplicate Records

No duplicate records were found in the dataset.


## Target Variable

The target variable is Churn, where:
- 1 = Customer has churned
- 0 = Customer is retained


## Initial Observations

- Dataset contains customer demographics and behavioral information.
- Features include customer satisfaction, complaints, order history, payment preferences, cashback, and tenure.
- The dataset is suitable for customer churn prediction, segmentation, and retention analysis.
- After preprocessing, the dataset contains no missing values or duplicate records.