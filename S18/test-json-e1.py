import json
import termcolor
from pathlib import Path

# Leer el archivo JSON
jsonstring = Path("people-e1.json").read_text()

# Convertir JSON → lista de Python
people = json.loads(jsonstring)

print()

# Número total de personas
termcolor.cprint("Total people: ", 'green', end="")
print(len(people))
print()

# Recorrer todas las personas
for i, person in enumerate(people):
    termcolor.cprint(f"Person {i+1}", 'blue')

    termcolor.cprint("  Name: ", 'green', end="")
    print(person['Firstname'], person['Lastname'])

    termcolor.cprint("  Age: ", 'green', end="")
    print(person['age'])

    phoneNumbers = person['phoneNumber']

    termcolor.cprint("  Phone numbers: ", 'green', end="")
    print(len(phoneNumbers))

    for j, phone in enumerate(phoneNumbers):
        termcolor.cprint(f"    Phone {j+1}:", 'red')
        print("      Type:", phone['type'])
        print("      Number:", phone['number'])

    print()