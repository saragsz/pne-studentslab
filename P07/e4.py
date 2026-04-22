import http.client
import json
import termcolor
from Seq1 import Seq

genes = {
    "FRAT1": "ENSG00000165879", "ADA": "ENSG00000196839", "FXN": "ENSG00000165060",
    "RNU6_269P": "ENSG00000212379", "MIR633": "ENSG00000207552", "TTTY4C": "ENSG00000228296",
    "RBMY2YP": "ENSG00000227633", "FGFR3": "ENSG00000068078", "KDR": "ENSG00000128052",
    "ANK2": "ENSG00000145362"
}


gene_name = input("Write the gene name: ")

if gene_name in genes:
    gene_id = genes[gene_name]

    server = "rest.ensembl.org"
    endpoint = f"/sequence/id/{gene_id}"
    params = "?content-type=application/json"
    url = server + endpoint + params

    print(f"\nServer: {server}")
    print(f"URL: {url}")

    conn = http.client.HTTPConnection(server)
    conn.request("GET", endpoint + params)
    response = conn.getresponse()

    print(f"Response received!: {response.status} {response.reason}\n")

    if response.status == 200:
        data = json.loads(response.read().decode("utf-8"))

        termcolor.cprint("Gene: ", 'green', end='')
        print(gene_name)
        termcolor.cprint("Description: ", 'green', end='')
        print(data.get('desc', 'No description available'))

        seq_obj = Seq(data.get("seq", ""))

        total_len = seq_obj.len()
        termcolor.cprint("Total lengh: ", 'green', end='')
        print(total_len)

        counts = seq_obj.count()
        if total_len > 0:
            for base in ['A', 'C', 'G', 'T']:
                termcolor.cprint(f"{base}: ", 'blue', end='')
                count = counts.get(base, 0)
                pct = (count / total_len) * 100
                print(f"{count} ({pct:.1f}%)")

            most_freq = max(counts, key=counts.get)
            termcolor.cprint("Most frequent Base: ", 'green', end='')
            print(most_freq)
    else:
        print("Error fetching data from server.")
else:
    print("Gene not found in dictionary.")