import pandas as pd
from sqlalchemy import create_engine, text
import datetime

# Database Config
DB_USER = "postgres"
DB_PASSWORD = "YOUR_DB_PASSWORD"
DB_HOST = "your-db-instance.aws.com"
DB_PORT = "5432"
DB_NAME = "postgres"

engine = create_engine(f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}", 
                       connect_args={'sslmode': 'require'})

def log_to_audit(job_name, status, rows, error=""):
    """Writes the result of the run to the RDS Audit Table"""
    query = text("""
        INSERT INTO etl_audit_logs (job_name, status, rows_processed, error_message)
        VALUES (:name, :status, :rows, :err)
    """)
    with engine.connect() as conn:
        conn.execute(query, {"name": job_name, "status": status, "rows": rows, "err": error})
        conn.commit()

def run_pipeline():
    job_name = "crypto_load_v1"
    try:
        # 1. READ & VALIDATE
        df = pd.read_csv("crypto_silver_cleaned.csv")
        
        # DATA QUALITY CHECK: Price must be > 0
        if (df['current_price'] <= 0).any():
            raise ValueError("Data Quality Failed: Negative or Zero price detected!")
        
        # 2. LOAD TO RDS
        print(f"🚀 Quality checks passed. Pushing {len(df)} rows...")
        df.to_sql('crypto_prices', engine, if_exists='append', index=False)
        
        # 3. LOG SUCCESS
        log_to_audit(job_name, "SUCCESS", len(df))
        print("✅ Pipeline run logged as SUCCESS in audit table.")

    except Exception as e:
        # 4. LOG FAILURE
        print(f"❌ Pipeline failed: {e}")
        log_to_audit(job_name, "FAILED", 0, str(e))

if __name__ == "__main__":
    run_pipeline()
