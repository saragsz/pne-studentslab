import http.server
import socketserver
import termcolor
from pathlib import Path

PORT = 8080

socketserver.TCPServer.allow_reuse_address = True

BASE_PATH = Path("html")

class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        """Called whenever the client sends a GET request"""

        termcolor.cprint(self.requestline, 'green')

        requested_path = self.path.lstrip("/")

        if requested_path == "":
            requested_path = "index.html"

        file_path = BASE_PATH / requested_path

        try:
            content = file_path.read_text()
            self.send_response(200)

        except FileNotFoundError:

            error_path = BASE_PATH / "error.html"

            try:
                content = error_path.read_text()
            except FileNotFoundError:
                content = "<h1>Error file not found</h1>"

            self.send_response(404)


        self.send_header("Content-Type", "text/html")
        self.send_header("Content-Length", len(content.encode()))
        self.end_headers()

        self.wfile.write(content.encode())


Handler = TestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Serving at PORT", PORT)

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nStopped by the user")
        httpd.server_close()