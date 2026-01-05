# 🛡️ Project 3: Data Quality & Monitoring Framework

This project enhances the existing Crypto ETL pipeline by adding a robust **Observability and Data Quality Layer**. It ensures that only validated data enters the production database and provides real-time visibility into pipeline health.

## 🌟 Overview
In production environments, pipelines often fail due to bad data or API changes. Project 3 solves this by implementing "Quality Gates" and a custom monitoring dashboard to track every run in **AWS RDS**.



## 🛠️ Key Features
- **Data Quality Gates:** Automated validation checks using Python/Pandas to catch anomalies (e.g., negative prices, null values) before ingestion.
- **Audit Logging Framework:** A custom metadata table (`etl_audit_logs`) in PostgreSQL that tracks:
    - **Run Status:** (SUCCESS/FAILED)
    - **Rows Processed:** Total records moved.
    - **Error Tracebacks:** Detailed logs for rapid debugging if a run fails.
- **Observability Dashboard:** A live **Streamlit** UI for stakeholders to monitor market trends and pipeline performance at a glance.

## 📊 Monitoring Dashboard
![Pipeline Dashboard](monitoring_dashboard.png)
*Above: Screenshot of the live dashboard showing 100% Success Rate and data directly from the Gold layer.*

## 📂 Project 3 Components
- **`master_etl_pipeline.py`**: The primary engine with integrated validation logic and logging.
- **`dashboard.py`**: The UI code for the monitoring dashboard.
- **`create_audit_table.py`**: Infrastructure script to initialize the metadata logging system.
- **`check_audit_logs.py`**: Developer utility to verify run history via terminal.

## 🚀 Technical Implementation
1. **Validation:** Applied logic to ensure `current_price` is always positive and schema types match.
2. **Metadata Capture:** Utilized `SQLAlchemy` to insert run results into the audit table at the end of every execution.
3. **Frontend:** Developed a Streamlit app to query the RDS audit logs and render real-time KPIs (Success Rate, Last Run Status).

---
**Tech Stack:** Python, Pandas, SQLAlchemy, PostgreSQL (AWS RDS), Streamlit.
