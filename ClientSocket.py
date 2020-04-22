import socket

# import time

import pickle

l=[]
c = socket.socket()
print('Connecting to server')
# time.sleep(2)
name = input('Enter your Name : ')
l.append(name)
password = input('Enter your password : ')
l.append(password)
credentials = pickle.dumps(l)
print(credentials)
c.connect(('192.168.1.13', 9999))
c.send(bytes(credentials))
#c.send(bytes(password, 'utf-8'))
data = c.recv(1024).decode()
print("Data received from Server is : ", data)
