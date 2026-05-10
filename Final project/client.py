import http.client
import json

SERVER = "localhost"
PORT = 8080


def make_request(endpoint):
    try:
        conn = http.client.HTTPConnection(SERVER, PORT)
        conn.request("GET", endpoint)
        response = conn.getresponse()

        if response.status == 200:
            data_string = response.read().decode("utf-8")
            return json.loads(data_string)
        else:
            print(f"HTTP Error: {response.status}")
            return None
    except ConnectionRefusedError:
        print("Error: Could not connect. Is server.py running?")
        return None


def main():
    print("--------------------------------------------------")
    print("             REST API CLIENT TEST                 ")
    print("--------------------------------------------------")

    # 1. Test data endpoint: Gene Info
    print("\n[Test 1] Getting data for FRAT1 gene...")
    gene_data = make_request("/geneInfo?gene=FRAT1&json=1")

    if gene_data:
        print(f"Success! The gene {gene_data['gene_name']} (ID: {gene_data['gene_id']})")
        print(f"is located on chromosome {gene_data['chromosome']}")
        print(f"and has a length of {gene_data['length']} bases.")

    # 2. Test list endpoint: Species list
    print("\n[Test 2] Getting a list of 3 species...")
    species_data = make_request("/listSpecies?limit=3&json=1")

    if species_data:
        print(f"Success! The database has {species_data['total_species']} species in total.")
        print("The first 3 species extracted from the JSON are:")
        for species in species_data['raw_species_names']:
            print(f"  - {species}")

    print("\n--------------------------------------------------")

if __name__ == "__main__":
    main()