import time
from socket import *
clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.settimeout(1.0)
addr = ("localhost", 12000)
seq_num = 0
window = [0,1]
n = 2
start_index = 0
copy = seq_num
while True:
    message = 'ping'
    for seq in range(start_index, n + 1):
        message = str(window[seq]) + ", "+ message
        print(message)
        clientSocket.sendto(message.encode(), addr)
        try:
            recievedMessage, server = clientSocket.recvfrom(1024)
            ack = int(recievedMessage.decode('utf-8').split(',')[0])
            if ack == window[n - 1]:
                    seq_num+=1
                    start_index+=1
                    n+= 1
                    window.append(seq_num)
                    print(recievedMessage.decode('utf-8'))

        except timeout:
            print('Request timed out')
