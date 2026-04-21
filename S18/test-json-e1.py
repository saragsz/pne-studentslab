import json
import termcolor
from pathlib import Path

# 1. Leer el archivo JSON
jsonstring = Path("people-e1.json").read_text()

# 2. Convertir el texto JSON a una lista de objetos de Python
people = json.loads(jsonstring)

# 3. Imprimir el total de personas
print(f"Total people in the database:  {len(people)}\n")

# 4. Recorrer la lista de personas e imprimir la información
for person in people:
    # Nombre
    termcolor.cprint("Name: ", 'green', end='')
    print(f"{person['Firstname']} {person['Lastname']}")

    # Edad
    termcolor.cprint("Age: ", 'green', end='')
    print(person['age'])

    # Teléfonos
    phone_numbers = person['phoneNumber']
    termcolor.cprint("Phone numbers: ", 'green', end='')
    print(len(phone_numbers))

    for i, phone in enumerate(phone_numbers):
        # Indice del teléfono
        termcolor.cprint(f"  Phone {i}:", 'blue')
        # Tipo
        termcolor.cprint("    Type: ", 'red', end='')
        print(phone['type'])
        # Número
        termcolor.cprint("    Number: ", 'red', end='')
        print(phone['number'])
    print() # Salto de línea entre personas
