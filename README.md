# CS3251_P2
- README
1) High Level Description
Given a port number, server binds to the port and waits for connection request from client. Once the connection is established and the client wishes to play the game(either by pressing 'y' or backdoor), the server sends a game template that the client can respond to. Server also loads an array of words based on the text file given, or a default word dictionary text file included in the zip. Server-Client messages contain the required fields asked in the instructions(such as message length, word length, data, etc.). Server can accept up to 3 connections, and refuses to connect to additional clients unless any of the three previous clients finishes playing the game and a spot opens up. 

2) Team Member Names
- Seon Gyoo Lee
- Theunis Gerber

3) Who Did What
All of the work(code to write-up) was done as a group effort, with testing done individually to confirm robustness of the system. 

4) Run Instructions
- pip3 install packages in requirements.txt
- python3 server.py (port_number) (optional txt file)
- python3 client.py 127.0.0.1 (same_port_number)
- We used 8888 for port number for testing purposes
- additional clients can be opened up in different terminals

*run on python3*
*Default text file in folder must be named: 'word_dictionary.txt'* (already included)

5) test results:
Test Result 1 (correctly guessing word, including edge cases for guesses):

Server:
    python3 server.py 8888
    Socket Created
    ('127.0.0.1', 8888)
    Socket Bind Success
    Socket Listening
    Get connected from 127.0.0.1 : 53580
    End the connection from 127.0.0.1 : 53580

Client:
    python3 client.py 127.0.0.1 8888
    Ready to start game? (y/n)1
    _ _ _ _
    Incorrect Guesses:

    Letter to guess: z # a correct guess
    _ _ z z
    Incorrect Guesses:

    Letter to guess: s # an incorrect guess
    _ _ z z
    Incorrect Guesses:  S

    Letter to guess: ? # a non letter guess
    Error! Please guess ONE letter.

    Letter to guess: asdfe # more than one letter guess
    Error! Please guess ONE letter.

    Letter to guess: A # correct guess but uppercase
    _ a z z
    Incorrect Guesses:  S

    Letter to guess: j # final correct guess with graceful ending
    You Win!
    Game Over!

Word Dictionary: 
    4 15
    jazz
    buzz
    hajj
    fizz
    jinx
    huff
    buff
    jiff
    junk
    quiz
    bone
    rock
    kiss
    rekt
    pets




Test Result 2 (incorrect guessing of word):

server:
    python3 server.py 8888
    Socket Created
    ('127.0.0.1', 8888)
    Socket Bind Success
    Socket Listening   
    Get connected from 127.0.0.1 : 53633
client:
    python3 client.py 127.0.0.1 8888
    Ready to start game? (y/n)2
    _ _ _ _
    Incorrect Guesses:  

    Letter to guess: b  
    b _ _ _
    Incorrect Guesses:  

    Letter to guess: a
    b _ _ _
    Incorrect Guesses:  A

    Letter to guess: c
    b _ _ _
    Incorrect Guesses:  A C

    Letter to guess: r
    b _ _ _
    Incorrect Guesses:  A C R

    Letter to guess: t
    b _ _ _
    Incorrect Guesses:  A C R T

    Letter to guess: y
    b _ _ _
    Incorrect Guesses:  A C R T Y

    Letter to guess: i
    You Lose :(
    Game Over!

word dictionary:
    4 15
    jazz
    buzz
    hajj
    fizz
    jinx
    huff
    buff
    jiff
    junk
    quiz
    bone
    rock
    kiss
    rekt
    pets