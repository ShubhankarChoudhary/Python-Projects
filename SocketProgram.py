import socket



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
    print('The name of the Client is ',name,' and Port number is ',port)
    print('***********************************************************')
    ip.send(bytes("Welcome to the world of Sockets",'utf-8'))
    ip.close()
