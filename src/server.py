from http.server import BaseHTTPRequestHandler, HTTPServer
import response_factory

class MetricsServer(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path != '/metircs':
            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(bytes("NOT FOUND", "utf-8"))
            return
        res = response_factory.build()
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(bytes(res.build(), "utf-8"))

def start(hostName, serverPort, server):
    webServer = HTTPServer((hostName, serverPort), server)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")