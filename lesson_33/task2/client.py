import socket

HOST = '127.0.0.1'
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    text = input("Enter text:\n")
    key = input("Input shift key:\n")
    s.sendall(bytes(key + "|" + text, 'utf-8'))
    data = s.recv(1024)

print('Received text', repr(data))
