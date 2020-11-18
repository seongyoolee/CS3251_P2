import socket
import sys
import json

BUF_SIZE = 1024
SERVER = sys.argv[1]
PORT = int(sys.argv[2])
play = True
letter_attempts = set()
incorrect_attempts = []
previous_guess = ""
previous_server_message = ""

s = socket.socket()
s.connect((SERVER, PORT))

def generate_client_message(data):
    length = 1 if type(data) == int else len(data)
    client_message = json.dumps({"msg_length": length, "data": data})
    return client_message

while True:
    user_response = input("Ready to start game? (y/n)").lower()
    print(user_response)
    if user_response.isnumeric():
        word_index = int(user_response) - 1
        s.sendall(generate_client_message(word_index).encode())
        break
    elif user_response == "y":
        s.sendall(generate_client_message(-1).encode())
        break
    elif user_response == "n":
        s.sendall(generate_client_message(-2).encode())
        play = False
        break
    else:
        print("Input not valid. Try again.")
    
while play:
    server_message = json.loads(s.recv(BUF_SIZE).decode())

    # print server message right away
    print(server_message["data"])

    if server_message["msg_flag"] > 0:# check if server sent "message"
        if server_message["data"] == "Game Over!":
            break
    else:# server sent "game progress"
        if server_message["data"] == previous_server_message:
            if previous_guess:
                incorrect_attempts.append(previous_guess.upper())
        else:
            previous_server_message = server_message["data"]
        print("Incorrect Guesses: ", " ".join(incorrect_attempts))

        user_guess = input("\nLetter to guess: ").lower()
        while user_guess < 'a' or user_guess > 'z' or len(user_guess) != 1 or user_guess in letter_attempts:
            if user_guess in letter_attempts:
                print("Error! Letter " + user_guess.upper() + " has been guessed before, please guess another letter.")
            else:
                print("Error! Please guess ONE letter.")
            user_guess = input("\nLetter to guess: ").lower()
        letter_attempts.add(user_guess)
        previous_guess = user_guess
        s.sendall(generate_client_message(user_guess).encode())

s.close()