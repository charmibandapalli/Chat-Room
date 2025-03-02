import socket

s = socket.socket()
s.bind(("localhost", 12345))
s.listen(1)
conn, addr = s.accept()

while True:
    msg = input("You: ")
    conn.send(msg.encode())
    print("Friend:", conn.recv(1024).decode())

