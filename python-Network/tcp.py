import socket

Host = "127.0.0.1"
port = 9999

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((Host, port))
client.send(b"HI")
response = client.recv(1024)
