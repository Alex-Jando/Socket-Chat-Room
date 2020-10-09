import socket
import threading

HOST = "127.0.0.1"

PORT = 5551

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((HOST, PORT))

nicknames = list()
clients = list()

s.listen()

def broadcast(message):
	try:
		for client in clients:

			client.send(message.encode())
		print(message)
	except:
		print(message)

def join():

	while True:

		client, address = s.accept()

		print(client)

		client.send("!@..894dfh//]".encode())

		nickname = client.recv(1024).decode()

		clients.append(client)
		nicknames.append(nickname)

		print(f"{address} has joined with the name of {nickname}")

		broadcast(f"{nickname} has join the chat!")

		thread = threading.Thread(target=recive, args=(client,nickname,), daemon = True)
		thread.start()

def recive(client, nickname):

	while True:

		try:
			message = client.recv(1024)

		except:

			broadcast(f"{nickname} has left the chat.")

			client.close()

			nicknames.remove(nicknames[clients.index(client)])
			clients.remove(clients[clients.index(client)])

			break

		else:
			broadcast(message.decode())

join()