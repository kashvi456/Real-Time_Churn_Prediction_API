import pandas as pd
from sqlalchemy import create_engine

def get_training_data():
    db_url = "mysql+pymysql://root:<password>@localhost:3306/customer_churn_db" 
    engine = create_engine(db_url)

    sql_query = """
        SELECT 
            c.customer_id,
            c.tenure_months,
            c.monthly_charges,
            s.total_support_tickets,
            s.days_since_last_login,
            c.churned
        FROM customers c
        LEFT JOIN usage_stats s ON c.customer_id = s.customer_id;
"""

    df = pd.read_sql(sql_query, engine)
    return df

if __name__ == "__main__":
    df = get_training_data()
    print(f"Extracted {len(df)} records successfully.\n")
    print("Here are the first 5 rows:")
    print(df.head())