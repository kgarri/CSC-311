import random
from socket import *
import time as time

serverSocket = socket(AF_INET, SOCK_DGRAM)

serverSocket.bind(('192.168.100.250', 12000))
ack_num = 0 

while True:
    
    packet = ack_num
    
    message , address = serverSocket.recvfrom(1024)

    message = message.decode('utf-8').split(',') 
    if ack_num ==  message[0]:
        ack_num +=1
        message = str(ack_num) + ', ACK'
        serverSocket.sendto(message.encode(), address)
