import socket
import picamera
import sys

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '192.168.1.29'
port = 6666
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((host,port))
print('Bound to ', host, port)

while True:
    #establish connection
    server.listen(5)
    client, addr = server.accept()
    print('Connection from ', addr)
    
    #begin stream
    run = True
    while run:
        #take picture and store as jpeg
        with picamera.PiCamera() as cam:
            cam.capture('image.jpeg', resize = (1280,720), quality = 10)
        
        #encode jpeg into bytes
        with open('image.jpeg', 'rb') as image:
            read_image = image.read()
            
        length = len(read_image)
        size = str(length)
        print(size)
        
        client.sendall(size.encode('utf-8'))
        msg = client.recv(1024)
        client.sendall(read_image)
        
        word = msg.decode('utf-8')
        if word == 'End':
            run = False
    
    #stream has ended, close the connection
    client.close()
    