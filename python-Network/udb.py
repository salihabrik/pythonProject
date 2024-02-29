import socket

Host = "127.0.0.1"
port = 9999

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client.sendto("ASDASO",(Host, port))

data, data2 = client.recvfrom(4096)
print(data)
print(data2)
