# Scalable Data warehouse Tech stack
 **Data Engineering Project**: Building Scalable Data warehouse tech stack using PostgreSQL, DBT, Airflow, Spark, and Superset (Change and Automation)

### Table of Content

- [Introduction](#introduction)
- [Data](#data)
- [Technologies used](#technologies-used)
- [Airflow](#airflow)
- [DBT](#dbt)
- [Scripts](#scripts)
- [Install](#instalation)
- [Documentation](#documentation)


### Introduction

An AI startup deployed sensors to businesses, that collects data from all activities in a business - from people’s interaction to the smart appliances installed in the company to reading environmental and other relevant information. 

This project aims to collect a stream of data from all sensors, and analyse the data to provide key insights to the business. 
By doing this will help to reduce the cost of running the client facility as well as to increase the livability and productivity of workers. 

In this project, it is requested to create a scalable data warehouse tech-stack tool that will help the AI startup to provide a better service to the client.


### Data

For building this project, a sample data found in Data [`ucdavis.edu`](https://anson.ucdavis.edu/~clarkf/) is used which contains parquet data, and or sensor data in CSV formats with size ~1.5Gb uncompressed each.

The data used in this project are `I80_stations.csv` ,and `I80_davis.txt`. These files are tracked with dvc, and are found on `data` directory.

If you wish to run/use this project, download these data from the url specified and put them into the data directory.

- **`I80_stations.csv`** : contains stations metadata
- **`I80_davis.txt`** : contains the sensor data, which has about `(3 * 10 ** 6)*11.9629 ~ 35,888,700` rows of data

### Technologies used

- [Airflow](#) : Airflow ...
- [DBT](#): DBT ...
- [Docker-compose](#):  ...
- [PostgreSQL](#): PostgreSQL ...
- [Apache-Spark](#): Apache-Spark ...
- [Superset](#): Superset ...





### Instalation

- **Install Required Python packages**

```
git clone https://github.com/Caphace-Ethan/data-warehouse-tech-stack
cd data-warehouse-tech-stack
pip install -r requirements.txt
```

- **Docker-compose**

```
docker-compose up --build
```

- **Airflow**

```
----
```

- **DBT**
Try running the following commands:

```
dbt debug
dbt compile
dbt seed
dbt run
dbt test
dbt docs generate
dbt docs serve
```

### DBT Resources:
- Learn more about dbt [in the docs](https://docs.getdbt.com/docs/introduction)
- Check out [Discourse](https://discourse.getdbt.com/) for commonly asked questions and answers
- Join the [chat](http://slack.getdbt.com/) on Slack for live discussions and support
- Find [dbt events](https://events.getdbt.com) near you
- Check out [the blog](https://blog.getdbt.com/) for the latest news on dbt's development and best practices


### Scripts

- **`create_db_tables.py `** : Scripts to create database, and tables to `MySQL` database