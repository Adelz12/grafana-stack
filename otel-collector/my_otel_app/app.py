import http.server
import socketserver
import time
import os

# Using standard library to avoid network/pip issues
PORT = 8000

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(b"<h1>Hello from Standard Python!</h1>")
            self.wfile.write(b"<p>Instrumented by <b>Beyla (eBPF)</b> - Zero Code needed!</p>")
        elif self.path == "/slow":
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            time.sleep(1) # Simulate slow response
            self.wfile.write(b"<h1>Slow Response</h1><p>Beyla will capture this delay automatically.</p>")
        elif self.path == "/fast":
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(b"<h1>Fast Response</h1>")
        else:
            self.send_response(404)
            self.end_headers()

if __name__ == "__main__":
    print(f"Starting server on port {PORT}...")
    with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
        httpd.serve_forever()
