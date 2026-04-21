import http.client
import json
import termcolor

conn = http.client.HTTPConnection("localhost", 8080)
conn.request("GET", "/listusers")

response = conn.getresponse()
data = response.read().decode()

people = json.loads(data)

print()

for person in people:
    termcolor.cprint("Name: ", 'green', end="")
    print(person['Firstname'], person['Lastname'])

    termcolor.cprint("Age: ", 'green', end="")
    print(person['age'])