import pandas as pd
import psycopg2
from psycopg2 import Error
import mysql.connector as mysql
station_sqlFile = './sql_schema/station_table_schema.sql'
sensor_sqlFile = './sql_schema/sensor_table_schema.sql'
station_data_path = "./data/I80_stations.csv"
sensor_data_path = "./data/all_sensor_data1.csv"


def PostgresConnect(dbName=None):

    try:
        conn = psycopg2.connect(host="localhost",
                             user="dbtuser",
                             passwd="pssd",
                             port="5433",
                             database=dbName
                             )

        cur = conn.cursor()
        conn.autocommit = True
        print('Connection Established')

    except Exception as error:
        print(error)
        conn, cur = None, None

    return conn, cur


def MySQLConnect(dbName=None):
    try:
        conn = mysql.connect(host="localhost",
                             user="root",
                             passwd="password",
                             port="3306",
                             database=dbName
                             )

        cur = conn.cursor()
        conn.autocommit = True
        print('Connection Established')

    except Exception as error:
        print(error)
        conn, cur = None, None

    return conn, cur


def migrate_data_from_table(MysqldbName: str, PostgresdbName: str,  tableName: str) -> None:
    try:
        conn, cur = MySQLConnect(MysqldbName)

        sql = f"SELECT * FROM {tableName}"
        cur.execute(sql)
        print("Record inserted")
        # Fetch all the records
        data_list = []
        result = cur.fetchall()
        for i in result:
            data_list.append(i)
            print(":::", i)

        conn.commit()
        print("Records Fetched, Sucessfully")
    except Exception as e:
        print(":::", e)

    conn.commit()
    cur.close()
    print("----- Done")

    conn, cur = PostgresConnect(PostgresdbName)
    for row in data_list:
        sql = f"INSERT INTO {PostgresdbName}.{tableName} VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

    conn.commit()
    cur.close()
    return data_list

