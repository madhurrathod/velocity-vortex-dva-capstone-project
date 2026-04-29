# Data Dictionary

## Dataset Summary

- Dataset name: UCI Bank Marketing (`bank-additional-full.csv`)
- Source: UCI Machine Learning Repository
- Sector: Finance
- Row count: 41,188
- Column count: 21 including the target column
- Unit of analysis: one customer contact record in a telemarketing campaign
- Target variable: `subscribed`

## Raw Columns

| Column Name | Type | Description |
| --- | --- | --- |
| age | numeric | Client age |
| job | categorical | Job category |
| marital | categorical | Marital status |
| education | categorical | Education level |
| default | categorical | Credit in default status |
| housing | categorical | Housing loan status |
| loan | categorical | Personal loan status |
| contact | categorical | Contact communication type |
| month | categorical | Last contact month |
| day_of_week | categorical | Last contact day of week |
| duration | numeric | Last contact duration in seconds |
| campaign | numeric | Number of contacts during current campaign |
| pdays | numeric | Days since last contact from previous campaign; `999` means not previously contacted |
| previous | numeric | Number of contacts before current campaign |
| poutcome | categorical | Outcome of previous campaign |
| emp.var.rate | numeric | Employment variation rate |
| cons.price.idx | numeric | Consumer price index |
| cons.conf.idx | numeric | Consumer confidence index |
| euribor3m | numeric | Euribor 3-month rate |
| nr.employed | numeric | Number of employees indicator |
| y | binary | Whether the client subscribed to a term deposit |

## Derived Columns in Cleaned Data

| Column Name | Type | Description |
| --- | --- | --- |
| subscribed_flag | binary | `1` if subscribed, else `0` |
| contacted_before | categorical | Whether the client was contacted in a previous campaign |
| pdays_clean | numeric | `pdays` with `999` converted to missing |
| month_name | categorical | Full month name for display |
| day_name | categorical | Full weekday name for display |
| age_group | categorical | Age band for segmentation |
| campaign_band | categorical | Bucketed contact count |
| duration_minutes | numeric | Call duration in minutes |
| previous_contact_band | categorical | Bucketed previous-contact count |
| month_order | numeric | Sorting field for dashboard month order |

## Cleaning Decisions

- Standardized column names to lowercase snake_case style where possible.
- Converted `"unknown"` values in selected categorical fields to missing values.
- Treated `pdays = 999` as “not previously contacted”.
- Added business-friendly labels and segmentation fields for Tableau.

## Data Quality Issues Present

- Missing categorical values encoded as `"unknown"`
- Sentinel value `999` in `pdays`
- Mixed analytical usefulness across raw fields, requiring derived segmentation columns
