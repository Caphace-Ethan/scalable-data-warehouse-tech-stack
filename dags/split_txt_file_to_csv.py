from airflow import DAG
from airflow.operators.python import PythonOperator, BranchPythonOperator
from airflow.operators.bash import BashOperator
from datetime import datetime
import time
import os


def _create_small_txt_files():
	try:
		project_dir = os.system("cd ..")
		print(project_dir)
		project_dir = os.system("cd scripts/")
		os.system("./split_txt_file.sh")
		e = "Splitting txt file into small, successfully"
	except Exception as e:
		e = e
	return e


def _create_batches_csv_files(i):
	try:
		project_dir = os.system("cd ..")
		print(project_dir)
		project_dir = os.system("cd scripts/")
		os.system("./txt_to_csv.sh")
		e = "txt to csv conversion successfully"
	except Exception as e:
		e = e
	return e


with DAG("split_txt_file", start_date=datetime(2021, 9, 21),
		 schedule_interval="@daily", catchup=False) as dag:

	splitting_large_txt_file = PythonOperator(
		task_id="creating_small_txt",
		python_callable=_create_small_txt_files
	)

	creating_csv_from_txt = PythonOperator(
		task_id="creating_csv_from_txt",
		python_callable=_create_batches_csv_files
	)

	splitting_large_txt_file >> creating_csv_from_txt
