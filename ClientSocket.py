import socket
import time
c = socket.socket()
print('Connecting to server')
time.sleep(2)
name = input('Enter your Name : ')
password = input('Enter your password : ')
c.connect(('192.168.1.13',9999))
c.send(bytes(name,'utf-8'))
data = c.recv(1024).decode()
print("Data received from Server is : ", data)