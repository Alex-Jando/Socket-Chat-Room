import socket
import threading
import sys

HOST = sys.argv[1]

PORT = int(sys.argv[2])

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

nickname = input("Enter Your Nickname: ")

s.connect((HOST,PORT))

def recive():

    while True:

        message = s.recv(1024).decode()
         
        if message == "!@..894dfh//]":
            s.send(nickname.encode())

        else:

            print(message)

def send():

    while True:

        message = input(">>>")

        message = f"{nickname}: {message}".encode()

        s.send(message)

thread1 = threading.Thread(target=recive)
thread1.start()
thread2 = threading.Thread(target=send)
thread2.start()


