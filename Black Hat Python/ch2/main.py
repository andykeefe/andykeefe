# This is the UDP client script shown on page 11
# To see if this works, go to terminal and use netcat
# nc -ulp <target_port> will show the message

import socket
target_host = '127.0.0.1'
target_port = 9997

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client.sendto(b'Go fuck yourself loser', (target_host, target_port))

data, addr = client.recvfrom(4096)

print(data.decode('utf-8'))
print(addr.decode('utf-8'))

client.close()  # It worked! Let's move on to the next task
