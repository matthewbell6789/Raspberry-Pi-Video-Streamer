import socket
import sys
import pygame
from pygame.locals import *

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '192.168.1.29' # ip of raspberry pi
port = 6666
client.connect((host, port))

pygame.init()

resolution = (1280, 720)

gameDisplay = pygame.display.set_mode(resolution)
pygame.display.set_caption('Python Video Streamer')

run = True
msg = 'Received'
while run:

    if pygame.event.peek(KEYDOWN):
        run = False
        msg = 'End'

    data = client.recv(1024)
    client.sendall(msg.encode())
    size_str = data.decode('utf-8')
    size = int(size_str)
    print("Data: ", size_str)
    img_size = 0
    image = b''

    while img_size <= size:
        image = image + client.recv(102400)
        img_size = sys.getsizeof(image)

    print("Image size: ", img_size)

    with open('image.jpg', 'wb') as i:
        i.write(image)

    picture = pygame.image.load('image.jpg')

    if pygame.event.peek(): #works
        gameDisplay.blit(picture, (0, 0)) # does nto work by self?

    pygame.display.flip()

client.close()