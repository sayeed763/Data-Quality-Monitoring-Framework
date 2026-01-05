import streamlit as st
import pandas as pd
from sqlalchemy import create_engine

# DB Connection
DB_USER = "postgres"
DB_PASSWORD = "YOUR_DB_PASSWORD"
DB_HOST = "your-db-instance.aws.com"
DB_PORT = "5432"
DB_NAME = "postgres"

engine = create_engine(f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}")

st.set_page_config(page_title="Crypto ETL Monitor", layout="wide")
st.title("📊 Crypto Pipeline Monitoring Dashboard")

# 1. Fetch Audit Logs
df_logs = pd.read_sql("SELECT * FROM etl_audit_logs ORDER BY start_time DESC", engine)

# 2. Key Metrics
col1, col2, col3 = st.columns(3)
total_runs = len(df_logs)
success_rate = (len(df_logs[df_logs['status'] == 'SUCCESS']) / total_runs * 100) if total_runs > 0 else 0

col1.metric("Total ETL Runs", total_runs)
col2.metric("Success Rate", f"{success_rate:.1f}%")
col3.metric("Last Run Status", df_logs['status'].iloc[0] if total_runs > 0 else "N/A")

# 3. Data Quality Alerts
st.subheader("🚨 Recent Audit Logs")
st.dataframe(df_logs, use_container_width=True)

# 4. Price Trends (Gold Layer Data)
st.subheader("💰 Current Market Prices (Live from RDS)")
df_prices = pd.read_sql("SELECT symbol, current_price, investment_tier FROM crypto_prices", engine)
st.bar_chart(df_prices.set_index('symbol')['current_price'])
