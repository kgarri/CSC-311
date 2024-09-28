import time
from socket import *
clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.settimeout(1.0)
addr = ("localhost", 12000)
seq_num = 0
window = [seq_num]
n = 2
while True:
    message = 'ping'
    for seq in window:
        packet = seq
        message = str(seq) + ", "+ message
        print(message)
        clientSocket.sendto(message.encode(), addr)
    try:
        recievedMessage, server = clientSocket.recvfrom(1024)
        ack = int(recievedMessage.decode('utf-8').split(',')[0])
        if ack <=  window[0] + n:
            if len(window)+1<n:
                seq_num +=1
                window.append(seq_num)
            else:
                seq_num+=1
                window[0] = window[-1]
                window[-1] = seq_num
            print(recievedMessage.decode('utf-8'))

    except timeout:
        print('Request timed out')
