import service_factory
import controller
import http_response
import config
from http.server import BaseHTTPRequestHandler, HTTPServer

_service_factory = service_factory.ServiceFactory()

class Server(BaseHTTPRequestHandler):
    def do_GET(self): # Listen for all GET request
        control = controller.Controller(_service_factory, config.Config) # Makes a new controller
        control.route(http_response.HttpResponse(self), self.path) # Routes the request with a response object

def start(hostName, serverPort, server): # Starts the server
    webServer = HTTPServer((hostName, serverPort), server)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")