import socket
import base64
import picamera
import gzip
import sys

s = socket.socket()
host = '192.168.1.24'
port = 12345
s.bind((host, port))

# establish connection
s.listen(5)
c, addr = s.accept()
print('Connection from ', addr)
c.send('Thank you for connecting'.encode())
print(c.recv(1024))

while True:
    # take picture and store as jpeg
    with picamera.PiCamera() as cam:
        cam.capture('image.jpeg', resize=(160, 90), quality=9)

    # encode jpeg image into bytes
    with open('image.jpeg', 'rb') as image:
        read_image = image.read()
    encoded_image = base64.encodebytes(read_image)

    # compress image
    compressed_image = gzip.compress(encoded_image)
    with gzip.open('/home/pi/Documents/ECE_387/image.jpeg.gz', 'wb') as zip:
        zip.write(compressed_image)

    c.send(compressed_image)
    # print(sys.getsizeof(encoded_image))
    print(sys.getsizeof(compressed_image))
    c.recv(1024)

c.close()