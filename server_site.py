import time
import datetime
import zmq
import sys
import os

#SERVER SITE

def log(func):
    def wrapper(*args, **kwargs):
        value = func(*args, **kwargs)
        with open("logs.txt", "a") as file:
            now = datetime.datetime.now()
            file.write(f"Server::{now:%Y-%m-%d %H:%M:%S} >> {func.__name__} \n")
        return value
    return wrapper


class Server:
    def __init__(self):
        print("starting server...")
        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.REP)
        self.socket.bind("tcp://*:5555")
        self.packet_listener()
        
    #
    # Init server, wait for the client
    #

    @log
    def packet_listener(self):
        print("enable listener.. \n\n")

        while True:
            message = self.socket.recv()
            print(message)
            if message == b'connected':
                print("Connected. \n")
                self.socket.send(b"connected")
                self.game()
            else:
                self.socket.send(b"not connected")
                print("not connected")

            time.sleep(1)

    #
    # Display game menu
    #

    @log
    def init_game(self):
        id = 5555
        print('''Hello in this super extra cool game \n
                You are the host now, give this number to your opponent to connect \n
                 ''' + f'ID: {id}'
        )
        print('''
                 Menu: \n
                 1. Type: 'start' to start the game \n
                 2. 'stop' to stop the game \n
        ''')
    #    
    # Take secret word from user
    #
    
    @log
    def generate_word(self):
        word = input("Type word to guess: ")
        return word

    #
    # Get hint from host to send to the client
    #     
    
    @log
    def get_hint(self):
        hint = input("Type now your hint to the word: ")
        return hint

    #
    # Begin game
    #

    
    def game(self):
        self.init_game()
        self.socket.recv()

        command = input()

        if command.lower() == "start":
            self.secret_word = self.generate_word()
            self.socket.send(b'''Your opponent set word to guess. Now is your turn to answer. Type your word. \n He also gave first hint to his secret word: ''' + self.get_hint().encode() + b"\n" )

        if command.lower() == "stop":
            self.socket.send(b'stop')
            sys.exit()

        while True:
            self.message = self.socket.recv()
            print(f"Your opponent said: {self.message.decode()} \n")

            if self.message.lower().decode() == self.secret_word.lower():
                print("Your opponent guessed your secret word, you lose..")
                self.socket.send(b"end_game")
                sys.exit()
                break
                # add here options to restart game
            else:
                print("Your opponent did not guess, type: \n 1. 'hint' to send him hint \n 2.'again' to give him another chance without hint \n ")
                option = input()
                
                if option.lower() == "hint":
                    self.socket.send(b"Try again, here is the hint: " + self.get_hint().encode())
                else:
                    self.socket.send(b"Try again.")
            
            time.sleep(0.5)
            os.system("cls")
            print("waiting for response..\n\n")


server = Server()
server.__init__()