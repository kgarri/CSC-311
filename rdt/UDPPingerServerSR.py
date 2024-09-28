import random
from socket import *
import time as time

serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.settimeout(2.0)
serverSocket.bind(('', 12000))
seq_num = 0
window = [0]

while True:
    
    packet = seq_num
    print(seq_num)
    try:
        message,address = serverSocket.recvfrom(1024)  
        message = message.decode('utf-8').split(',')
        print(message)
        if window[-1] == int(message[0]):
            seq_num = int(message[0])
            for seq in window:
                message = str(seq) + ', ACK'
                serverSocket.sendto(message.encode(),address)
            window.append(int(message[0])+1)
        else:
                message = str(seq_num) + ', ACK'
                serverSocket.sendto(message.encode(),address)

    except timeout:
        print("Request Timeout")
