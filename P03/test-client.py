from Client0 import Client

PORT = 8080
IP = "127.0.0.1"

c = Client(IP,PORT)
print("-----| Practice 3, Exercise 7 |------")
print(c)

print("*Testing PING...")
response = c.talk("PING")
print(response,"\n")

print("*Testing GET...")
seq = ""
for i in range(5):
    msg = f"GET {i}"
    response = c.talk(msg)
    print(f"{msg}:{response} \n")
    if i == 0:
        later_seq = response

print("*Testing INFO...")
response = c.talk(f"INFO {later_seq}")
print(response)

print("*Testing COMP...")
response = c.talk(f"COMP {later_seq}")
print(response)
print(f"Seq: {later_seq}")
print(f"COMP: {response} \n")

print("*Testing REV...")
response = c.talk(f" REV {later_seq}")
print(response)
print(f"Seq: {later_seq}")
print(f"REV: {response} \n")

print("*Testing GENE...")
genes = ["U5","ADA","FRAT1","FXN","RNU6_269P"]
for gen in genes:
    print(f"GENE {gen} ")
    response = c.talk(f"GENE {gen}")
    print(response)


