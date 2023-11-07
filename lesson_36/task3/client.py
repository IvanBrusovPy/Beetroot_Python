import socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65433      # The port used by the server



with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        message = input("Enter some text: ")
        if message == '0':
            break
        s.sendall(message.encode('utf-8'))
        data = s.recv(1024)
        print('Received', repr(data))


# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#     s.connect((HOST, PORT))
#     while True:
#         message = input("Enter some text: ")
#         if message == '0':
#             break
#         s.sendall(message.encode('utf-8'))
#         data = s.recv(1024)
#         print('Received', repr(data))
