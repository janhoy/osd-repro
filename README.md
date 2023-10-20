# Reproduction of OSD bug #2419

https://github.com/openseadragon/openseadragon/issues/2419

This repo stands up a simple python server image that emulates a level-0 iiif server that has pre-generated images
of different resolutions. The server will serve an `info.json` and respond with each image when requested.
The server will also show a web page with an instance of OSD that is pre-configured to hit the iiif server.

## Instructions

1. Build and run the docker image:

       docker build . -t osd-2419:latest
       docker run -p 3000:3000 osd-2419:latest

2. Open a browser to http://localhost:3000/

   An image shows up.
   See the log from the container to see the requests that are being made to iiif.

3. Click on the image to zoom in

   The info.json defines 10 image levels, while OSD only ever requests the first few
 
4. Debug OSD application to see why it won't request the higher levels
