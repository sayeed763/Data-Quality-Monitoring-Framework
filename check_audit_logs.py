import pandas as pd
from sqlalchemy import create_engine, text

# Database Config
DB_USER = "postgres"
DB_PASSWORD = "SayeedProject2026"
DB_HOST = "crypto-db.c6lgk8qqkp23.us-east-1.rds.amazonaws.com"
DB_PORT = "5432"
DB_NAME = "postgres"

engine = create_engine(f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}", 
                       connect_args={'sslmode': 'require'})

def view_logs():
    query = "SELECT * FROM etl_audit_logs ORDER BY start_time DESC LIMIT 5;"
    df = pd.read_sql(query, engine)
    
    print("\n📜 --- RECENT ETL AUDIT LOGS --- 📜")
    if df.empty:
        print("No logs found.")
    else:
        print(df.to_string(index=False))
    print("-----------------------------------\n")

if __name__ == "__main__":
    view_logs()
