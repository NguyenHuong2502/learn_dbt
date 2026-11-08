
from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.docker.operators.docker import DockerOperator
from docker.types import Mount

# Import hàm main từ file chứa logic gọi API
import sys
sys.path.append('/opt/airflow/api-request')

from api_inserts import main


def safe_main_callable():
    return main()


with DAG(
    dag_id='weather-dbt-orchestrator',
    description='A DAG to orchestrate weather data pipeline',
    start_date=datetime(2026, 10, 29),
    schedule=timedelta(minutes=5),
    catchup=False,
) as dag:

    task1 = PythonOperator(
        task_id='extract_weather_data',
        python_callable=safe_main_callable,
    )

    task2 = DockerOperator(
        task_id='transform_data_task',
        image='ghcr.io/dbt-labs/dbt-postgres:1.9.latest',
        command='run',
        working_dir='/usr/app',
        mounts=[
            Mount(
                source='/home/nguye/repos/weather-data-project/dbt/my_project',
                target='/usr/app',
                type='bind'
            ),
            Mount(
                source='/home/nguye/repos/weather-data-project/dbt',
                target='/root/.dbt',
                type='bind'
            )
        ],
        network_mode='weather-data-project_my-network',
        docker_url='unix://var/run/docker.sock',
        auto_remove='success',
    )

    task1 >> task2
