import socket
import threading

class Servidor:
    def __init__(self, host="localhost", porta=12345):
        self.host = host
        self.porta = porta
        self.clientes = []
        self.servidor_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def iniciar(self):
        self.servidor_socket.bind((self.host, self.porta))
        self.servidor_socket.listen()
        print(f"🔌 Servidor ouvindo em {self.host}:{self.porta}")

        while True:
            cliente_socket, endereco = self.servidor_socket.accept()
            print(f"🧍 Cliente conectado: {endereco}")
            self.clientes.append(cliente_socket)

            thread = threading.Thread(target=self.organizar_cliente, args=(cliente_socket, endereco))
            thread.start()

    def organizar_cliente(self, cliente_socket, endereco):
        while True:
            try:
                mensagem = cliente_socket.recv(1024)
                if not mensagem:
                    break

                print(f"💬 Mensagem de {endereco}: {mensagem.decode()}")
                self.broadcast(mensagem, cliente_socket)
            except:
                break

        print(f"🚪 Cliente {endereco} saiu.")
        self.clientes.remove(cliente_socket)
        cliente_socket.close()


    def broadcast(self, mensagem, remetente):
        for cliente in self.clientes:
            if cliente != remetente:
                try:
                    cliente.sedall(mensagem)
                except:
                    self.clientes.remove(cliente)
                    cliente.close()


if __name__ == "__main__":
    servidor = Servidor()
    servidor.iniciar()