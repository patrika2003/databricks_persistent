import mysql.connector
conn=mysql.connector.connect(
  host="localhost",
  port=3306,
  user="root",
  password="patrika@2003",
  database="college"
)

cursor=conn.cursor()
cursor.execute("select * from college.student")
for row in cursor:
  print(row)


conn.close()