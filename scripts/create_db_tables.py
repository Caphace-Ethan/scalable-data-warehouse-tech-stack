import pandas as pd
import psycopg2
from psycopg2 import Error
global station_sqlFile
global sensor_sqlFile
station_sqlFile = './sql_schema/station_table_schema.sql'
sensor_sqlFile = './sql_schema/sensor_table_schema.sql'
station_data_path = "./data/I80_stations.csv"
sensor_data_path = "./data/all_sensor_data1.csv"


def DBConnect(dbName=None):

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


def createDB(dbName: str) -> None:

    try:

        conn, cur = DBConnect()
        sql = f"CREATE DATABASE {dbName};"
        cur.execute(sql)
        # conn.commit()
        cur.close()

    except Exception as e:
        print("::::", e)


def createTables(dbName: str, tableName: str) -> None:

    conn, cur = DBConnect(dbName)
    cur.execute(f"DROP TABLE IF EXISTS {tableName};")
    fd = open(tableName, 'r')
    readSqlFile = fd.read()
    fd.close()

    sqlCommands = readSqlFile.split(';')

    for command in sqlCommands:
        try:
            res = cur.execute(command)
            response = "Table created sucessfuly"
        except Exception as ex:
            print("Command skipped: ", command)
            response = "Table Not Created"
            print(ex)
    conn.commit()
    cur.close()

    return print(response)


if __name__ == "__main__":

    if (True):
        createDB(dbName='sensor_data')
        createTables(dbName='sensor_data', tableName=station_sqlFile)
        createTables(dbName='sensor_data', tableName=sensor_sqlFile)
        print("Sucessfully, created db and Tables")




