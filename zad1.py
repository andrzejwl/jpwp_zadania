import socket
import json

HOST = "172.104.229.108"
PORT = 9001

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    """
    Tutaj uzupełnij kod.
    """

    s.close()