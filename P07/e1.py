import http.client
import json

server = "rest.ensembl.org"
endpoint = "/info/ping"
params = "?content-type=application/json"
url = server + endpoint + params

print()
print(f"Server:{server}")
print(f"URL: {url}")

conn = http.client.HTTPConnection(server)

try:
    conn.request("GET", endpoint + params)
except ConnectionRefusedError:
    print("ERROR! Cannot connect to the Server")
    exit()

response = conn.getresponse()

print(f"Response received!: {response.status} {response.reason}")
print()

data = response.read().decode("utf-8")
parsed_data = json.loads(data)

if parsed_data.get("ping") == 1:
    print("PING OK! The database is running!")
else:
    print("Failed to reach the database")