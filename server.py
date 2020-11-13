import socket
import sys

# HOST = sys.argv[0]
HOST = "127.0.0.1"
PORT = int(sys.argv[1])
FILE = 'word_dictionary.txt'
if len(sys.argv) == 3:
    FILE = sys.argv[2]
elif len(sys.argv) > 3:
    print("Too many arguments given to run the server.")

# create socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Socket Created")

# bind socket
try:
    print((HOST, PORT))
    s.bind((HOST, PORT))
except:
    print("Socket Bind Failure Error: ", socket.error)
    sys.exit()
print("Socket Bind Success")


# socket listen
s.listen()
print("Socket Listening")

BUF_SIZE = 1024
# communicate with client
while True:
    connection, address = s.accept()
    print("Connected with", address[0], "at PORT", address[1])

    data = connection.recv(BUF_SIZE).decode()
    connection.sendall("hello world".encode())
    connection.close()