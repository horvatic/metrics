from http.server import HTTPServer
import server
import cpu

print(cpu.cpu_usage())

hostName = "0.0.0.0"
serverPort = 5500

webServer = HTTPServer((hostName, serverPort), server.MetricsServer)
print("Server started http://%s:%s" % (hostName, serverPort))

try:
    webServer.serve_forever()
except KeyboardInterrupt:
    pass

webServer.server_close()
print("Server stopped.")