import http.server
import socketserver
from pathlib import Path
from urllib.parse import urlparse, parse_qs
import json
import http.client
import jinja2 as j

from Seq1 import Seq

PORT = 8080

socketserver.TCPServer.allow_reuse_address = True


class ProjectHandler(http.server.BaseHTTPRequestHandler):

    def read_html(self, filename):
        file_path = Path(filename)
        if file_path.exists():
            contents = file_path.read_text(encoding="utf-8")
            return j.Template(contents)
        else:
            return j.Template("<html><body><h1> File not found</h1></body></html>")

    def ensembl_data(self, endpoint):
        server = "rest.ensembl.org"
        conn = http.client.HTTPConnection(server)
        if "?" in endpoint:
            params = "&content-type=application/json"
        else:
            params = "?content-type=application/json"

        try:
            conn.request("GET", endpoint + params)
            response = conn.getresponse()
            if response.status == 200:
                data = json.loads(response.read().decode("utf-8"))
                return data
            else:
                print(f"Ensembl error: {response.status} in {endpoint}")
                return None
        except ConnectionRefusedError:
            print("ERROR! Cannot connect to the Server")
            exit()

    def render_response(self, params, template_name, context_data=None):
        json_param = params.get("json", ["0"])[0]

        if json_param == "1":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            data_to_send = context_data if context_data is not None else {}
            self.wfile.write(json.dumps(data_to_send).encode("utf-8"))
        else:
            template = self.read_html(template_name)
            if context_data is not None:
                html_final = template.render(context=context_data)
            else:
                html_final = template.render()

            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(html_final.encode("utf-8"))

    def do_GET(self):
        parsed_url = urlparse(self.path)
        endpoint = parsed_url.path
        query_params = parse_qs(parsed_url.query)

        if endpoint == "/":
            self.handle_main_page(query_params)
        elif endpoint == "/listSpecies":
            self.handle_list_species(query_params)
        elif endpoint == "/karyotype":
            self.handle_karyotype(query_params)
        elif endpoint == "/chromosomeLength":
            self.handle_chromosome_length(query_params)
        elif endpoint == "/geneLookup":
            self.handle_gene_lookup(query_params)
        elif endpoint == "/geneSeq":
            self.handle_gene_seq(query_params)
        elif endpoint == "/geneInfo":
            self.handle_gene_info(query_params)
        elif endpoint == "/geneCalc":
            self.handle_gene_calc(query_params)
        elif endpoint == "/geneList":
            self.handle_gene_list(query_params)
        else:
            self.handle_error(query_params)

    def handle_main_page(self, params):
        self.render_response(params, "html/main.html")

    def handle_list_species(self, params):
        limit = params.get("limit", [None])[0]

        ensembl_data = self.ensembl_data("/info/species")
        if not ensembl_data:
            self.handle_error(params)
            return
        species_list = ensembl_data.get('species', [])
        total_species = len(species_list)

        limit_str = limit if limit and limit.isdigit() else "Todos"
        if limit and limit.isdigit():
            species_list = species_list[:int(limit)]

        items_html = ""
        raw_species_names = []
        for s in species_list:
            name = s.get('display_name', 'Unknown')
            items_html += f"<li>{name}</li>\n"
            raw_species_names.append(name)

        context_data = {
            "total_species": total_species,
            "limit": limit_str,
            "list_species": items_html,
            "raw_species_names": raw_species_names
        }
        self.render_response(params, "html/species.html", context_data)

    def handle_karyotype(self, params):
        species = params.get("species", [""])[0]
        if not species:
            self.handle_error(params)
            return

        safe_species = species.replace(" ", "%20")
        ensembl_data = self.ensembl_data(f"/info/assembly/{safe_species}")

        if not ensembl_data or 'karyotype' not in ensembl_data:
            self.handle_error(params)
            return

        karyotype = ensembl_data['karyotype']
        items_html = ""
        for chromo in karyotype:
            items_html += f"<li>{chromo}</li>\n"

        context_data = {
            "specie": species,
            "chromosomes": items_html,
            "raw_chromosomes": karyotype
        }
        self.render_response(params, "html/karyotype.html", context_data)

    def handle_chromosome_length(self, params):
        species = params.get("species", [""])[0]
        chromo_target = params.get("chromo", [""])[0]

        if not species or not chromo_target:
            self.handle_error(params)
            return

        safe_species = species.replace(" ", "%20")
        ensembl_data = self.ensembl_data(f"/info/assembly/{safe_species}")

        if not ensembl_data or 'top_level_region' not in ensembl_data:
            self.handle_error(params)
            return

        length = "Not found"
        for region in ensembl_data['top_level_region']:
            if region['name'] == chromo_target:
                length = str(region['length'])
                break

        if length == "Not found":
            self.handle_error(params)
            return

        context_data = {
            "specie": species,
            "chromosome": chromo_target,
            "length": length
        }
        self.render_response(params, "html/chromosome.html", context_data)

    def handle_gene_lookup(self, params):
        gene_name = params.get("gene", [""])[0]
        if not gene_name:
            self.handle_error(params)
            return

        ensembl_data = self.ensembl_data(f"/lookup/symbol/homo_sapiens/{gene_name}")

        if not ensembl_data or 'id' not in ensembl_data:
            self.handle_error(params)
            return

        context_data = {
            "gene_name": gene_name,
            "gene_id": ensembl_data['id'],
        }
        self.render_response(params, "html/gene_lookup.html", context_data)

    def handle_gene_seq(self, params):
        gene_name = params.get("gene", [""])[0]
        if not gene_name:
            self.handle_error(params)
            return

        lookup_data = self.ensembl_data(f"/lookup/symbol/homo_sapiens/{gene_name}")
        if not lookup_data or 'id' not in lookup_data:
            self.handle_error(params)
            return

        seq_data = self.ensembl_data(f"/sequence/id/{lookup_data['id']}")
        if not seq_data or 'seq' not in seq_data:
            self.handle_error(params)
            return

        my_seq = Seq(seq_data['seq'])

        context_data = {
            "gene_name": gene_name,
            "sequence": str(my_seq)
        }
        self.render_response(params, "html/gene_seq.html", context_data)

    def handle_gene_info(self, params):
        gene_name = params.get("gene", [""])[0]
        if not gene_name:
            self.handle_error(params)
            return

        ensembl_data = self.ensembl_data(f"/lookup/symbol/homo_sapiens/{gene_name}")
        if not ensembl_data or 'id' not in ensembl_data:
            self.handle_error(params)
            return

        start = ensembl_data['start']
        end = ensembl_data['end']

        context_data = {
            "gene_name": gene_name,
            "gene_id": ensembl_data['id'],
            "chromosome": ensembl_data['seq_region_name'],
            "start": start,
            "end": end,
            "length": end - start + 1
        }
        self.render_response(params, "html/gene_info.html", context_data)

    def handle_gene_calc(self, params):
        gene_name = params.get("gene", [""])[0]
        if not gene_name:
            self.handle_error(params)
            return

        lookup_data = self.ensembl_data(f"/lookup/symbol/homo_sapiens/{gene_name}")
        if not lookup_data or 'id' not in lookup_data:
            self.handle_error(params)
            return

        seq_data = self.ensembl_data(f"/sequence/id/{lookup_data['id']}")
        if not seq_data or 'seq' not in seq_data:
            self.handle_error(params)
            return

        my_seq = Seq(seq_data['seq'])
        total_length = my_seq.len()
        counts = my_seq.count()

        if total_length > 0:
            perc_A = round((counts.get('A', 0) / total_length) * 100, 2)
            perc_C = round((counts.get('C', 0) / total_length) * 100, 2)
            perc_G = round((counts.get('G', 0) / total_length) * 100, 2)
            perc_T = round((counts.get('T', 0) / total_length) * 100, 2)
        else:
            perc_A = perc_C = perc_G = perc_T = 0

        context_data = {
            "gene_name": gene_name,
            "length": total_length,
            "count_A": counts.get('A', 0), "perc_A": perc_A,
            "count_C": counts.get('C', 0), "perc_C": perc_C,
            "count_G": counts.get('G', 0), "perc_G": perc_G,
            "count_T": counts.get('T', 0), "perc_T": perc_T
        }
        self.render_response(params, "html/gene_calc.html", context_data)

    def handle_gene_list(self, params):
        chromo = params.get("chromo", [""])[0].strip()
        start = params.get("start", [""])[0].strip()
        end = params.get("end", [""])[0].strip()

        if not chromo or not start or not end:
            self.handle_error(params)
            return

        endpoint = f"/overlap/region/human/{chromo}:{start}-{end}?feature=gene"
        ensembl_data = self.ensembl_data(endpoint)

        if ensembl_data is None or not isinstance(ensembl_data, list):
            self.handle_error(params)
            return

        items_html = ""
        raw_gene_names = []
        for gene in ensembl_data:
            name = gene.get('external_name', gene.get('id', 'Unknown'))
            items_html += f"<li>{name}</li>\n"
            raw_gene_names.append(name)

        if not items_html:
            items_html = "<li>No genes found in this region.</li>"

        context_data = {
            "chromo": chromo,
            "start": start,
            "end": end,
            "gene_list_html": items_html,
            "raw_gene_names": raw_gene_names
        }
        self.render_response(params, "html/gene_list.html", context_data)

    def handle_error(self, params):
        self.send_response(404)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        template = self.read_html("html/error.html")
        self.wfile.write(template.render().encode("utf-8"))

if __name__ == "__main__":
    with socketserver.TCPServer(("", PORT), ProjectHandler) as httpd:
        print(f"Server running on port: {PORT}")
        print(f"Open in your browser: http://localhost:{PORT}")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServer stopped by the user.")
            httpd.server_close()
