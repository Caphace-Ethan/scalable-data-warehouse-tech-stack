from airflow import DAG
from airflow.operators.python import PythonOperator, BranchPythonOperator
from airflow.operators.bash import BashOperator
from datetime import datetime
import time


def _create_db_table():
	# Execute dbt to compile models
	time.sleep(15)
	return "Created table"


def _load_data_db_table():
	# Execute dbt to load the data to db
	time.sleep(20)
	return "Data Loaded to table"


with DAG("create_tables", start_date=datetime(2021, 9, 21),
		 schedule_interval="@daily", catchup=False) as dag:

	creating_db_tables = PythonOperator(
		task_id="creating_db_tables",
		python_callable=_create_db_table
	)

	loading_station_data_db = PythonOperator(
		task_id="load_station_data",
		python_callable=_load_data_db_table
	)

	creating_db_tables >> loading_station_data_db
