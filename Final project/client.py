import http.client
import json

SERVER = "localhost"
PORT = 8080

print(f"Conectando al servidor {SERVER}:{PORT}...")


conn = http.client.HTTPConnection(SERVER, PORT)

endpoint = "/geneInfo?gene=FRAT1&json=1"

try:
    print(f"Asking data to: {endpoint}")
    conn.request("GET", endpoint)
    response = conn.getresponse()

    if response.status == 200:
        data_string = response.read().decode("utf-8")
        data_json = json.loads(data_string)

        print("\n--- DATA RECEIVED BY THE SERVER ---")
        print(f"Gen: {data_json['gene_name']}")
        print(f"ID Ensembl: {data_json['gene_id']}")
        print(f"Chromosome: {data_json['chromosome']}")
        print(f"Length: {data_json['length']} pares de bases")
        print("------------------------------------")
    else:
        print(f"Error: {response.status}")

except ConnectionRefusedError:
    print("Error")