import socket
import sys
import _thread
import random
import json

num_connections = 0
BUF_SIZE = 1024
HOST = "127.0.0.1"
PORT = int(sys.argv[1])
FILE = 'word_dictionary.txt'

# get file
if len(sys.argv) == 3:
    FILE = sys.argv[2]
elif len(sys.argv) > 3:
    print("Too many arguments given to run the server.")

# load from word dictionary
f = open(FILE, "r")
words = []
lines = f.readlines()
for line in lines[1:]:
    if line[-1] == '\n':
        line = line[:-1]
    words.append(line)

# create socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Socket Created")

# bind socket
try:
    print((HOST, PORT))
    s.bind((HOST, PORT))
except:
    print("Socket Bind Failure Error: ", socket.error.strerror())
    sys.exit()
print("Socket Bind Success")


# socket listen
s.listen()
print("Socket Listening")

def generate_server_message(data, word_to_guess, letter_attempts):
    if data in ["You Win!", "You Lose :(", "Game Over!"]:
        return json.dumps({
            "msg_flag": len(data), 
            "data": data
        })
    else:
        return json.dumps({
            "msg_flag": 0, 
            "word_length": len(word_to_guess), 
            "num_incorrect": len(letter_attempts - set(word_to_guess)),
            "data": data
        })


# thread to connect client
def connect_client(connection, address):
    print("Get connected from", address[0], ":", address[1])

    word_to_guess = ""
    word_progress = []
    letter_attempts = set()
    num_remaining_attempts = 6

    while True:
        client_message = connection.recv(BUF_SIZE).decode()
        client_message = json.loads(client_message)
        client_data = client_message["data"]

        # print("word to guess: ", word_to_guess)

        if type(client_data) == int:# set word to guess
            if client_data == -2:
                break
            elif client_data == -1:
                word_to_guess = random.choice(words)
            else:
                word_to_guess = words[client_data]
            word_progress = ["_" for i in range(len(word_to_guess))]
            progress = " ".join(word_progress)
            connection.sendall(generate_server_message(progress, word_to_guess, letter_attempts).encode())
        else:# user/client guesses letters in word
            if client_data not in letter_attempts and client_data in word_to_guess:
                letter_attempts.add(client_data)

                # update word progress
                for i in range(len(word_to_guess)):
                    if word_to_guess[i] == client_data:
                        word_progress[i] = client_data

                if "_" not in word_progress:#User Wins
                    connection.sendall(generate_server_message("You Win!", None, None).encode())
                    connection.sendall(generate_server_message("Game Over!", None, None).encode())
                    break
                else:# keep playing game, send progress
                    progress = " ".join(word_progress)
                    connection.sendall(generate_server_message(progress, word_to_guess, letter_attempts).encode())
            else:
                num_remaining_attempts -= 1
                if num_remaining_attempts == 0:
                    connection.sendall(generate_server_message("You Lose :(", None, None).encode())
                    connection.sendall(generate_server_message("Game Over!", None, None).encode())
                    break
                progress = " ".join(word_progress)
                connection.sendall(generate_server_message(progress, word_to_guess, letter_attempts).encode())

    print("End the connection from", address[0], ":", address[1])
    connection.close()
    global num_connections
    num_connections -= 1
    # print("remaining connections: ", num_connections)

# communicate with client
while True:
    connection, address = s.accept()

    # connect with client
    if num_connections < 3:
        num_connections += 1
        # print("num connections: ", num_connections)
        _thread.start_new_thread(connect_client, (connection, address, ))
    else:
        print("server-overloaded")
        connection.close()

s.close()