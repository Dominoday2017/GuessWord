import time
import zmq

#CLIENT SITE

class Test:
    def __init__(self):
        self.context = zmq.Context()
        print("connecting to sever")
        self.socket = self.context.socket(zmq.REQ)
        self.socket.connect("tcp://localhost:5555")

    def connect(self):
        for request in range(10):
            print(f"sending request {request}")
            self.socket.send(b"Hello")

            self.message = self.socket.recv()
            print(f"Recieved reply {request}, {self.message}")


test = Test()
test.connect()