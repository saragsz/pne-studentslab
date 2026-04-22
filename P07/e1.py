import http.client
import json

SERVER = "rest.ensembl.org"
ENDPOINT = "/info/ping"
PARAMS = "?content-type=application/json"
URL = SERVER + ENDPOINT + PARAMS

print()
print(f"Server:{SERVER}")
print(f"URL: {URL}")

conn = http.client.HTTPConnection(SERVER)
conn.request("GET", ENDPOINT + PARAMS)
response = conn.getresponse()

print(f"Response received!: {response.status} {response.reason}")
print()

data = response.read().decode("utf-8")
parsed_data = json.loads(data)

if parsed_data.get("ping") == 1:
    print("PING OK! The database is running!")
else:
    print("Failed to reach the database")