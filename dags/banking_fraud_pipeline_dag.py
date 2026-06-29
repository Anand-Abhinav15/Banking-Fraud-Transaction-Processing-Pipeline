from airflow import DAG
from airflow.operators.python import PythonOperator

from datetime import datetime
import sys

sys.path.append("/opt/airflow/project")

from etl.airflow_tasks import(
    extract_task,
    validate_task,
    deduplicate_task,
    fraud_task,
    transform_task,
    load_task
)

default_args = {
    "owner": "abhinav",
    "retries": 1
}

with DAG(
    dag_id = "banking_fraud_pipeline",
    start_date = datetime(2026,1, 1),
    schedule = None,
    catchup = False,
    default_args = default_args,
    tags= ["banking", "fraud", "etl"]
) as dag:

    extract = PythonOperator(
        task_id = "extract", python_callable = extract_task
    )

    validate = PythonOperator(
        task_id = "validate", python_callable = validate_task
    )

    deduplicate = PythonOperator(
        task_id = "deduplicate", python_callable = deduplicate_task
    )

    fraud = PythonOperator(
        task_id = "fraud_detection", python_callable = fraud_task
    )

    transform = PythonOperator(
        task_id = "transform", python_callable = transform_task
    )

    load = PythonOperator(
        task_id = "load", python_callable = load_task
    )

    (extract >> validate >> deduplicate >> fraud >> transform >> load)