import socket
import random

class NumberGuesser:
    def __init__(self) -> None:
        self.secret_number = random.randint(1, 100)
        self.attempts = []
        self.finished = False   # 👈 control del juego

    def guess(self, number):
        number = int(number)
        self.attempts.append(number)

        if number == self.secret_number:
            self.finished = True
            return f"You won after {len(self.attempts)} attempts"
        elif number > self.secret_number:
            return "Lower"
        else:
            return "Higher"


HOST = "127.0.0.1"
PORT = 8080

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

print("Server is running...")

while True:
    cs, addr = server.accept()
    print(f"Connected by {addr}")

    game = NumberGuesser()

    data = cs.recv(1024).decode()

    while data and not game.finished:
        response = game.guess(data)
        cs.send(response.encode())

        if not game.finished:
            data = cs.recv(1024).decode()
        else:
            data = None

    cs.close()
    print("Connection closed")