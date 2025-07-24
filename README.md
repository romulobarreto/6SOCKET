# 💬 Projeto Chat em Rede com Sockets e Tkinter

## 📌 Visão Geral
Este é um sistema de chat em rede desenvolvido em Python, utilizando sockets para conexão entre clientes e servidor, e interface gráfica com Tkinter. O projeto tem como objetivo explorar conceitos de redes, multithreading, orientação a objetos e interface de usuário.

---

## ⚙️ Funcionalidades

- Envio e recebimento de mensagens em tempo real  
- Sistema de salas (chat rooms)  
- Interface gráfica com Tkinter  
- Alinhamento personalizado das mensagens (direita para o remetente, esquerda para os demais)  
- Scroll automático no histórico de mensagens  
- Notificação de entrada/saída de participantes (visível apenas aos outros membros da sala)  
- Lista de salas disponíveis ordenada automaticamente  

---

## 🧠 Conceitos Aplicados

- Programação orientada a objetos (POO)  
- Programação concorrente com `threading`  
- Comunicação via `socket` TCP  
- Interface com Tkinter  
- Organização de código em padrão MVC (parcial)  

---

## 🗂️ Estrutura do Projeto

```
📁 6SOCKET
├── client.py          # Cliente com interface Tkinter
├── server.py          # Servidor central com gerenciamento de salas
```

---

## 🧩 Como Funciona

### Cliente
- O cliente abre uma interface gráfica
- Escolhe um nome e uma sala existente ou cria uma nova
- Conecta ao servidor e começa a enviar/receber mensagens
- As mensagens são exibidas com alinhamento personalizado

### Servidor
- Aguarda conexões dos clientes
- Gerencia salas e lista de clientes conectados
- Reenvia mensagens recebidas para os outros clientes da mesma sala (broadcast)
- Evita duplicar mensagens para o remetente

---

## 🛠️ Tecnologias Utilizadas

- **Linguagem:** Python 3  
- **Redes:** socket (TCP)  
- **Interface:** Tkinter  
- **Concorrência:** threading  

---

## ▶️ Como Executar

1. Clone o repositório:
   ```bash
   git clone https://github.com/romulobarreto/6SOCKET.git
   ```

2. Execute o servidor:
   ```bash
   python server.py
   ```

3. Em outra janela, execute o cliente:
   ```bash
   python client.py
   ```

4. Abra quantas instâncias quiser do `client.py` para simular vários usuários 

---

## 👨‍💻 Autor

Desenvolvido por `Rômulo Barreto da Silva ❤️
