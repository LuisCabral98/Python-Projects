# Socket Programming
# method of communication between two nodes or sockets

import socket
import sys

# first parameter refers to address IPv4 and second parameter is connection oriented TCP 
# to get ip for website, type ping and then your website or use socket.gethostbyname('website')
# ip = socket.gethostbyname('(website)')
# print(ip)

try: 
	# create socket
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	print('socket created')
except socket.error as err: 
	print(f'socket failed with {err}')
 
port = 80
website = input(f'please input a website you would like the ip from ')

#modify with website you want ip from 
try: 
	host_ip = socket.gethostbyname(f'{website}')
#this error means there is a DNS error
except socket.gaierror:
	print('error resolving host')
	sys.exit()

#connecting to server
s.connect((host_ip, port))
#connection successful 
print(f'Socket connected to website on port {host_ip}')

 