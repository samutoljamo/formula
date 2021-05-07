import socket, time
PORT = 384
s = socket.socket()

s.connect(("localhost", PORT))
for i in range(255):
    s.send(i.to_bytes(byteorder="big", length=1))

s.close()