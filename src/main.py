import server

hostName = "0.0.0.0"
serverPort = 8080

server.start(hostName, serverPort, server.MetricsServer)