# Reproduction of OSD bug #2419

https://github.com/openseadragon/openseadragon/issues/2419

This repo stands up a simple python server that emulates an IIIF server on level 0.
The server will show a web page with an instance of OSD that is pre-configured to hit the localhost iiif server.
When OSD reads the `info.json` from the server, it will see a level-0 spec with 10 fixed `sizes`:

    82, 164, 250, 327, 500, 654, 1308, 1900, 2617, 5233

As OSD requests each image resolution the server will print to stdout and serve an image of that size
from some publically available image server.

## Instructions

1. Check out this repository or download the zip file and unzip it

2. Start the demo

       python3 iiif_server.py

   Alternatively, if you don't have python installed, start a docker image:

       docker run --rm -t -p 3000:3000 cominvent/osd-repro

3. Open a browser to http://localhost:3000/

   OpenSeaDragon shows up with the demo image.
   See the log from the container to see the requests that are being made to iiif.

4. Click on the image to zoom in

   The info.json defines 10 image levels, while OSD only ever requests the first 8 levels:

       IIIF server is running on port 3000. Visit http://localhost:3000/
       127.0.0.1 - - [20/Oct/2023 13:46:04] "GET / HTTP/1.1" 200 -
       127.0.0.1 - - [20/Oct/2023 13:46:04] "GET /styles.css HTTP/1.1" 200 -
       127.0.0.1 - - [20/Oct/2023 13:46:04] "GET /iiif/2/demo/info.json HTTP/1.1" 200 -
       Got request for info.json
       Got request for image size 500
       127.0.0.1 - - [20/Oct/2023 13:46:04] "GET /iiif/2/demo/full/500,/0/default.jpg HTTP/1.1" 200 -
       Got request for image size 164
       127.0.0.1 - - [20/Oct/2023 13:46:05] "GET /iiif/2/demo/full/164,/0/default.jpg HTTP/1.1" 200 -
       127.0.0.1 - - [20/Oct/2023 13:46:05] "GET /favicon.ico HTTP/1.1" 404 -
       Got request for image size 654
       127.0.0.1 - - [20/Oct/2023 13:46:18] "GET /iiif/2/demo/full/654,/0/default.jpg HTTP/1.1" 200 -
       Got request for image size 1308
       127.0.0.1 - - [20/Oct/2023 13:46:21] "GET /iiif/2/demo/full/1308,/0/default.jpg HTTP/1.1" 200 -
       Got request for image size 1900
       127.0.0.1 - - [20/Oct/2023 13:46:25] "GET /iiif/2/demo/full/1900,/0/default.jpg HTTP/1.1" 200 -
       Got request for image size 1900
       127.0.0.1 - - [20/Oct/2023 13:46:26] "GET /iiif/2/demo/full/1900,/0/default.jpg HTTP/1.1" 200 -
     
5. Debug OSD application

   **Find out why OSD won't request level 9 (witdth 2617) and 10 (width 5233).**
