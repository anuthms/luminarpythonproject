import mysql.connector

#step 1: establish a connection eith mysql

db=mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='Password@123',
    auth_plugin='mysql_native_password'
)

#step 3: create a cursor object
cursor=db.cursor()
sql='select version()'
cursor.execute(sql)
data=cursor.fetchone()
print(data)
db.close()

