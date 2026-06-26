#KPI 1 — Daily Transaction Volume

SELECT
    transaction_date,
    COUNT(*) AS total_transactions
FROM clean_transactions
GROUP BY transaction_date
ORDER BY tansaction_date;


#KPI 2 — Average Transaction Amount

SELECT
    transaction_date,
    ROUND(AVG(amount), 2) AS avg_count
FROM clean_transactions
GROUP BY transaction_date
ORDER BY transaction_date;

#KPI 3 — Fraud Transactions

SELECT
    COUNT(*) AS suspicious_transactions
FROM clean_transactions
WHERE fraud_score >0;

#KPI 4 — Fraud Percentage By Channel

SELECT
    payment_channel,
    ROUND(100.0*SUM(
            CASE 
                WHEN fraud_score > 0 THEN 1
                ELSE 0
            END
        ) / COUNT(*), 2
    ) AS fraud_percentage
FROM clean_transactions
GROUP BY payment_channel;

#KPI 5 — Fraud By Region

SELECT
    location,
    COUNT(*) AS fraud_transactions
FROM clean_transactions
WHERE fraud_score > 0
GROUP BY location
ORDER BY fraud_transactions DESC;


#KPI 6 — High Risk Customers

SELECT
    customer_id,
    COUNT(*) AS suspicious_count,
    SUM(fraud_score) AS total_score
FROM clean_transactions
WHERE fraud_score > 0
GROUP BY customer_id
ORDER BY total_score DESC;


#KPI 7 — Peak Transaction Hours

SELECT 
    transaction_hour,
    COUNT(*) AS total_transactions
FROM clean_transactions
GROUP BY transaction_hour
ORDER BY total_transactions DESC;


#KPI 8 — Fraud Distribution By Risk Category  

SELECT 
    risk_category,
    COUNT(*) AS transactions
FROM clean_transactions
GROUP BY risk_category
ORDER BY transactions DESC;


#KPI 9 — Top Payment Channels

SELECT
    payment_channel,
    COUNT(*) AS transaction_count
FROM clean_transactions
GROUP BY payment_channel
ORDER BY transaction_count DESC;


#KPI 10 — Total Transaction Amount By Day

SELECT 
    transactions_date,
    SUM(amount) AS total_amount
FROM clean_transactions
GROUP BY transaction_date
ORDER BY transaction_date;

