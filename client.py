import socket
import threading

class Cliente:
    def __init__(self, host="localhost", porta=12345):
        self.host = host
        self.porta = porta
        self.nome = input("Digite seu nome + sobrenome: ").strip().title()
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


    def conectar(self):
        try:
            self.socket.connect((self.host, self.porta))
            print(f"✅ Conectado ao servidor!")
        except:
            print("❌ Não foi possível conectar ao servidor.")
            return
        
        # Receber mensagens dos outros
        thread_receber = threading.Thread(target=self.receber_mensagens)
        thread_receber.start()

        # Enviar mensagens ao servidor
        self.enviar_mensagens()


    def enviar_mensagens(self):
        while True:
            mensagem = input()
            if mensagem.lower().strip() == "quit":
                self.socket.close()
                print("🚪 Desconectado.")
                break
            mensagem_formatada = f"{self.nome}: {mensagem}"
            self.socket.sendall(mensagem_formatada.encode())

    def receber_mensagens(self):
        while True:
            try:
                mensagem = self.socket.recv(1024).decode()
                if not mensagem:
                    break
                print(mensagem)
            except:
                break


if __name__ == "__main__":
    cliente = Cliente()
    cliente.conectar()