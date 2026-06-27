from receiver import Receiver

def main():

    receiver = Receiver("0.0.0.0", 5005) # Olha para todas as interfaces de rede na porta 5005

    receiver.receive()

if __name__ == "__main__":
    main()