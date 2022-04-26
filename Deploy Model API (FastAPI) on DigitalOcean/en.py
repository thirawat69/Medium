import socket
import random

serverip = "104.248.39.146"
port = 27617

server = socket.socket()
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.connect((serverip, port))
