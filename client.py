import socket
import sys

SERVER = sys.argv[1]
PORT = int(sys.argv[2])

s = socket.socket()
s.connect((SERVER, PORT))

message = "0"
s.sendall(message.encode())

BUF_SIZE = 1024
while True:
    message = s.recv(BUF_SIZE)
    print(message.decode())

s.close()