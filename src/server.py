from http.server import BaseHTTPRequestHandler, HTTPServer
import response_factory
import metircs_controller
import http_response

_res = response_factory.ResponseFactory()

class MetricsServer(BaseHTTPRequestHandler):
    def do_GET(self):
        controller = metircs_controller.MetricsController(_res)
        controller.route(http_response.HttpResponse(self), self.path)

def start(hostName, serverPort, server):
    webServer = HTTPServer((hostName, serverPort), server)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")