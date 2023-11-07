from ceasar import encrypt
import socket

HOST = '127.0.0.1'
PORT = 65432
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        while True:
            data = conn.recv(1024)
            key_index = data.find(b"|")
            if not data:
                break
            data = encrypt(int.from_bytes(data[0:key_index], byteorder='little'), str(data[key_index+1:]))
            conn.sendall(bytes(data, encoding='utf8'))

