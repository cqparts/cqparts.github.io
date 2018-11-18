#!/usr/bin/env python
import SimpleHTTPServer
import SocketServer

PORT = 8000

Handler = SimpleHTTPServer.SimpleHTTPRequestHandler

httpd = SocketServer.TCPServer(("", PORT), Handler)

print "serving at port", PORT
try:
    httpd.serve_forever()
except KeyboardInterrupt:
    print("[Ctrl+C] server stopped")
