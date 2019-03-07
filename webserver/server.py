#!/usr/bin/env python

import http.server
import socketserver
import logging

PORT = 8000

class GetHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        logging.error(self.headers)
        http.server.SimpleHTTPRequestHandler.do_GET(self)

socketserver.TCPServer.allow_reuse_address = True
httpd = socketserver.TCPServer(("", PORT), GetHandler)

httpd.serve_forever()
