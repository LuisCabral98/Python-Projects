# Socket Programming
# method of communication between two nodes or sockets

import socket
import sys

# first parameter refers to address IPv4 and second parameter is connection oriented TCP 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# to get ip for website, type ping and then your website 
