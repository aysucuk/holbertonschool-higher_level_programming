import json
from http.server import BaseHTTPRequestHandler, HTTPServer

class SimpleAPIHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Route to handle root URL
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        # Route to serve JSON data
        elif self.path == '/data':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            data = {
                "name": "John",
                "age": 30,
                "city": "New York"
            }
            self.wfile.write(json.dumps(data).encode('utf-8'))

        # Route to serve API status
        elif self.path == '/status':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            status = {
                "status": "OK"
            }
            self.wfile.write(json.dumps(status).encode('utf-8'))

        # Route to serve API info
        elif self.path == '/info':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            info = {
                "version": "1.0",
                "description": "A simple API built with http.server"
            }
            self.wfile.write(json.dumps(info).encode('utf-8'))

        # Handle undefined endpoints
        else:
            self.send_response(404)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            error_message = {
                "error": "Not Found",
                "message": f"The endpoint '{self.path}' is not available."
            }
            self.wfile.write(json.dumps(error_message).encode('utf-8'))

def run(server_class=HTTPServer, handler_class=SimpleAPIHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting http server on port {port}...')
    httpd.serve_forever()

if __name__ == '__main__':
    run()

