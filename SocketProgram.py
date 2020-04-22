import mysql.connector
import socket
import pickle

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
    n = ip.recv(1024)
    n = pickle.loads(n)
    print(n[0])
    print(n[1])
    name = (n[0],)
    password = n[1]
    #password = ip.recv(1024).decode()
    #print(password)
    pointer2 = db.cursor()
    query = ("select * from login where Name = %s")
    pointer2.execute(query,name)
    for i in pointer2:
        print(i)
        #if i != None:
            #if pointer2[i+1] == password:
                #ip.send(bytes("Welcome to the world of Sockets", 'utf-8'))
                #print('The name of the Client is {name} and Port number is ', port)
            #else:
             #   print('Please enter your password correctly')
        #else:
            #print('Client is not authorised')
    print('***********************************************************')
    #ip.send(bytes("Welcome to the world of Sockets",'utf-8'))
    ip.close()
