# Feature Engineering

## New Features Created

### AverageSpendPerOrder
Estimates the average customer value per order using the customer's cashback amount and order count.
## Output

The engineered customer dataset was saved as:
`data/features/customer_features.csv`

### EngagementScore
Combines app usage, coupons used, and order count to estimate customer engagement.

### LoyaltyLevel
Categorizes customers into New, Regular, Loyal, and VIP based on tenure.

### HighValueCustomer
Identifies customers with cashback above the median.

### CustomerActivity
Represents overall shopping activity using order count and coupon usage.

### CashbackPerOrder
Measures cashback earned per order.