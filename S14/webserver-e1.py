import http.server
import socketserver
import termcolor

# Define the Server's port
PORT = 8080

# Prevent "Port already in use"
socketserver.TCPServer.allow_reuse_address = True


class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        """Called whenever the client sends a GET request"""

        # Print request line
        termcolor.cprint(self.requestline, 'green')

        # Check requested resource
        if self.path == "/":
            contents = "Welcome to my server"
            self.send_response(200)
        else:
            contents = "Resource not available"
            self.send_response(404)

        # Headers
        self.send_header('Content-Type', 'text/plain')
        self.send_header('Content-Length', len(contents.encode()))
        self.end_headers()

        # Body
        self.wfile.write(contents.encode())

        return

# Server MAIN program
Handler = TestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Serving at PORT", PORT)

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nStopped by the user")
        httpd.server_close()