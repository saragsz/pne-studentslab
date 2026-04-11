import http.server
import socketserver

# Define the Server's port
PORT = 8080

# Prevent "Port already in use"
socketserver.TCPServer.allow_reuse_address = True


class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):

        path = self.path

        if path == "/" or path == "/index.html":
            filename = "index.html"
            self.send_response(200)
        else:
            filename = "error.html"
            self.send_response(404)

        self.send_header("Content-type", "text/html")
        self.end_headers()

        try:
            with open(filename, "r") as f:
                content = f.read()
                self.wfile.write(content.encode())
        except FileNotFoundError:
            self.wfile.write(b"<h1>File not found</h1>")

# Server MAIN program
Handler = TestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Serving at PORT", PORT)

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nStopped by the user")
        httpd.server_close()