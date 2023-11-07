import socket

UDP_IP_ADDRESS = '127.0.0.1'
UDP_PORT_NO = 65432

serverSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverSock.bind((UDP_IP_ADDRESS, UDP_PORT_NO))
while True:
    data= serverSock.recv(1024)
    data = data.upper()
    print(data)
