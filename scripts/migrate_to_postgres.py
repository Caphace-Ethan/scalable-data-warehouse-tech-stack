import pandas as pd
import psycopg2
from psycopg2 import Error
import mysql.connector as mysql


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
            print(f":: Fetching data from MySQL Progress, {round((i*100)/result.rowcount,2)}")

        conn.commit()
        cur.close()
        print("Records Fetched, Sucessfully")
    except Exception as e:
        print(":::", e)

    print("----- Done")

    try:
        conn, cur = PostgresConnect(PostgresdbName)
        for row in data_list:
            print(f":: Migration Progress, {round((row*100)/len(data_list),2)}")
            sql = f"INSERT INTO {PostgresdbName}.{tableName} VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

        conn.commit()
        cur.close()
    except Exception as e:
        print(e)

    return None


if __name__ == "__main__":

    if (True):
        sensor_table_name = "all_sensor_data"
        station_table_name = "I80_stations"
        migrate_data_from_table(MysqldbName='sensor_data', PostgresdbName='sensor_data', tableName=station_table_name)
        migrate_data_from_table(MysqldbName='sensor_data', PostgresdbName='sensor_data', tableName=sensor_table_name)
        print("Sucessfully, created db and Tables")

