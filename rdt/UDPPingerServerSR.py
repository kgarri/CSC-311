import random
from socket import *
import time as time

serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.settimeout(2.0)
serverSocket.bind(('', 12000))
seq_num = 0
window = [] 
n = 2
start_index = 0
while True:

    packet = seq_num
    try:
        message,address = serverSocket.recvfrom(1024)  
        message = message.decode('utf-8').split(',')
        cur_seq = int(message[0])
        if len(window)<n:
            window.append(cur_seq)
        else:
            if window[n-1] == cur_seq:
                for seq in range(start_index,n):
                    message = str(window[seq]) + ', ACK'
                    serverSocket.sendto(message.encode(),address)
                    n+=1
                    start_index +=1
            else:
                found = False
                for seq in window:
                    if seq == message[0]:
                        found = True
                        break
                if found == False:
                    window.append(cur_seq)
                message = str(cur_seq) + ', ACK'
                serverSocket.sendto(message.encode(),address)

    except timeout:
        print("Request Timeout")
