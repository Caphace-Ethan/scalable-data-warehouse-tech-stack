
#python3 migrate_to_postgres.py

python3 -c'import migrate_to_postgres; migrate_to_postgres.migrate_data_from_table(MysqldbName="sensor_data", PostgresdbName="sensor_data", tableName=station_table_name)'

python3 -c'import migrate_to_postgres; migrate_to_postgres.migrate_data_from_table(MysqldbName="sensor_data", PostgresdbName="sensor_data", tableName=sensor_table_name)'