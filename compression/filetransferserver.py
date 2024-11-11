import socket
import time 
HOST = '192.168.200.250'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)
filename = input("Please enter filename: ")
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print(f"Listening on {HOST}:{PORT}")

    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        start = time.time()
        with open(filename , 'rb') as f:
            while True:
                data = f.read(1024)
                if not data:
                    break
                conn.sendall(data)
        end = time.time()
        print(f"time it took to send {filename} : {end - start}")
