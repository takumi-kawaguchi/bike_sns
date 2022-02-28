import mysql.connector as mysql


# conn = mydb.connect(
#     host='bike-sns-db-container',
#     port=3307,
#     user='test',
#     password='bike_sns',
#     database='bike_sns'
# )

# print(conn.is_connected())


# bike_makers

conn = mysql.connect(
    host="bike-sns-db-container",
    user="root",
    port=3306,
    database="bike_sns"
)

cur = conn.cursor()

table = 'users'
cur.execute('SELECT * FROM users')
rows = cur.fetchall()
for row in rows:
    print(row)
