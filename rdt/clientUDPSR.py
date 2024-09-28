import time
from socket import *
clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.settimeout(1.0)
addr = ("localhost", 12000)
seq_num = 0
while True:
    message = 'ping'
    packet = seq_num
    message = str(seq_num) + ", "+ message
    print(message)
    clientSocket.sendto(message.encode(), addr)
    try:
        recievedMessage, server = clientSocket.recvfrom(1024)
        ack = int(recievedMessage.decode('utf-8').split(',')[0])
        if ack == packet + 1:
            seq_num +=1
            print(recievedMessage.decode('utf-8'))
    except timeout:
        print('Request timed out')
