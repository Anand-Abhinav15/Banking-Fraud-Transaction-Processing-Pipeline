from airflow import DAG
from airflow.operators.python import PythonOperator

from datetime import datetime
import sys

sys.path.append("/opt/airflow/project")

from main import run_pipeline

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

    run_pipeline_task = PythonOperator(
        task_id = "run_pipeline",
        python_callable = run_pipeline
    )

