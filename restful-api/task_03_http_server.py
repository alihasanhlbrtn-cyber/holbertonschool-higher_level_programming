#!/usr/bin/python3
"""
Simple HTTP API server using Python's http.server module.

Endpoints:
    GET /          -> "Hello, this is a simple API!"
    GET /data      -> JSON: {"name": "John", "age": 30, "city": "New York"}
    GET /status    -> "OK"
    GET /info      -> JSON: {"version": "1.0", "description": "..."}
    Any other path -> 404 "Endpoint not found"
"""

from http.server import HTTPServer, BaseHTTPRequestHandler
import json


class SimpleAPIHandler(BaseHTTPRequestHandler):
    

    def _set_headers(self, status_code=200, content_type="text/plain"):
    
        self.send_response(status_code)
        self.send_header("Content-Type", content_type)
        self.end_headers()

    def do_GET(self):
    
        if self.path == "/":
            
            self._set_headers(200, "text/plain; charset=utf-8")
            self.wfile.write(b"Hello, this is a simple API!")

        elif self.path == "/data":
            
            data = {"name": "John", "age": 30, "city": "New York"}
            self._set_headers(200, "application/json; charset=utf-8")
            self.wfile.write(json.dumps(data).encode("utf-8"))

        elif self.path == "/status":
            
            self._set_headers(200, "text/plain; charset=utf-8")
            self.wfile.write(b"OK")

        elif self.path == "/info":
            
            info = {
                "version": "1.0",
                "description": "A simple API built with http.server"
            }
            self._set_headers(200, "application/json; charset=utf-8")
            self.wfile.write(json.dumps(info).encode("utf-8"))

        else:
            
            self._set_headers(404, "text/plain; charset=utf-8")
            self.wfile.write(b"Endpoint not found")


def run(server_class=HTTPServer, handler_class=SimpleAPIHandler):

    server_address = ("", 8000)  
    httpd = server_class(server_address, handler_class)
    print("Starting simple API server on port 8000...")
    httpd.serve_forever()


if __name__ == "__main__":
    run()
