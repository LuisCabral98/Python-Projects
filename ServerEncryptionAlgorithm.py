#open socket for connections
#receive msg from client, apply sha512, send msg back

import socket 
import hashlib
import sys

HOST = '127.0.0.1'
PORT = 60001

try: 
    #create socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    #bind
    s.bind((HOST, PORT))

except socket.error as E: 
    print(f"Binding failed")
    sys.exit()
    
#begin listening
s.listen()
print(f"Listening...")

#accept connection from address
conn, addr = s.accept()

#perform actions with connection
with conn: 
    
    #print connected address
    print(f"Connected by: {addr}")
    while True: 
        data = conn.recv(4096)
        print(f"Message Received")
        data.decode()

        if not data:
            break
        
        #encrypt
        encrypt_data = hashlib.sha512(b"{data}").hexdigest()

        #send encrypted message back
        conn.sendall(b"data")

