import socket
import random
from time import sleep

f = open("output.png","wb+")
UDP_IP = "127.0.0.1"
UDP_PORT = 5000
size = 257
invber = 10**3

gnd = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
gnd.bind((UDP_IP, UDP_PORT))
gnd.settimeout(0.001)

count=0
data=""

while True:
    
    try:
        data, addr = gnd.recvfrom(size) # buffer size is 1024 bytes
        count=0
        
        
    except:
        data=""
    
    if len(data)>1:
        dataOut=[]
        for byte in data:
            if byte == 0:
                count = count+1
            if count > 200:
                f.close()
                print("done")
                break
        f.write(bytes(data))
        

