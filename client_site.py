import time
import zmq
import sys
import os
import datetime

#CLIENT SITE

def log(func):
    def wrapper(*args, **kwargs):
        value = func(*args, **kwargs)
        with open("logs.txt", "a") as file:
            now = datetime.datetime.now()
            file.write(f"Client::{now:%Y-%m-%d %H:%M:%S} >> {func.__name__} \n")
        return value
    return wrapper


class Test:
    def __init__(self):
        self.context = zmq.Context()
        print("connecting to sever")
        self.socket = self.context.socket(zmq.REQ)
        self.socket.connect("tcp://localhost:"+str(self.init_game()))

    # 
    # Connect to host
    #

    @log
    def connect(self):
        while True:
            self.socket.send(b"connected")
            self.message = self.socket.recv()

            if self.message == b'connected':
                print("connected to host")
                self.socket.send(b"connected successfully")
                self.game()
                break
            else:
                print("not connected")
            
            

            time.sleep(1)

    # 
    # Take id from user to connect with host 
    #

    @log
    def init_game(self):
        id = input("Type id to connect with host: ")
        return id
    
    #
    # Get answer from user
    #

    @log
    def get_answer(self):
        answer = input("type anwser: ")
        return answer

    #
    # Begin game
    #

    @log
    def game(self):
        message = self.socket.recv().decode()
        
        print(message)

        if message == 'stop':
                sys.exit()

        while True:
            self.socket.send(self.get_answer().encode())
            print("waiting for response \n\n")
            resp = self.socket.recv().decode()
            os.system("cls")
            print(resp)
            if resp == "end_game":
                print("you won!")
                sys.exit()
            

test = Test()
test.connect()