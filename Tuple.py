import mysql.connector

db=mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'Shubhankar@1',
    database = 'python'
)
pointer2 = db.cursor()
query = ("select * from login where Name = %s")
name = ('Shubhankar',)
pointer2.execute(query,name)
for i in pointer2:
    print(i)