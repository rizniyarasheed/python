import mysql.connector

db=mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='Password@123',
    auth_plugin='mysql_native_password',
    database="pythondecember"
)

cursor=db.cursor()

sql="select * from movie"
cursor.execute(sql)
movies=cursor.fetchall()

for movie in movies:
    print(movie)
db.close()



import mysql.connector

db=mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='Password@123',
    auth_plugin='mysql_native_password',
    database="pythondecember"
)
def get_data():
    cursor=db.cursor()

    sql="select * from movie"

    cursor.execute(sql)
    yield cursor.fetchall()


movies=get_data()
print(movies.__next__())
db.close()