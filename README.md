# Disputed Transactions Extractor

This script helps External Dispute Resolution (EDR) agents at Revolut quickly extract and analyse all relevant customer transactions in complex fraud-related cases. It retrieves not only 'completed' transactions but also those marked as 'declined', 'failed', and 'rejected', ensuring a full picture for investigation.

## 📌 Problem Statement

The standard Back Office export includes only completed transactions, requiring agents to manually retrieve other types. This was time-consuming and inefficient, especially for cases with 50+ disputed items.

## ✅ Solution

This script uses a SQL query to fetch all relevant transaction types over a selected date range, converting the results into a CSV file for analysis.

## 🛠 How to Use

1. Replace the placeholders in the `owner_id` and `created_date` fields of the query.
2. Run the script in an environment where the `zeus()` connection and `pandas` are available.
3. A `Transactions.csv` file will be generated in the local directory.

### Example
```sql
owner_id = '1234567890'
created_date >= '2024-12-01'
created_date <= '2024-12-31'
