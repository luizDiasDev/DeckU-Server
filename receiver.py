import socket

class  Receiver:
    
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind((self.ip, self.port))

    def receive(self):
        while True:
            data, addr = self.sock.recvfrom(1024)
            print(f"Received message: {data.decode()} from {addr}")