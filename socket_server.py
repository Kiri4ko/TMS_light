import socket

sock = socket.socket()
sock.bind(("127.0.0.1", 10001))
sock.listen(1)
print("Start listening...")

connect, addr = sock.accept()
print("Connected from:", addr)

while True:
    data = connect.recv(1024).decode("utf-8")  # bytes
    print("Get data:", data)
    connect.send(b"Received data ")
    if not data:
        break
    connect.send(b"200")

sock.close()
exit()
