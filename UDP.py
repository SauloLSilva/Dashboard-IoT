import socket
from Models.sqlitedb import Sqlitedb

sqlite = Sqlitedb()

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the port
host, port = '0.0.0.0', 65000
server_address = (host, port)

# print(f'Starting UDP server on {host} port {port}')
sock.bind(server_address)

while True:
    try:
        # Wait for message
        message, address = sock.recvfrom(4096)
        if message != '':
            dados = message.decode('utf-8').split(',')
            id = dados[0]
            nome = dados[1]
            data = dados[2]
            sqlite.check_acesso(id, nome, data)
    except:
        pass