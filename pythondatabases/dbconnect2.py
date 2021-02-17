import mysql.connector

db=mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='Password@123',
    auth_plugin='mysql_native_password',
    database='pythondecember'
)
cursor=db.cursor()
sql='create table movie(id int,name vaechar(50),year varchar(30).rating int)'
cursor.execute(sql)
print("table created")
db.close()