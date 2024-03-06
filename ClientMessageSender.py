#send encrypted message to server and receive decrypted message
import socket
import hashlib
import sys

HOST = '127.0.0.1'
PORT = 60001
print(f"Attempting to connnect...")

try: 
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

    s.connect((HOST, PORT))
    
except socket.error as E: 
    print(f"Connection to server unsuccessful") 
    sys.exit()

print(f"Connection Successful! Please enter message to encrypt: ")
#receive message from user
user_inp = input()
#encode message
encoded_inp = user_inp.encode()
#send encoded message
s.sendall(encoded_inp)
#receive encrypted message from server
encrypted_inp = s.recv(4096)
#decode what was received from server
encrypted_inp = hashlib.sha512(b"encrypted_inp").hexdigest()
#print decoded encrypted message
print(f"Here is your encrypted message: {encrypted_inp}")
s.close()

