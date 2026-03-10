from Client0 import Client

IP = "212.128.255.90"
PORT = 8080

for i in range(5):

    msg = f"Message: {i}"
    print(f"To server: {msg}")
    client = Client(IP,PORT)
    response = client.talk(msg)
    print(f"From server: {response}")

