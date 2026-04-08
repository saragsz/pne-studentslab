import http.server
import socketserver
import termcolor

# Define the Server's port
PORT = 8080

# -- This is for preventing the error: "Port already in use"
socketserver.TCPServer.allow_reuse_address = True


# Class with our Handler. It is a called derived from BaseHTTPRequestHandler
# It means that our class inherits all his methods and properties
class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):

        import http.server
        import socketserver

        PORT = 8080

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
                except:
                    self.wfile.write(b"<h1>File not found</h1>")

        with socketserver.TCPServer(("", PORT), TestHandler) as httpd:
            print(f"Serving at port {PORT}")
            httpd.serve_forever()


# ------------------------
# - Server MAIN program
# ------------------------
# -- Set the new handler
Handler = TestHandler

# -- Open the socket server
with socketserver.TCPServer(("", PORT), Handler) as httpd:

    print("Serving at PORT", PORT)

    # -- Main loop: Attend the client. Whenever there is a new
    # -- clint, the handler is called
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stopped by the user")
        httpd.server_close()
