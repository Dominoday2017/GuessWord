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
        #self.connect()
        self.packet_listener()

    def connect(self):


        print("enable listener..")

        
    def packet_listener(self):
        while True:
            self.message = self.socket.recv()
            print(f"Received request: {self.message}")
            time.sleep(1)
            self.socket.send(b"World")



server = Server()
server.__init__()