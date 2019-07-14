import socket
import threading

sock = socket.socket()
sock.bind(('', 9090))
sock.listen(10000000)

clients = []

def clients_job():
    while True:
        conn, addr = sock.accept()
        if conn not in clients:
            clients.append(conn)
        else:
            pass

t = threading.Thread(target=clients_job)
t.start()

while True:
    data = input("Commands-> ")
    for client in clients:
        client.sendall(data.encode("utf-8"))
