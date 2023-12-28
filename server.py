import threading
import socket
host = 'localhost'
port = 80

clients = []

def main():

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

    #Iniciando conexão
    try:
        server_socket.bind((host, port))
        server_socket.listen()
        print("Servidor de chat iniciado, esperando conexões...")
    except:
        return print('\nNão foi possível iniciar o servidor!\n')


    while True:
        client, addr = server_socket.accept()
        print(f"Conexão de {addr[0]}:{addr[1]} estabelecida.")
        clients.append(client)

        thread = threading.Thread(target=messagesTreatment, args=[client])
        thread.start()

def save_message(msg):
    try:
        with open('logaChat.txt', 'a') as file:  # Corrigido o nome do arquivo
            file.write(msg + '\n')
            file.flush()
            file.close()
            print(f'Mensagem salva: {msg}')
    except Exception as e:
        print(f"Erro ao salvar mensagem: {e}")

def messagesTreatment(client):
    while True:
        try:
            msg = client.recv(2048)
            broadcast(msg, client)
            print('\n' + msg.decode('utf-8'))

            save_message(msg.decode('utf-8'))
        except:
            deleteClient(client)
            break

def broadcast(msg, client):
    for clientItem in clients:
        if clientItem != client:
            try:
                clientItem.send(msg)
            except:
                deleteClient(clientItem)


def deleteClient(client):
    clients.remove(client)

main()