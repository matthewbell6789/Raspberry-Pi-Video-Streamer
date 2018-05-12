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

## Writing midterm_server.py and midterm_client.py

As I learned how to utilize all the libraries I used for these programs, I began writing the server.py and client.py files. 

I first started by combining the functions and methods used from the picamera, base64 and gzip libraries. I wrote a test.py file in which I captured took a photo and then encoded the photo, compressed the encoded data, and then reversed the process by decompressing and then decoding the photo. This allowed me to test all three of the libraries and test what size and encoding quality I wanted for the image.jpeg.

Now that I had the encoder and compression working, I spilt the test.py code up into the server.py and client.py files. I then began implementing the socket protocol. By using the example I had found online [3] I was easily able to set up the socket and transmit data from the Raspberry Pi to my laptop. Once I began to send images, I realized that the file size of the image.jpeg would have to be severely reduced. I lowered the resolution and decreased the quality of the .jpeg encoder until I was able to send the encoded and compressed image between devices using socket.

Lastly I worked on trying to display the image I had received from the Raspberry Pi. I tried several different methods but finally settled on using the Pillow library for the Midterm. The Pillow library allows me to display the image sent from the Raspberry Pi, but I can not update the displayed image. Instead I have to open another window with the next image being sent. For the final project I will be finding a different way to display the images.

## Writing stream_server.py and stream_client.py

Starting from where I left off last semester, my first and foremost task was to increase the size of the image file I could send between the server and the client.

## Libraries

socket - https://docs.python.org/3.6/library/socket.html#module-socket

gzip - https://docs.python.org/3.6/library/gzip.html#module-gzip

base64 - https://docs.python.org/3.6/library/base64.html

sys - https://docs.python.org/3.6/library/sys.html

picamera - https://picamera.readthedocs.io/en/release-1.13/index.html

Pillow - https://pillow.readthedocs.io/en/latest/index.html

## Refrences

[3] https://raspberrypi.stackexchange.com/questions/13425/server-and-client-between-pc-and-raspberry-pi
