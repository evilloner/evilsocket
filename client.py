import socket
import sys
import subprocess

sock = socket.socket()
sock.connect(('localhost', 9090 ))

data_split = []

while True:
    data = sock.recv(1024)

    data_split = data.decode("utf-8").split()

    if data_split[0] == "client":
        if len(data_split) >= 2 and data_split[1] == "stop":
            sys.exit()
        else:
            pass
    else:
        pass

    data_split = []
