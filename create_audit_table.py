from sqlalchemy import create_engine, text

DB_USER = "postgres"
DB_PASSWORD = "SayeedProject2026" 
DB_HOST = "crypto-db.c6lgk8qqkp23.us-east-1.rds.amazonaws.com"
DB_PORT = "5432"
DB_NAME = "postgres"

engine = create_engine(f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}", 
                       connect_args={'sslmode': 'require'})

audit_table_query = """
CREATE TABLE IF NOT EXISTS etl_audit_logs (
    run_id SERIAL PRIMARY KEY,
    job_name VARCHAR(100),
    status VARCHAR(20),
    rows_processed INT,
    error_message TEXT,
    start_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
"""

with engine.connect() as conn:
    conn.execute(text(audit_table_query))
    conn.commit()
    print("✅ Audit table created! We can now track pipeline health.")
