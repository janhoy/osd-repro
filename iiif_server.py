#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Reproduction iiif server
import re
import http.server
from http.server import BaseHTTPRequestHandler
from urllib.request import urlopen

class IIIFRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            # Serve the index.html file for the root path
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            with open("index.html", "rb") as file:
                self.wfile.write(file.read())
        elif self.path == "/styles.css":
            # Serve the styles file
            self.send_response(200)
            self.send_header("Content-type", "text/css")
            self.end_headers()
            with open("styles.css", "rb") as file:
                self.wfile.write(file.read())
        elif self.path == "/iiif/2/demo/info.json":
            # Serve the info.json file
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            print(f"Got request for info.json")
            with open("info.json", "rb") as file:
                self.wfile.write(file.read())
        elif re.match(r"/iiif/2/demo/full/\d+,/0/default.jpg", self.path):
            # Extract requested size from URL and print to stdout
            size = re.search(r"/iiif/2/demo/full/(\d+),/0/default.jpg", self.path).group(1)
            print(f"Got request for image size {size}")
            # Stream the content from the provided URL
            url = f"https://iiif.princeton.edu/loris/pudl0001%2F4609321%2Fs42%2F00000001.jp2/full/{size},/0/default.jpg"
            with urlopen(url) as response:
                self.send_response(200)
                self.send_header("Content-type", response.getheader("Content-type"))
                self.end_headers()
                self.wfile.write(response.read())
        else:
            # If the request doesn't match any of the above patterns, return a 404 response
            self.send_response(404)
            self.end_headers()

if __name__ == "__main__":
    PORT = 3000
    # Change the directory to the location of your files (index.html, info.json)
    server = http.server.HTTPServer(('0.0.0.0', PORT), IIIFRequestHandler)
    print(f"IIIF server is running on port {PORT}. Visit http://localhost:3000/")
    server.serve_forever()
