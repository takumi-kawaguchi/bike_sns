import mysql.connector as mydb

conn = mydb.connect(
    host='bike-sns-db-container',
    port=3307,
    user='test',
    password='bike_sns',
    database='bike_sns'
)

print(conn.is_connected())


# bike_makers
