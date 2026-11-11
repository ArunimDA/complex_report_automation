import os
import psycopg2
import pandas as pd

DB_CONFIG = {
    "host": os.getenv("DB_HOST"),
    "port": int(os.getenv("DB_PORT", 5432)),
    "dbname": os.getenv("DB_NAME", "postgres"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD")
}

os.makedirs("output_reports", exist_ok=True)

print("Connecting to Supabase...")
conn = psycopg2.connect(**DB_CONFIG)

# Commercial Orders
df_com = pd.read_sql_query("SELECT * FROM amlan.ecommerce_com_orders;", conn)
com_path = "output_reports/COM_Report.xlsx"
df_com.to_excel(com_path, index=False)
print(f"Saved: {com_path}")

# Marketing Campaigns
df_mkt = pd.read_sql_query("SELECT * FROM amlan.ecommerce_mkt_campaigns;", conn)
mkt_path = "output_reports/MKT_Report.xlsx"
df_mkt.to_excel(mkt_path, index=False)
print(f"Saved: {mkt_path}")

conn.close()
print("All reports generated successfully!")
