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
* Sending the compressed bytes from a server to a client using socket.
* Decoding the bytes into an image.
* Displaying the image, representing one frame of a video stream.

## Video Demos

### Midterm Demo

https://www.youtube.com/watch?v=qsVpvSTfRnY

### Final Demo

https://youtu.be/W8hBRJdEFV8

## Libraries

socket - https://docs.python.org/3.6/library/socket.html#module-socket

gzip - https://docs.python.org/3.6/library/gzip.html#module-gzip

base64 - https://docs.python.org/3.6/library/base64.html

sys - https://docs.python.org/3.6/library/sys.html

picamera - https://picamera.readthedocs.io/en/release-1.13/index.html

Pillow - https://pillow.readthedocs.io/en/latest/index.html

## Refrences

[3] https://raspberrypi.stackexchange.com/questions/13425/server-and-client-between-pc-and-raspberry-pi
