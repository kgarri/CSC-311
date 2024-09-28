import random
from socket import *
import time as time

serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.settimeout(2.0)
serverSocket.bind(('', 12000))
seq_num = 0
window = [] 
r = 0
n = 2
while True:

    packet = seq_num
    print(seq_num)
    try:
        message,address = serverSocket.recvfrom(1024)  
        message = message.decode('utf-8').split(',')
        print(message)
        if len(window)<n:
            window.append(int(message[0]))
        else:
            if window[n-1] == int(message[0]):
                seq_num = int(message[0])
                window.append(int(message[0]))
            if seq_num == r:
                for seq in range(r,n + 1):
                    message = str(window[seq]) + ', ACK'
                    serverSocket.sendto(message.encode(),address)
                    r+=1
                    n+=1
            else:
                window.append(int(message[0]))
                message = str(seq_num) + ', ACK'
                serverSocket.sendto(message.encode(),address)

    except timeout:
        print("Request Timeout")
