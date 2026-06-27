from receiver import Receiver
from dotenv import load_dotenv
import os

load_dotenv()

def main():

    port = int(os.getenv("PORT"))

    receiver = Receiver("0.0.0.0", port) # Olha para todas as interfaces de rede na porta especificada

    receiver.receive()

if __name__ == "__main__":
    main()