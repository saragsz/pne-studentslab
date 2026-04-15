import http.server
import socketserver
import termcolor
from pathlib import Path
from urllib.parse import urlparse, parse_qs

from Seq1 import Seq

PORT = 8080

socketserver.TCPServer.allow_reuse_address = True

seq_list = ["ACGT", "TGCT", "CCGA", "GTAC", "ACCT"]


class SeqHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):

        termcolor.cprint(self.requestline, 'green')

        url = urlparse(self.path)
        path = url.path
        params = parse_qs(url.query)

        content = ""

        if path == "/":
            content = Path("html/index.html").read_text()
            code = 200

        elif path == "/ping":
            content = Path("html/ping.html").read_text()
            code = 200

        elif path == "/get":
            n = int(params["n"][0])
            sequence = seq_list[n]

            content = Path("html/get.html").read_text()
            content = content.replace("{{number}}", str(n))
            content = content.replace("{{sequence}}", sequence)
            code = 200

        elif path == "/gene":
            name = params["name"][0]

            file = f"../S04/sequences/{name}.txt"
            seq = Seq()
            seq.read_fasta(file)

            content = Path("html/gene.html").read_text()
            content = content.replace("{{gene}}", name)
            content = content.replace("{{sequence}}", str(seq))
            code = 200

        elif path == "/operation":
            sequence = params["seq"][0].upper()
            op = params["op"][0]

            seq = Seq(sequence)
            result = ""

            if op == "info":
                counts = seq.count()
                length = len(sequence)

                result += f"<p>Total length: {length}</p>"

                for k, v in counts.items():
                    perc = round((v / length) * 100, 2)
                    result += f"<p>{k}: {v} ({perc}%)</p>"

            elif op == "comp":
                result = seq.complement()

            elif op == "rev":
                result = seq.reverse()

            content = Path("html/operation.html").read_text()
            content = content.replace("{{result}}", result)
            content = content.replace("{{sequence}}", sequence)
            content = content.replace("{{op}}", op)
            code = 200

        else:
            content = Path("html/error.html").read_text()
            code = 404

        self.send_response(code)
        self.send_header("Content-Type", "text/html")
        self.send_header("Content-Length", str(len(content.encode())))
        self.end_headers()

        self.wfile.write(content.encode())


with socketserver.TCPServer(("", PORT), SeqHandler) as server:
    print(f"Seq2 Server running on PORT {PORT}")
    server.serve_forever()







