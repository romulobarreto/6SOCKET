import socket
import threading

HOST = 'localhost'
PORT = 55555

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

salas = {}

def broadcast(sala, mensagem):
    for i in salas[sala]:
        if isinstance(mensagem, str):
            mensagem = mensagem.encode()
        i.send(mensagem)

def enviar_mensagem(nome, sala, client):
    while True:
        mensagem = client.recv(1024)
        mensagem = f"{nome}: {mensagem.decode()}\n"
        broadcast(sala, mensagem)

while True:
    client, address = server.accept()
    client.send(b'SALA')
    sala = client.recv(1024).decode()
    nome = client.recv(1024).decode()
    if sala not in salas.keys():
        salas[sala] = []
    salas[sala].append(client)
    print(f'✅ O cliente {nome.title()} conectou-se na sala {sala.title()}! INFO: {address}')
    broadcast(sala, f'{nome}: Entrou na sala!')
    thread = threading.Thread(target=enviar_mensagem, args=(nome, sala, client))
    thread.start()