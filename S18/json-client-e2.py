import http.client
import json
import termcolor

PORT = 8080
SERVER = 'localhost'

print(f"\nConnecting to server: {SERVER}:{PORT}\n")

# 1. Conectar con el servidor
conn = http.client.HTTPConnection(SERVER, PORT)

try:
    # 2. Hacer la petición GET a /listusers
    conn.request("GET", "/listusers")
except ConnectionRefusedError:
    print("ERROR! Cannot connect to the Server")
    exit()

# 3. Recibir la respuesta
r1 = conn.getresponse()
print(f"Response received!: {r1.status} {r1.reason}\n")

if r1.status == 200:
    # 4. Leer y decodificar el cuerpo de la respuesta (el texto JSON)
    json_data = r1.read().decode("utf-8")

    # 5. Convertir el texto JSON a lista de Python
    people = json.loads(json_data)

    # --- A partir de aquí es exactamente igual que el Ejercicio 1 ---
    print(f"Total people in the database:  {len(people)}\n")

    for person in people:
        termcolor.cprint("Name: ", 'green', end='')
        print(f"{person['Firstname']} {person['Lastname']}")

        termcolor.cprint("Age: ", 'green', end='')
        print(person['age'])

        phone_numbers = person['phoneNumber']
        termcolor.cprint("Phone numbers: ", 'green', end='')
        print(len(phone_numbers))

        for i, phone in enumerate(phone_numbers):
            termcolor.cprint(f"  Phone {i}:", 'blue')
            termcolor.cprint("    Type: ", 'red', end='')
            print(phone['type'])
            termcolor.cprint("    Number: ", 'red', end='')
            print(phone['number'])
        print()
else:
    print("Error al obtener los datos del servidor.")