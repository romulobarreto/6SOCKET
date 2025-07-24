import socket
import threading

HOST = 'localhost'
PORT = 55554

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

salas = {}



def broadcast(sala, mensagem, remetente=None):
    for cliente in salas[sala][:]:
        if cliente['socket'] == remetente:
            continue
        try:
            if isinstance(mensagem, str):
                mensagem = mensagem.encode()
            cliente['socket'].send(mensagem)
        except:
            salas[sala].remove(cliente)
            cliente['socket'].close()




def enviar_mensagem(nome, sala, client):
    try:
        while True:
            mensagem = client.recv(1024)
            if not mensagem:
                break
            mensagem = f"{nome}: {mensagem.decode()}\n"
            broadcast(sala, mensagem, remetente=client)
    except:
        pass
    finally:
        print(f"🚪 Cliente {nome} saiu da sala {sala}.")
        salas[sala] = [c for c in salas[sala] if c['socket'] != client]
        client.close()
        broadcast(sala, f"{nome} saiu da sala.\n")




while True:
    client, address = server.accept()
    # Envia a lista de salas
    lista_salas = list(salas.keys())
    salas_str = ','.join(lista_salas) if lista_salas else '__NO_SALAS__'
    client.send(salas_str.encode())
    client.send(b'__CMD_SALA__')
    dados = client.recv(1024).decode()
    sala, nome = dados.split('|||')
    if sala not in salas.keys():
        salas[sala] = []
    salas[sala].append({'nome': nome, 'socket': client})
    print(f'✅ O cliente {nome.title()} conectou-se na sala {sala.title()}! INFO: {address}')
    broadcast(sala, f'{nome}: Entrou na sala!\n', remetente=client)
    thread = threading.Thread(target=enviar_mensagem, args=(nome, sala, client))
    thread.start()