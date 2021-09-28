import pandas as pd
import mysql.connector as mysql

global station_sqlFile
global sensor_sqlFile
station_sqlFile = './sql_schema/station_table_schema.sql'
sensor_sqlFile = './sql_schema/sensor_table_schema.sql'


def DBConnect(dbName=None):

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
    cur.execute("DROP TABLE IF EXISTS stations")
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


def insert_data_to_table(dbName: str, tableName: str) -> None:
    try:
        conn, cur = DBConnect(dbName)
        df = pd.read_csv("./data/I80_stations.csv")
        df = df.where((pd.notnull(df)), None)
        df = df.astype(object).where(pd.notnull(df), None)

        print(df.dtypes)
        # df.to_sql(tableName, con=conn, index=False, if_exists='append')
        for i, row in df.iterrows():
            sql = "INSERT INTO sensor_data.stations VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            cur.execute(sql, tuple(row))
            print("Record inserted")
            # the connection is not autocommitted by default, so we

        conn.commit()
        print("Inserted Records, Sucessfully")
    except Exception as e:
        print(":::", e)

    conn.commit()
    cur.close()
    print("----- Done")


def fetch_data_from_table(dbName: str, tableName: str) -> None:
    try:
        conn, cur = DBConnect(dbName)

        sql = "SELECT * FROM stations"
        cur.execute(sql)
        print("Record inserted")
        # Fetch all the records
        result = cur.fetchall()
        for i in result:
            print(":::", i)

        conn.commit()
        print("Records Fetched, Sucessfully")
    except Exception as e:
        print(":::", e)

    conn.commit()
    cur.close()
    print("----- Done")

if __name__ == "__main__":

    if (True):
        # createDB(dbName='sensor_data')
        createTables(dbName='sensor_data', tableName=station_sqlFile)
        # createTables(dbName='sensor_data', tableName=sensor_sqlFile)
        print("Sucessfully, created db and Tables")

    elif (False):
        insert_data_to_table('sensor_data', 'stations')

    elif (False):
        fetch_data_from_table('sensor_data', 'stations')



