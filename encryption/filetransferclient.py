import socket
import des_encryption as des
HOST = '1192.168.200.250'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    with open('received_file.txt', 'wb') as f:
        while True:
            nonce = s.recv(1024)
            encrypt_data = s.recv(1024)
            tag = s.recv(1024)
            if not nonce:
                break
            if not encrypt_data:
                break
            if not tag:
                break
            data = des.decrypt(nonce, encrypt_data, tag)
            if data:
                f.write(data)

print('File received successfully.')
