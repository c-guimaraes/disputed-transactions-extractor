import pandas as pd

def zeus_to_pandas(sql: str) -> pd.DataFrame:
    """
    Executes a SQL query using the Zeus connection and returns the result as a pandas DataFrame.
    """
    z = zeus()  # Assumes a zeus() connection object is available in the environment
    cur = z.cursor
    cur.execute(sql)
    
    df = pd.DataFrame(
        data=cur.fetchall(),
        columns=[x[0] for x in cur.description]
    )
    return df

# Example query - Replace placeholders with actual values
query = '''

SELECT 
    transactions_type,
    created_date,
    ea_description,
    amount_real,
    fee,
    currency,
    amount_gbp,
    transactions_state,
    transactions_source,
    ea_card_id,
    ea_digitized_card_id,
    ea_merchant_name,
    ea_cardholderpresence,
    ea_reason_code,
    ea_reason,
    ea_passed_3ds,
    ea_sca_exemption,
    ea_digital_wallet_provider,
    ea_user_comments
FROM 
    core.transactions_b
WHERE 
    owner_id = 'xxxxxxxxxxxx'  -- Replace with actual user ID
    AND created_date >= (TIMESTAMP 'yyyy-mm-dd')  -- Start date
    AND created_date <= (TIMESTAMP 'yyyy-mm-dd')  -- End date
ORDER BY 
    created_date ASC

'''

# Export to CSV
df = zeus_to_pandas(query)
df.to_csv('Transactions.csv', index=False, header=True)
