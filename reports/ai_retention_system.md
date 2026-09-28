# Retenexa
## AI Retention Recommendation System

## Objective

The objective of this module is to transform machine learning churn predictions into actionable and personalized customer retention strategies.
The system combines predicted churn probability with customer behavioral characteristics to identify customer risk levels and recommend appropriate retention actions.

## Workflow

The retention recommendation pipeline follows these steps:

1. Load the trained Random Forest churn prediction model.
2. Load the engineered customer dataset.
3. Prepare the customer features for prediction.
4. Predict churn probability for each customer.
5. Categorize customers into risk levels.
6. Analyze customer behavioral characteristics.
7. Generate personalized retention recommendations.
8. Save the final recommendation dataset.

## Risk Levels

Customers are categorized according to their predicted
churn probability.

| Risk Level | Churn Probability |
|------------|-------------------|
| High | ≥ 70% |
| Medium | 40% – 69% |
| Low | < 40% |

These risk categories help retention teams prioritize customers according to their likelihood of churn.


## Recommendation Logic

The recommendation engine considers multiple customer characteristics, including:

- Customer tenure
- Complaint history
- Order count
- Cashback amount
- Churn probability
- Customer activity
- Loyalty characteristics

Recommendations are generated based on the customer's risk level and behavioral characteristics.


## Example Recommendations

### High-Risk Customers

Potential actions include:

- Resolve customer complaints through proactive support.
- Launch targeted retention campaigns.
- Provide personalized incentives.
- Offer cashback or loyalty rewards.
- Encourage repeat purchases.

### Medium-Risk Customers

Potential actions include:

- Provide targeted discounts.
- Recommend relevant products.
- Encourage repeat purchases.
- Increase customer engagement.
- Monitor changes in customer activity.

### Low-Risk Customers

Potential actions include:

- Continue loyalty engagement.
- Provide personalized product recommendations.
- Encourage repeat purchases.
- Maintain positive customer relationships.
- Offer loyalty benefits where appropriate.


## Output

The recommendation pipeline generates a customer-level dataset containing information such as:

- Customer ID
- Churn Probability
- Risk Level
- Personalized Retention Recommendation

The final dataset is saved as:

`data/features/customer_retention_recommendations.csv`


## Integration with Customer Segmentation

The retention recommendation system works alongside customer segmentation.

Customer segments provide behavioral context, while the churn model provides an estimate of churn risk.
Together, these components allow the system to support more targeted retention strategies.

For example:

| Customer Situation | Example Strategy |
|---|---|
| High churn risk | Immediate retention intervention |
| Medium churn risk | Engagement and targeted incentives |
| Low churn risk | Loyalty and relationship maintenance |
| Premium customer at risk | High-priority personalized intervention |
| Low-engagement customer | Re-engagement campaign |


## Business Benefits

The AI Retention Recommendation System helps businesses:

- Identify customers at high risk of churn.
- Prioritize retention efforts.
- Deliver personalized engagement strategies.
- Improve customer satisfaction.
- Support customer lifetime value.
- Reduce unnecessary retention spending.
- Support data-driven business decisions.


## System Integration

The recommendation dataset is integrated into the Retenexa Streamlit dashboard.

The dashboard allows users to explore customer information,risk levels, and recommended retention actions.


## Conclusion

The AI Retention Recommendation System bridges predictive analytics and business strategy by converting churn predictions into actionable customer retention recommendations.
This enables businesses to move from simply identifying customers who may churn to determining what action should be taken to retain them.