import pandas as pd
import random
from sqlalchemy import create_engine

def generate_and_insert_data():
    print("Generating 500 rows of customer data...")

    customers_data = []
    usage_data = []
    
    for i in range(1, 501):
        customer_id = f"CUST_{i:04d}"
        tenure = random.randint(1, 72)
        charges = round(random.uniform(15.0, 120.0), 2)
        tickets = random.randint(0, 10)
        last_login = random.randint(1, 60)

        if tickets >= 5 and last_login > 14:
            churned = 1
        
        elif tenure < 6 and charges >90.0:
            churned = random.choices([0, 1], weights=[0.4, 0.6])[0]

        else: 
            churned = random.choices([0, 1], weights=[0.9, 0.1])[0]

        account_status = 'active' if churned == 0 else 'cancelled'

        #appends to lists
        customers_data.append([customer_id, tenure, charges, account_status, churned])
        usage_data.append([customer_id, tickets, last_login])

    df_customers = pd.DataFrame(customers_data, columns=['customer_id', 'tenure_months', 'monthly_charges', 'account_status', 'churned'])
    df_usage = pd.DataFrame(usage_data, columns=['customer_id', 'total_support_tickets', 'days_since_last_login'])

    db_url = "mysql+pymysql://root:<password>@localhost:3306/customer_churn_db"

    try:
        engine = create_engine(db_url)
        df_customers.to_sql('customers', con=engine, if_exists='append', index=False)
        df_usage.to_sql('usage_stats', con=engine, if_exists='append', index=False)
        
        print("Successfully inserted 500 rows into MySQL!")

    except Exception as e:
        print(f"Database connection failed: {e}")

if __name__ == "__main__":
    generate_and_insert_data()