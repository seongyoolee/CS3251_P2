# CS3251_P2
- README
1) high level description

2) team member names
- Seon Gyoo Lee
- Theunis Gerber
3) who did what

4) run instructions
- python3 server.py (port_number) (optional txt file)
- python3 client.py 127.0.0.1 (same_port_number)
- We used 8888 for port number for testing purposes

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