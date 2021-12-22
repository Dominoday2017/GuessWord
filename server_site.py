import time
import datetime
import zmq

#SERVER SITE

def log(func):
    def wrapper(*args, **kwargs):
        with open("logs.txt", "a") as file:
            now = datetime.datetime.now()
            file.write(f"{now:%Y-%m-%d %H:%M:%S} >> {func.__name__} \n")
    return wrapper


class Server:
    def __init__(self):
        print("starting server...")
        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.REP)
        self.socket.bind("tcp://*:5555")
        self.packet_listener()

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
    
    def generate_word(self):
        word = input("Type word to guess: ")
        return word
    
    def game(self):
        self.init_game()

        command = input()

        if command.lower() == "start":
            self.word = self.generate_word()
            self.socket.send(b"Your opponent set word to guess. Now is your turn to answer. Type your word")

        while True:
            self.message = self.socket.recv()
            #print(f"Received request: {self.message}")
            
            print(f"Your opponent said: {self.message} \n")

            if self.message.lower() == self.word.lower():
                print("Your opponent guessed your secret word, you lose..")
                break
            else:
                print("Your opponent did not guess, type: \n 1. 'hint' to send him hint \n 2.'again' to give him another chance \n ")
            
            time.sleep(0.5)
            #self.socket.send(b"World")



server = Server()
server.__init__()