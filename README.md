# Raspberry Pi Video Streamer

The goal of this project was to use a Raspberry Pi and Raspberry Pi V2 Camera Module to stream video to a computer over Wifi using Python.

## What uses are there for a wireless video streaming device?

There are a lot of potential uses for a wireless video streaming device, namely:
* Security Systems
* Surveillance Systems
* Motion Sensors
* Point of View Cameras for RC Cars or Drones

All of these options would be a great use for a small wireless video streaming device.

## How does this device work?

This video streaming device works by:
* Taking a photo using the Raspberry Pi Camera Module.
* Encoding that photo into a file of bytes using the base64 library.
* Compressing the byte file using the gzip library.
* Sending the compressed bytes from a server to a client using socket.
* Uncompressing the byte file.
* Decoding the uncompresses bytes into an image.
* Displaying the image, representing one frame of a video stream.

## Video Demo

https://www.youtube.com/watch?v=qsVpvSTfRnY

## Libraries

socket - https://docs.python.org/3.6/library/socket.html#module-socket

gzip - https://docs.python.org/3.6/library/gzip.html#module-gzip

base64 - https://docs.python.org/3.6/library/base64.html

sys - https://docs.python.org/3.6/library/sys.html

picamera - https://picamera.readthedocs.io/en/release-1.13/index.html

Pillow - https://pillow.readthedocs.io/en/latest/index.html

