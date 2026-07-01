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


CREATE TABLE IF NOT EXISTS fraud_transactions
(
    transaction_id VARCHAR(50),
    customer_id VARCHAR(50),
    account_number VARCHAR(50),
    transaction_type VARCHAR(50),
    merchant_id VARCHAR(50),
    amount NUMERIC(15,2),
    currency VARCHAR(10),
    transaction_timestamp TIMESTAMP,
    device_id VARCHAR(100),
    location VARCHAR(100),
    payment_channel VARCHAR(50),
    status VARCHAR(50),
    fraud_flag TEXT,
    fraud_score INTEGER,
    is_high_risk BOOLEAN,
    transaction_hour INTEGER,
    transaction_day VARCHAR(20),
    amount_bucket VARCHAR(50),
    risk_category VARCHAR(50),
    processing_timestamp TIMESTAMP
);






