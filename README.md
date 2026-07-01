# 🏦 Banking Fraud Transaction Processing Pipeline

[![Python](https://img.shields.io/badge/Python-3.12-blue.svg)]()
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16-blue.svg)]()
[![Apache Airflow](https://img.shields.io/badge/Apache%20Airflow-2.10-red.svg)]()
[![Apache Superset](https://img.shields.io/badge/Apache%20Superset-Latest-orange.svg)]()
[![Docker](https://img.shields.io/badge/Docker-Containerized-blue.svg)]()
[![Status](https://img.shields.io/badge/Status-Completed-success.svg)]()

An end-to-end **Banking Fraud Transaction Processing Pipeline** built using **Python, PostgreSQL, Docker, Apache Airflow, and Apache Superset**. The project simulates a real-world banking environment where millions of transactions are processed daily, validated, enriched with fraud intelligence, and made available for analytics and reporting.

---

# 📌 Business Problem

Banks receive transaction data from multiple channels:

* ATM Transactions
* Mobile Banking
* POS Systems
* Online Banking

Raw transaction data often contains:

* Duplicate records
* Missing values
* Invalid timestamps
* Inconsistent formats
* Suspicious or fraudulent activities

Fraud analysts and downstream systems require:

* Clean and validated datasets
* Fraud risk tagging
* Historical transaction storage
* Analytics-ready datasets
* Interactive dashboards

This project builds a complete data pipeline to address these challenges.

---

# 🏗️ Architecture

<img width="1536" height="1024" alt="architecture" src="https://github.com/user-attachments/assets/823dbc02-9ae5-44c2-86b7-6dc6502a545a" />


---

# 🚀 Features

### Data Ingestion

* Reads raw banking transaction files (CSV)
* Supports processing of large datasets (100K+ records)

### Data Validation

* Mandatory field checks
* Data type validation
* Currency validation
* Timestamp validation
* Account number validation

### Rejected Records Handling

* Invalid records are separated
* Stored for audit and debugging

### Deduplication

* Detect duplicate transactions
* Keep latest valid record
* Log duplicate counts

### Fraud Detection Engine

Implemented configurable rule-based fraud detection:

* High Amount Transactions
* Rapid Transactions
* Geographic Anomalies
* Night Transactions
* Fraud Scoring
* Risk Categorization

### Data Transformation

Creates derived features:

* fraud_score
* is_high_risk
* risk_category
* transaction_hour
* transaction_day
* amount_bucket
* processing_timestamp

### Storage

* PostgreSQL analytical tables
* Partitioned Parquet Data Lake storage

### Orchestration

* Apache Airflow DAG orchestration

### Visualization

* Interactive dashboards using Apache Superset

### Infrastructure

* Fully Dockerized environment

---

# 🛠️ Technology Stack

| Component                 | Technology              |
| ------------------------- | ----------------------- |
| Programming Language      | Python                  |
| Data Processing           | Pandas                  |
| Database                  | PostgreSQL              |
| Workflow Orchestration    | Apache Airflow          |
| Dashboarding              | Apache Superset         |
| Containerization          | Docker & Docker Compose |
| Storage Format            | CSV, Parquet            |
| Synthetic Data Generation | Faker                   |
| SQL Queries               | PostgreSQL              |

---

# 📂 Project Structure

```text
banking-fraud-pipeline/
│
├── airflow/
│   └── dags/
│       └── banking_fraud_pipeline.py
│
├── architecture/
│   └── architecture.png
│
├── config/
│   └── config.yaml
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── rejected/
│
├── etl/
│   ├── extract.py
│   ├── validate.py
│   ├── deduplicate.py
│   ├── fraud_rules.py
│   ├── transform.py
│   ├── load.py
│   ├── logger.py
│   └── paths.py
│
├── reports/
│
├── scripts/
│   └── generate_transactions.py
│
├── sql/
│   ├── schema.sql
│   └── analytics_queries.sql
│
├── tests/
│
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
├── main.py
└── README.md
```

---

# 🔄 End-to-End Pipeline Flow

```text
Raw Transaction Files
          ↓
      Extract Layer
          ↓
     Validation Layer
          ↓
     Deduplication Layer
          ↓
   Fraud Detection Engine
          ↓
   Transformation Layer
          ↓
   Curated Transactions
          ↓
 ┌───────────────────┐
 │   PostgreSQL DB   │
 └───────────────────┘
          ↓
 ┌───────────────────┐
 │ Parquet Data Lake │
 └───────────────────┘
          ↓
 Apache Superset Dashboards
```

---

# 🔍 Fraud Detection Rules

## Rule 1 – High Amount

```text
IF amount > threshold
THEN fraud_flag = HIGH_AMOUNT
```

---

## Rule 2 – Rapid Transactions

```text
More than N transactions
within M minutes
```

---

## Rule 3 – Geographic Anomaly

```text
Transactions from multiple
locations within a short duration
```

---

## Rule 4 – Night Transactions

```text
Transactions between
1:00 AM and 4:00 AM
```

---

# ⚙️ Config-Driven Rules

Fraud rules are configurable via:

```yaml
high_amount_threshold: 100000
rapid_txn_limit: 5
rapid_txn_window_minutes: 2
night_start_hour: 1
night_end_hour: 4
```

---

# 🗄️ PostgreSQL Tables

### clean_transactions

Curated and validated transactions.

### fraud_transactions

Contains only fraudulent transactions for fraud analytics.

---

# 🪣 Partitioned Parquet Storage

```text
data/processed/
└── year=2026/
    └── month=01/
        └── day=01/
            └── transactions.parquet
```

Benefits:

* Faster analytical queries
* Data lake concepts
* Scalable for Spark and Delta Lake integration

---

# 📊 Dashboards

## Executive Dashboard

Features:

* Total Transactions
* Fraud Transactions
* Fraud Percentage
* Total Transaction Amount
* Average Transaction Amount

---

## Fraud Analytics Dashboard

Features:

* Fraud by Payment Channel
* Fraud by Location
* Fraud by Hour
* Risk Category Distribution
* Fraud Score Distribution
* Top Fraud Customers

---

## Banking Analytics Dashboard

Features:

* Daily Transaction Volume
* Daily Transaction Amount
* Payment Channel Distribution
* Transaction Type Distribution
* Transaction Amount by Channel
* Peak Transaction Hours

---

# 📸 Project Screenshots

## Airflow DAG

<img width="1877" height="787" alt="airflow_dag" src="https://github.com/user-attachments/assets/3fe3d3fc-f5eb-474a-a2e8-80530f81c36a" />

---

## Executive Dashboard

<img width="2260" height="978" alt="executive_dashboard" src="https://github.com/user-attachments/assets/81c55419-a763-4ad8-83b1-ca2b27187048" />

---

## Fraud Dashboard

<img width="2237" height="1279" alt="fraud_dashboard" src="https://github.com/user-attachments/assets/98a9160d-5e9d-4a3c-963b-54f8ecdc0d0c" />

---

## Banking Dashboard

<img width="2260" height="978" alt="banking_dashboard" src="https://github.com/user-attachments/assets/2fb18937-280d-4dca-ae62-f0fa891d06e3" />

---

## Docker Containers

<img width="1816" height="371" alt="docker_containers" src="https://github.com/user-attachments/assets/49f5917b-0406-4ebc-bf22-eaa8db156502" />

---

# 🐳 Running the Project

## Clone Repository

```bash
git clone <your-repo-url>
cd banking-fraud-pipeline
```

---

## Create Virtual Environment

```bash
python -m venv .venv
```

Activate:

```bash
# Windows
.venv\Scripts\activate

# Linux/Mac
source .venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Start Docker Services

```bash
docker compose up -d
```

---

## Run Pipeline Locally

```bash
python main.py
```

---

## Run Airflow Pipeline

Open:

```text
http://localhost:8081
```

Trigger:

```text
banking_fraud_pipeline
```

---

## Open Superset

```text
http://localhost:8088
```

---

# 🧪 Synthetic Data Generation

Generate large datasets:

```bash
python scripts/generate_transactions.py
```

Supports:

* 100K+ transactions
* Dashboard testing
* Performance testing

---

# 📈 Key Project Metrics

* 100K+ Transactions Processed
* Fraud Detection Engine
* Modular ETL Architecture
* Dockerized Deployment
* Airflow Orchestration
* Interactive Dashboards
* Partitioned Data Lake Storage

---

# 🔮 Future Enhancements

* Kafka Streaming Ingestion
* PySpark Processing
* Delta Lake Integration
* Machine Learning Fraud Detection
* Great Expectations Data Validation
* CI/CD Pipeline
* Cloud Deployment on AWS
* Real-Time Dashboarding

---

# 🎯 Key Learnings

* Data Validation Frameworks
* Modular ETL Design
* Rule Engine Development
* Data Lake Concepts
* Airflow Orchestration
* Docker Containerization
* Data Modeling
* Dashboard Development
* End-to-End Data Engineering Practices

---

# ⭐ If you found this project useful, consider giving the repository a star!
