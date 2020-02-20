import socket

ip = "localhost"    #85.140.2.221

nickname = input()

sock = socket.socket()
sock.connect((ip, 9090))
if sock.recv(1024) == b"0":
    sock.send(b"0")

while True:
    message = input("Message: ")
    sock.send(bytes(f"{nickname}: {message}", "utf8"))
    if message == "stop":
        break

sock.close()
