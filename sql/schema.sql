CREATE TABLE IF NOT EXISTS clean_transactions(
transaction_id VARCHAR(50),
customer_id VARCHAR(50),
account_number VARCHAR(50),
transaction_type VARCHAR(20),
merchant_id VARCHAR(50),
amount NUMERIC,
currency VARCHAR(10),
transaction_timestamp TIMESTAMP,
fraud_flag TEXT,
fraud_score INTEGER,
is_high_risk BOOLEAN,
amount_bucket VARCHAR(20),
risk_category VARCHAR(20),
processing_timestamp TIMESTAMP
);







