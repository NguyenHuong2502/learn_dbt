
import sys
from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.python import PythonOperator
sys.path.append('/opt/airflow/api-request')
from api_inserts import main
def safe_main_callable():
    return main()


with DAG(
    dag_id='weather-api-orchestrator',
    description='A DAG to orchestrate data',
    start_date=datetime(2026, 10, 29),
    schedule=timedelta(minutes=5),
    catchup=False,
) as dag:

    task1 = PythonOperator(
        task_id='ingest_data_task',
        python_callable=safe_main_callable,
    )
