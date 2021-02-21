# hello-docker
#
# Version: 0.2.2 (2021-01-16)
# License: GNU General Public License v2.0
# Author: Stefan Junger

import http.server
import socketserver

class Handler(http.server.SimpleHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><head><title>Testserver</title></head>", "utf-8"))
        self.wfile.write(bytes("<body>", "utf-8"))
        self.wfile.write(bytes("<center>", "utf-8"))
        self.wfile.write(bytes("<font face=\"arial,helvetica\">", "utf-8"))
        self.wfile.write(bytes("<p>&nbsp;</p>", "utf-8"))
        self.wfile.write(bytes("<p>&nbsp;</p>", "utf-8"))
        self.wfile.write(bytes("<p>&nbsp;</p>", "utf-8"))
        self.wfile.write(bytes("<h1>Hello, Docker!</h1>", "utf-8"))
        self.wfile.write(bytes("<p>Request: %s</p>" % self.path, "utf-8"))
        self.wfile.write(bytes("<p>This is an example web server written in Python3.</p>", "utf-8"))
        self.wfile.write(bytes("</font>", "utf-8"))
        self.wfile.write(bytes("</center>", "utf-8"))
        self.wfile.write(bytes("</body></html>", "utf-8"))
        return

print('Server listening on port 8100...')
httpd = socketserver.TCPServer(('', 8100), Handler)
httpd.serve_forever()
