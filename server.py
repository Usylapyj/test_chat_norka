import socket
 
sock = socket.socket()
sock.bind(("", 8303))
while True:
    sock.listen(1)
    conn, addr = sock.accept()
    data = conn.recv(128)
    print("[" + addr[0] + "] " + bytes.decode(data))
