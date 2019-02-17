#!/usr/bin/python
# -*- coding: utf-8 -*-

from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from prometheus_client import Summary, Counter, Gauge, Info, start_http_server
from os import curdir, sep
import time

PORT_NUMBER = 8080
BIND_IP = '0.0.0.0'
EXPORTER_PORT_NUMBER = 8000
EXPORTER_BIND_IP = '0.0.0.0'

counter_failures = Counter('demo_counter_failures', 'Quantity of fault requests')
counter_summary = Summary('demo_request_counter', 'Summary of ok requests')
counter_gauge = Gauge('demo_request_gauge', 'Gauge of requests')
application_info = Info('demo_build_version', 'Application info')
# This class will handles any incoming request from
# the browser
class myHandler(BaseHTTPRequestHandler):

    # Handler for the GET requests
    def do_GET(self):
        if self.path == "/":
            self.path = "./index.html"

        if self.path == "/about":
             self.path = "./about.html"

        if self.path == "/contacts":
             self.path = "./contacts.html"

        try:
            # Check the file extension required and
            # set the right mime type

            sendReply = False
            if self.path.endswith(".html"):
                mimetype = 'text/html'
                sendReply = True
                counter_summary.observe(1)
            if self.path.endswith(".jpg"):
                mimetype = 'image/jpg'
                sendReply = True
            if self.path.endswith(".gif"):
                mimetype = 'image/gif'
                sendReply = True
            if self.path.endswith(".js"):
                mimetype = 'application/javascript'
                sendReply = True
            if self.path.endswith(".css"):
                mimetype = 'text/css'
                sendReply = True

            if sendReply == True:
                # Open the static file requested and send it
                # counter_summary.observe(2)
                counter_gauge.inc()
                counter_gauge.time()
                application_info.info({'version': '1.0.1', 'buildhost': 'macbook-pro-obsession'})
                f = open(curdir + sep + self.path)
                self.send_response(200)
                self.send_header('Content-type', mimetype)
                self.end_headers()
                self.wfile.write(f.read())
                f.close()
            return


        except IOError:
            counter_failures.inc()
            self.send_error(404, 'File Not Found: %s' % self.path)


try:
    # Create a web server and define the handler to manage the
    # incoming request
    server = HTTPServer(('', PORT_NUMBER), myHandler)
    print 'Started httpserver on %s:%s ' % (BIND_IP, PORT_NUMBER)

    start_http_server(EXPORTER_PORT_NUMBER, addr=EXPORTER_BIND_IP)
    print 'Started http prometheus exporter on %s:%s' % (EXPORTER_BIND_IP, EXPORTER_PORT_NUMBER)
    # Wait forever for incoming http requests
    server.serve_forever()



except KeyboardInterrupt:
    print '^C received, shutting down the web server'
    server.socket.close()