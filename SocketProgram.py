import mysql.connector
import socket

db = mysql.connector.connect(host = '127.0.0.1',user = 'root', passwd = 'Shubhankar@1', database = 'python')

pointer = db.cursor()
#pointer.execute('show databases')
print('Connected to database')
#query="select databases"
#pointer.execute('show databases')


s= socket.socket()
print('Socket Connected')
s.bind(('192.168.1.13',9999))
print('Connecting to Client')

s.listen(5)

while True:
    ip,port = s.accept()
    print('Connection Established')
    print('***********************************************************')
    name = ip.recv(1024).decode()
    pointer2 = db.cursor()
    #l=list(pointer2.execute("select * from login where Name = 'Shubhankar'"))
    #print(l)
    print('The name of the Client is ',name,' and Port number is ',port)
    print('***********************************************************')
    ip.send(bytes("Welcome to the world of Sockets",'utf-8'))
    ip.close()
