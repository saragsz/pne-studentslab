import http.server
import socketserver
import termcolor
from pathlib import Path

PORT = 8080
socketserver.TCPServer.allow_reuse_address = True


class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        termcolor.cprint(self.requestline, 'green')

        list_resource = self.path.split('?')
        resource = list_resource[0]

        if resource == "/":
            # Si piden la raíz, enviamos un mensajito simple o un index
            contents = "<h1>Bienvenido a la API REST</h1><p>Ve a <a href='/listusers'>/listusers</a></p>"
            content_type = 'text/html'
            error_code = 200
        elif resource == "/listusers":
            # Aquí está la clave: leemos el JSON y lo preparamos para enviar
            try:
                contents = Path('people-e1.json').read_text()
                content_type = 'application/json'  # Cabecera crucial para APIs REST
                error_code = 200
            except FileNotFoundError:
                contents = '{"error": "Database not found"}'
                content_type = 'application/json'
                error_code = 404
        else:
            contents = Path ('error.html').read_text()
            content_type = 'text/html'
            error_code = 404

        # Generar la respuesta HTTP
        self.send_response(error_code)
        self.send_header('Content-Type', content_type)
        self.send_header('Content-Length', len(contents.encode('utf-8')))
        self.end_headers()
        self.wfile.write(contents.encode('utf-8'))

with socketserver.TCPServer(("", PORT), TestHandler) as httpd:
    print("Serving at PORT", PORT)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nStopped by the user")
        httpd.server_close()
