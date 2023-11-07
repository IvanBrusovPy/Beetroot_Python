import multiprocessing
import socket
HOST = '127.0.0.1'  # Standard loop-back interface address (localhost)
PORT = 65433
# Port to listen on (non-privileged ports are > 1023)


def start_connection(connection, address):
    with connection:
        print('Connected by', address)
        while True:
            data = connection.recv(1024)
            if not data:
                break
            connection.sendall(data.upper())


if __name__ == '__main__':
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        while True:
            conn, addr = s.accept()
            print("Connected: ", HOST, PORT)
            p1 = multiprocessing.Process(target=start_connection, args=(conn, addr,), daemon=True)
            p1.start()

