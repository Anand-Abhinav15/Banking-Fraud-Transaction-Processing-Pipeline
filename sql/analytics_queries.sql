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





