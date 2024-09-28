import time
from socket import *
clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.settimeout(2.0)
message = 'ping'
addr = ("localhost", 12000)
seq_num = 0
while true:
    packet = seq_num
    message = str(seq_num) + ", "+ message
    clientSocket.sendto(message.encode(), addr)
    try:
        recievedMessage.split(',') , server = clientSocket.recvfrom(1024)
        if recivedMessage[0] = packet + 1 
            seq_num +=1 
    except timeout:
        print(f'#{i}')
        print('Request timed out')
