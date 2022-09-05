import socket

sock = socket.socket()
sock.connect(("127.0.0.1", 10001))

while True:
    message = input('Print message: ')
    sock.send(message.encode("utf-8"))
    data = sock.recv(1024).decode("utf-8")
    print(f"Response: {data}")
    if message == "exit":
        break
