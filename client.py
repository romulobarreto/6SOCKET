import socket
import threading
from tkinter import *
from tkinter.ttk import Combobox

class Chat:
    def __init__(self):
        HOST = 'localhost'
        PORT = 55554
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((HOST, PORT))

        self.nome = ''
        self.sala = ''

        # Recebe lista de salas
        recebido = self.client.recv(1024).decode()
        lista = []
        if recebido != '__NO_SALAS__':
            lista = recebido.split(',')

        # Espera sinal do servidor
        self.client.recv(1024)  # __CMD_SALA__

        self.iniciar_gui(lista)


    def iniciar_gui(self, lista_salas):
        lista_salas.sort()
        self.root = Tk()
        self.root.geometry("540x700")
        self.root.title("Login - Escolha a sala")
        self.janela_login(lista_salas)
        self.root.mainloop()

        

    def janela_login(self, lista_salas):
        for widget in self.root.winfo_children():
            widget.destroy()

        Label(self.root, text="Digite seu nome:").pack(pady=5)
        nome_entry = Entry(self.root)
        nome_entry.pack(pady=5)

        Label(self.root, text="Escolha uma sala ou digite uma nova:").pack(pady=5)

        self.sala_var = StringVar()
        combobox = Combobox(self.root, textvariable=self.sala_var, state="readonly")
        if lista_salas:
            combobox['values'] = lista_salas
            combobox.current(0)
        combobox.pack(pady=5)

        nova_sala_entry = Entry(self.root)
        nova_sala_entry.pack(pady=5)

        def entrar():
            nome = nome_entry.get().strip().title()
            nova = nova_sala_entry.get().strip().title()
            sala_escolhida = nova if nova else self.sala_var.get()
            if nome and sala_escolhida:
                self.nome = nome
                self.sala = sala_escolhida
                # Envia sala e nome para o servidor
                mensagem = f"{sala_escolhida}|||{nome}"
                self.client.send(mensagem.encode())
                self.janela()
            else:
                print("Preencha todos os campos")

        Button(self.root, text="Entrar", command=entrar).pack(pady=10)

    def janela(self):
        # Esconde widgets antigos
        for widget in self.root.winfo_children():
            widget.destroy()

        self.root.title(f"Chat - Sala: {self.sala}")

        frame_texto = Frame(self.root)
        frame_texto.place(relx=0.037, rely=0.01, width=500, height=620)

        scrollbar = Scrollbar(frame_texto)
        scrollbar.pack(side=RIGHT, fill=Y)

        self.caixa_texto = Text(frame_texto, yscrollcommand=scrollbar.set)
        self.caixa_texto.pack(side=LEFT, fill=BOTH, expand=True)
        self.caixa_texto.tag_configure("direita", justify='right')

        scrollbar.config(command=self.caixa_texto.yview)

        self.envia_mensagem = Entry(self.root)
        self.envia_mensagem.place(relx=0.037, rely=0.92, width=420, height=40)
        self.envia_mensagem.bind('<Return>', self.enviar_mensagem)

        self.btn_enviar = Button(self.root, text='Enviar', command=self.enviar_mensagem)
        self.btn_enviar.place(relx=0.82, rely=0.92, width=75, height=40)

        self.root.protocol("WM_DELETE_WINDOW", self.fechar)

        thread = threading.Thread(target=self.conecta)
        thread.start()

    def fechar(self):
        try:
            self.client.shutdown(socket.SHUT_RDWR)
            self.client.close()
        except:
            pass
        self.root.destroy()

    def conecta(self):
        try:
            while True:
                recebido = self.client.recv(1024)
                if not recebido:
                    break
                try:
                    self.caixa_texto.insert('end', recebido.decode())
                    self.caixa_texto.see('end')
                except:
                    pass
        except:
            pass

    def enviar_mensagem(self, event=None):
        mensagem = self.envia_mensagem.get()
        try:
            self.client.send(mensagem.encode())
            self.envia_mensagem.delete(0, END)
            self.caixa_texto.insert('end', f"{mensagem}\n", "direita")
            self.caixa_texto.see('end')
        except:
            pass

if __name__ == "__main__":
    Chat()