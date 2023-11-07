import socket
import threading
HOST = '127.0.0.1'  # Standard loop-back interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)


def start_connection(connection, address):
    with connection:
        print('Connected by', address)
        while True:
            data = connection.recv(1024)
            if not data:
                break
            connection.sendall(data.upper())


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    while True:
        conn, addr = s.accept()
        t = threading.Thread(target=start_connection, args=(conn, addr,))
        t.start()
        print(t.native_id)
        t.join()
