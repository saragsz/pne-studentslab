import http.server
import socketserver
import termcolor
from pathlib import Path
from urllib.parse import parse_qs, urlparse
import jinja2 as j

PORT = 8080

socketserver.TCPServer.allow_reuse_address = True


def read_html_file(filename):
    contents = Path("html/" + filename).read_text()
    contents = j.Template(contents)
    return contents


class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        termcolor.cprint(self.requestline, 'green')

        url_path = urlparse(self.path)
        path = url_path.path
        arguments = parse_qs(url_path.query)

        # MAIN PAGE
        if path == "/":
            contents = Path("html/form-1.html").read_text()

            self.send_response(200)
            self.send_header('Content-Type', 'text/html')
            self.send_header('Content-Length', len(contents.encode()))
            self.end_headers()

            self.wfile.write(contents.encode())

        # ECHO
        elif path == "/echo":
            msg = arguments.get("msg", [""])[0]

            contents = read_html_file("echo.html").render(
                context={"todisplay": msg}
            )

            self.send_response(200)
            self.send_header('Content-Type', 'text/html')
            self.send_header('Content-Length', len(contents.encode()))
            self.end_headers()

            self.wfile.write(contents.encode())

        # ERROR
        else:
            contents = Path("html/error.html").read_text()

            self.send_response(404)
            self.send_header('Content-Type', 'text/html')
            self.send_header('Content-Length', len(contents.encode()))
            self.end_headers()

            self.wfile.write(contents.encode())


Handler = TestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Serving at PORT", PORT)

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nStopped by user")
        httpd.server_close()