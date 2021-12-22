import time
import zmq

#CLIENT SITE

class Test:
    def __init__(self):
        self.context = zmq.Context()
        print("connecting to sever")
        self.socket = self.context.socket(zmq.REQ)
        self.socket.connect("tcp://localhost:"+str(self.init_game()))

    def connect(self):
        while True:
            self.socket.send(b"connected")

            self.message = self.socket.recv()
            #print(f"{self.message}")
            if self.message == b'connected':
                print("connected to host")
                self.game()
            else:
                print("not connected")

            time.sleep(1)



        #for request in range(10):
            #print(f"sending request {request}")
            #self.socket.send(b"Hello")



    def init_game(self):
        id = input("Type id to connect with host: ")
        return id
    
    def game(self):
        pass

test = Test()
test.connect()