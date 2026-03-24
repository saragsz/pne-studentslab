import socket

HOST = "127.0.0.1"
PORT = 8080

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

print("Connected to the game!")

finished = False

while not finished:
    guess = input("Enter your guess (1-100): ")

    client.send(guess.encode())

    response = client.recv(1024).decode()
    print("Server says:", response)

    if "You won" in response:
        finished = True

client.close()
print("Game finished")