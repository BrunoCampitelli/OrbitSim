import socket
import random
from time import sleep

#socket setup
UDP_IP = "127.0.0.1"
UDP_PORT_UP = 5005
UDP_PORT_DWN = 5006
UDP_PORT_SAT = 5001
UDP_PORT_GND = 5000


invber = 10**6 #use inverse of BER

size = 257 #channel param

#setup sockets
UpLnk = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
UpLnk.bind((UDP_IP, UDP_PORT_UP))
UpLnk.settimeout(0.001)

DwnLnk = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
DwnLnk.bind((UDP_IP, UDP_PORT_DWN))
DwnLnk.settimeout(0.001)
count=0
data=""
debug=0


def berData(data):
    dataOut=[]
    for byte in data:
        for bitCount in range(0,7):
            if (random.randrange(1,invber) == 1):
                byte=byte^(1<<bitCount)
        dataOut.append(byte)
    
    return bytes(dataOut)

def dprint(data):
    if debug==1:
        print(data)
        
    return

print("channels are ready")
while True:
    
    #check data for uplink
    try:
        dataUp, addrUp = UpLnk.recvfrom(size) # buffer size is 1024 bytes
        
    except:
        dataUp=""
    
    #simulate ber and send data to satellite
    if len(dataUp)>1 :
        dprint("received data from ground")
        UpLnk.sendto(berData(dataUp),(UDP_IP,UDP_PORT_SAT))
        dprint("data sent to sat")
        
    #repeat for downlink
    try:
        dataDwn, addrDwn = DwnLnk.recvfrom(size) # buffer size is 1024 bytes
        
    except:
        dataDwn=""
    
    if len(dataDwn)>1 :
        dprint("received data from sat")
        DwnLnk.sendto(berData(dataDwn),(UDP_IP,UDP_PORT_GND))
        dprint("data sent to ground")
    
    
        
