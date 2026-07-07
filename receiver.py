import socket
import json

class  Receiver:
    
    def __init__(self, ip, port, callback):
        self.ip = ip
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind((self.ip, self.port))
        self.callback = callback

    def receive(self):
        while True:
            data, addr = self.sock.recvfrom(1024)

            self.callback(json.loads(data.decode()))

            