import socket

HOST = '1192.168.200.250'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    with open('received_file.txt', 'wb') as f:
        while True:
            data = s.recv(1024)
            if not data:
                break
            f.write(data)

print('File received successfully.')
