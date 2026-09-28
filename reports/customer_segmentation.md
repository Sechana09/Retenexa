# Customer Segmentation

## Objective

The objective of this module is to segment customers into behavior-based groups using K-Means clustering.
Customer segmentation helps identify groups of customers with similar purchasing behavior, engagement levels, loyalty, and churn characteristics.


## Methodology

The following steps were used:

1. Select relevant customer features.
2. Encode categorical variables using One-Hot Encoding.
3. Standardize numerical features using StandardScaler.
4. Evaluate different cluster counts.
5. Select K = 5 for the final segmentation.
6. Apply K-Means clustering.
7. Analyze and profile the resulting customer segments.


## Selecting the Number of Clusters

The Elbow Method was used to evaluate different values of K.

The evaluated cluster counts ranged from:

K = 2 to K = 10

The final model used:

K = 5

The five-cluster solution provided a useful balance between cluster separation and business interpretability.


## Cluster Distribution

The final customer distribution was:

| Cluster | Customers |
|---------|-----------|
| 0 | 1211 |
| 1 | 840 |
| 2 | 837 |
| 3 | 627 |
| 4 | 2115 |

Total customers:
5630


# Customer Segments

## 1. New Customers

Cluster 0

Characteristics:

- Lower tenure
- Moderate engagement
- Relatively higher churn rate
- Lower order activity

### Business Strategy

- Provide onboarding support.
- Offer introductory promotions.
- Encourage second and repeat purchases.
- Improve early customer engagement.


## 2. Loyal Customers

Cluster 1

Characteristics:

- Higher tenure
- High order count
- Strong customer activity
- Lower churn rate

### Business Strategy

- Reward repeat purchases.
- Provide personalized offers.
- Introduce loyalty benefits.
- Encourage continued engagement.


## 3. Occasional Buyers

Cluster 2

Characteristics:

- Lower order activity
- Lower engagement
- Relatively higher churn rate
- Lower average customer activity

### Business Strategy

- Use re-engagement campaigns.
- Provide targeted discounts.
- Send personalized product recommendations.
- Encourage more frequent purchases.


## 4. Premium Customers

Cluster 3

Characteristics:

- Highest tenure
- Highest cashback amount
- Highest average spend per order
- Very low churn rate
- High-value customer characteristics

### Business Strategy

- Provide exclusive loyalty benefits.
- Offer premium customer support.
- Reward long-term loyalty.
- Protect these customers from churn.


## 5. Regular Customers

Cluster 4

Characteristics:

- Medium tenure
- Moderate engagement
- Stable purchasing behavior
- Large customer population

### Business Strategy

- Encourage repeat purchases.
- Use upselling and cross-selling.
- Provide personalized promotions.
- Gradually move customers toward higher-value segments.


## Business Value

Customer segmentation enables businesses to move beyond a single retention strategy.

Different customer groups can receive different strategies based on their behavior and value.

For example:

- New customers → onboarding and activation
- Loyal customers → loyalty rewards
- Occasional buyers → re-engagement
- Premium customers → VIP treatment
- Regular customers → upselling and cross-selling


## Output

The segmented customer dataset was saved as:
`data/features/customer_segments.csv`


## Conclusion

K-Means clustering successfully divided the 5,630 customers into five behavior-based segments.

The resulting segments provide a foundation for targeted customer engagement and retention strategies.