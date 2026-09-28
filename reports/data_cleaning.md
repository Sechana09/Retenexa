# Data Cleaning Decisions

## Missing Values

Numerical Columns
- Filled using Median

Reason:
Median is robust to skewed distributions.

Categorical Columns
- Filled using Mode

Reason:
Mode preserves the most common business category.

## Duplicate Records

Removed duplicate records if present.

## Outliers

Only visualized during cleaning.
No observations removed at this stage.

## Final Dataset Validation

After cleaning:

- Rows: 5630
- Columns: 20
- Missing values: 0
- Duplicate records: 0

The cleaned dataset was saved in:
`data/processed/`