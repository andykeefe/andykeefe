# This is the simplest TCP client you can code in Python
# We'll first import a socket, then define a target host
# Then we'll define the target port

import socket

target_host = '0.0.0.0'
target_port = 9998

# Create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# TCP requires connection. Connect the client.
client.connect((target_host, target_port))

# Send some data to receive a response
# This can be arbitrary bytes; for example,
# earlier I wrote the word 'FUCK' a bunch of times
# and saw it in Wireshark.
# However, the program will stutter and fail on
# trying to receive the information on port 4096

client.send(b"Oi, pretty boy")

# Receive some data
response = client.recv(4096)

print(response.decode())
client.close()
