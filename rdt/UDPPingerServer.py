import random
from socket import *
import time as time
import threading  as thread
serverSocket = socket(AF_INET, SOCK_DGRAM)

serverSocket.bind(('192.168.100.250', 12000))
ack_num = 0 

while True:
    
    packet = seq_num
    serverSocket.send(packet)
    
    message.split(',') , address = serverSocket.recvfrom(1024)

    
    if ack_num =  mesage[0]
        ack_num +=1
        message = ack_num + ', ACK'
        serverSocket.sendto(message, address)
