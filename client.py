import socket
import threading
from tkinter import *
import tkinter
from tkinter import simpledialog


class Chat:
    def __init__(self):
        HOST = 'localhost'
        PORT = 55555
        #self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #self.client.connect((HOST, PORT))

        login = Tk()
        login.withdraw()

        self.janela_carregada = False
        self.ativo = True

        #self.nome = simpledialog.askstring('Nome', 'Digite seu nome!', parent=login)
        #self.sala = simpledialog.askstring('Sala', 'Digite a sala que deseja entrar!', parent=login)
        self.janela()

    def janela(self):
        self.root = Tk()
        self.root.geometry("700x540")
        self.root.title("Chat")

        self.caixa_texto = Text(self.root)
        self.caixa_texto.place(relx=0.05, rely=0.01, width=650, height=400)

        #self.envia_mensagem = Entry(self.root)
        #self.envia_mensagem.place(relx=0.05, rely=0.8, width=460, height=30)

        #self.btn_enviar = Button(self.root, text='Enviar', command=self.enviar_mensagem)

        self.root.mainloop()

    def enviar_mensagem(self):
        pass


chat = Chat()