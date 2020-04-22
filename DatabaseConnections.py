import mysql.connector

db=mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'Shubhankar@1',
    database = 'python'
)

mycursor = db.cursor()

query= 'show databases'

mycursor.execute(query)

for i in mycursor:
    print(i)
print('***********************')

#query2 = "insert into login values (%s,%s)"
#credential = [('Shyam','KLM'),('Mohan','STU'),('Vivek','OPQ')]

#mycursor.executemany(query2,credential)

#db.commit()
query = ("select * from login where name = %s")
name=('Shubhankar',)
mycursor.execute(query,name)

for i in mycursor:
    print(i)