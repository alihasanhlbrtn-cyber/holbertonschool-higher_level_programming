#!/usr/bin/python3
"""
Simple HTTP API server using Python's http.server module.

Endpoints:
    GET /          -> "Hello, this is a simple API!"
    GET /data      -> JSON: {"name": "John", "age": 30, "city": "New York"}
    GET /status    -> "OK"
    Any other path -> 404 "Endpoint not found"
"""

from http.server import HTTPServer, BaseHTTPRequestHandler
import json


class SimpleAPIHandler(BaseHTTPRequestHandler):
    """Custom request handler for a simple HTTP API."""

    def _set_headers(self, status_code=200, content_type="text/plain"):
        """Helper to send status line and headers."""
        self.send_response(status_code)
        self.send_header("Content-Type", content_type)
        self.end_headers()

    def do_GET(self):
        """Handle GET requests for different endpoints."""
        if self.path == "/":
            # Root endpoint
            self._set_headers(200, "text/plain")
            self.wfile.write(b"Hello, this is a simple API!")

        elif self.path == "/data":
            # Serve JSON data
            data = {"name": "John", "age": 30, "city": "New York"}
            # Tests expect exactly: application/json
            self._set_headers(200, "application/json")
            self.wfile.write(json.dumps(data).encode("utf-8"))

        elif self.path == "/status":
            # Status endpoint
            self._set_headers(200, "text/plain")
            self.wfile.write(b"OK")

        else:
            # Undefined endpoint -> 404
            self._set_headers(404, "text/plain")
            self.wfile.write(b"Endpoint not found")


def run(server_class=HTTPServer, handler_class=SimpleAPIHandler):
    """Start the HTTP server on port 8000."""
    server_address = ("", 8000)  # listen on all interfaces, port 8000
    httpd = server_class(server_address, handler_class)
    print("Starting simple API server on port 8000...")
    httpd.serve_forever()


if __name__ == "__main__":
    run()
