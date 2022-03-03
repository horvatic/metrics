from http.server import BaseHTTPRequestHandler
import response

class MetricsServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(bytes(response.build(), "utf-8"))