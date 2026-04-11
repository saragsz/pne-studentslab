import http.server
import socketserver
import termcolor
from pathlib import Path

# Define the Server's port
PORT = 8080

# Prevent "Port already in use"
socketserver.TCPServer.allow_reuse_address = True


class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        """Called whenever the client sends a GET request"""

        # Print request line
        termcolor.cprint(self.requestline, 'green')

        # Remove initial "/"
        requested_path = self.path.lstrip("/")

        if requested_path == "":
            requested_path = "index.html"

        file_path = Path(requested_path)

        try:
            content = file_path.read_text()
            self.send_response(200)

        except FileNotFoundError:
            error_file = Path("error.html")

            try:
                content = error_file.read_text()
            except FileNotFoundError:
                content = "<h1>Error file not found</h1>"

            self.send_response(404)

        # Headers
        self.send_header("Content-Type", "text/html")
        self.send_header("Content-Length", len(content.encode()))
        self.end_headers()

        # Body
        self.wfile.write(content.encode())

        return


# ------------------------
# Server MAIN program
# ------------------------
Handler = TestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Serving at PORT", PORT)

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nStopped by the user")
        httpd.server_close()