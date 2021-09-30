from airflow import DAG
from airflow.operators.python import PythonOperator, BranchPythonOperator
from airflow.operators.bash import BashOperator
from datetime import datetime
import time
import os


def _create_db_table():
	try:
		project_dir = os.system("cd ..")
		print(project_dir)
		project_dir = os.system("cd scripts/")
		os.system("./create_db_table.sh")
		e = "Creating db and tables in PostgreSQL database, successfully"
	except Exception as e:
		e = e
	return e


def _migrate_data_mysql_postgres():
	try:
		project_dir = os.system("cd ..")
		print(project_dir)
		project_dir = os.system("cd scripts/")
		os.system("./migrate.sh")
		e = "Migrating data from MySQL to PostgreSQL database, successfully"
	except Exception as e:
		e = e
	return e


with DAG("create_tables", start_date=datetime(2021, 9, 21),
		 schedule_interval="@daily", catchup=False) as dag:

	creating_db_tables = PythonOperator(
		task_id="creating_db_tables",
		python_callable=_create_db_table
	)

	loading_station_data_db = PythonOperator(
		task_id="load_station_data",
		python_callable=_migrate_data_mysql_postgres
	)

	creating_db_tables >> loading_station_data_db
