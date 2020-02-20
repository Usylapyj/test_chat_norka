import socket

def sendData(data):
    sock = socket.socket()
    sock.connect(("35.194.254.250", 8303))
    sock.send(str.encode(data))
    sock.close()

sendData("312")
