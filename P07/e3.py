import http.client
import json
import termcolor

genes = {
    "FRAT1": "ENSG00000165879", "ADA": "ENSG00000196839", "FXN": "ENSG00000165060",
    "RNU6_269P": "ENSG00000212379", "MIR633": "ENSG00000207552", "TTTY4C": "ENSG00000228296",
    "RBMY2YP": "ENSG00000227633", "FGFR3": "ENSG00000068078", "KDR": "ENSG00000128052",
    "ANK2": "ENSG00000145362"
}

gene_name = "MIR633"
gene_id = genes[gene_name]

server = "rest.ensembl.org"
endpoint = f"/sequence/id/{gene_id}"
params = "?content-type=application/json"
url = server + endpoint + params

print()
print(f"Server: {server}")
print(f"URL: {url}")

conn = http.client.HTTPConnection(server)

try:
    conn.request("GET", endpoint + params)
except ConnectionRefusedError:
    print("ERROR! Cannot connect to the Server")
    exit()

response = conn.getresponse()

print(f"Response received!: {response.status} {response.reason}\n")

if response.status == 200:
    data = json.loads(response.read().decode("utf-8"))
    description = data.get("desc", "No description available")
    seq = data.get("seq", "")

    termcolor.cprint("Gene:", "yellow", end = "")
    print(gene_name)

    termcolor.cprint("Description:", "yellow", end="")
    print(description)

    termcolor.cprint("Bases:", "yellow", end="")
    print(seq)
else:
    print(f"Error fetching data: HTTP {response.status}")