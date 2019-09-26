import socket
from time import sleep

UDP_IP = "127.0.0.1"
UDP_PORT = 5001
UDP_PORT_DWN = 5006
sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP

sock.bind((UDP_IP, UDP_PORT))
sock.settimeout(0.001)

dataRate = 9600

debug=1

def dprint(data):
    if debug==1:
        print(data)
        
    return

f = open("input.png","rb")
message = f.read()
f.close()
packet = []
count = 0
for byte in message:
    packet.append(byte)
    if len(packet) > 255:
        dprint("sending packet #"+str(count))
        sock.sendto(bytes(packet), (UDP_IP, UDP_PORT_DWN))
        sleep(len(packet)*8/dataRate)
        count+=1
        packet = []
    
while len(packet) < 256:
    packet.append(0)
    
print("done")

sock.sendto(bytes(packet), (UDP_IP, UDP_PORT))
