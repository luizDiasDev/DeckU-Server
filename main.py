from receiver import Receiver
from virtual_gamepad import VirtualGamepad
from dotenv import load_dotenv
import os


def main():

    load_dotenv()

    ip = os.getenv("PC_IP")
    port = int(os.getenv("PORT"))

    virtgamepad = VirtualGamepad()

    def callback(data):

        virtgamepad.read_input(data)

    receiver = Receiver(ip, port, callback)

    receiver.receive()

    gamepad_input = {"LAX": 0, "LAY": 0, "RAX": 0, "RAY": 0, "R2": 0, "L2": 0, "L1": 0, "R1": 0, "DPY": 0, "DPX": 0, "A": 0, "X": 0, "B": 0, "Y": 0, "Select": 0, "Start": 0}

    

if __name__ == "__main__":
    main()