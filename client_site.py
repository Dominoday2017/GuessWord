import time
import zmq
import sys
import os

#CLIENT SITE

class Test:
    def __init__(self):
        self.context = zmq.Context()
        print("connecting to sever")
        self.socket = self.context.socket(zmq.REQ)
        self.socket.connect("tcp://localhost:"+str(self.init_game()))

    # 
    # Connect to host
    #

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

    def init_game(self):
        id = input("Type id to connect with host: ")
        return id
    
    #
    # Get answer from user
    #

    def get_answer(self):
        answer = input("type anwser: ")
        return answer

    #
    # Begin game
    #

    def game(self):
        print(self.socket.recv().decode())

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