import socket
from time import sleep
import random
import datetime

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

host, port = '192.168.0.13', 65000
server_address = (host, port)

colaboradores = [115, 29, 33, 14, 96, 11, 20, 30, 16, 100]

# Send a few messages
while True:
    data = str(datetime.datetime.now()).split('.')[0]

    id = str(random.choice(colaboradores))

    if id == '115':
        nome = 'Saulo'
    if id == '29':
        nome = 'Teste1'
    if id =='33':
        nome = 'Teste2'
    if id == '14':
        nome = 'Teste3'
    if id == '96':
        nome = 'Teste4'
    if id == '11':
        nome = 'Teste5'
    if id == '20':
        nome = 'Teste6'
    if id =='30':
        nome = 'Teste7'
    if id == '16':
        nome = 'Teste8'
    if id == '100':
        nome = 'Teste9'

    message = str('{},{},{}'.format(id, nome, data))
    print(message)
    sock.sendto(message.encode(),  server_address)

    sleep(5)