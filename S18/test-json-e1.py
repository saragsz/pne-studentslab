import http.client
import json
import termcolor

PORT = 8080
SERVER = 'localhost'

print(f"\nConnecting to server: {SERVER}:{PORT}\n")

conn = http.client.HTTPConnection(SERVER, PORT)

try:
    conn.request("GET", "/listusers")
except ConnectionRefusedError:
    print("ERROR! Cannot connect to the Server")
    exit()

response = conn.getresponse()
print(f"Response received!: {response.status} {response.reason}\n")

data = response.read().decode("utf-8")

data_json = json.loads(data)

print("CONTENT:\n")


people = data_json["people-e1"]

# Total de personas
print(f"Total people in the database: {len(people)}\n")


for person in people:
    termcolor.cprint("Name: ", 'green', end="")
    print(person["Firstname"], person["Lastname"])

    termcolor.cprint("Age: ", 'green', end="")
    print(person["age"])

    phone_numbers = person["phoneNumber"]

    termcolor.cprint("Phone numbers: ", 'green', end="")
    print(len(phone_numbers))

    for i, phone in enumerate(phone_numbers):
        termcolor.cprint(f"  Phone {i}:", 'blue')

        termcolor.cprint("    Type: ", 'red', end="")
        print(phone["type"])

        termcolor.cprint("    Number: ", 'red', end="")
        print(phone["number"])

    print()