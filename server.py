import requests
import socket

ip = requests.get('https://ip.beget.ru/').text[:-1]
port = 9090

def listen():
    data = conn.recv(1024)
    if not data:
        return
    elif data == b"stop":
        conn.close()
        exit()
        return
    return data

serv = socket.socket()
serv.bind((ip, port))

print(f'Server was started on {ip}:9090')

serv.listen(1)
conn, addr = serv.accept()
print(f"{addr} was connected")
conn.send(b"0")

while True:
    f = listen()
    print(f)

conn.close()
