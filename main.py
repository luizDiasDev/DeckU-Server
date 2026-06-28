from receiver import Receiver
from dotenv import load_dotenv
import os


def main():

    load_dotenv()

    ip = os.getenv("PC_IP")
    port = int(os.getenv("PORT"))

    receiver = Receiver(ip, port)

    receiver.receive()

if __name__ == "__main__":
    main()