import threading
import socket
volume_path = 'C:\\Users\\20192ewbj0060\\Documents\\SD'

def main():
    #Definindo IPV4 e protocolo TCP
    # Cria o socket do cliente
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client_socket.connect(('localhost', 80))
    except:
        return print('\nNão foi possível se conectar ao servidor!\n')

    username = input('Informe seu nome de usuário: ')
    print('\nConectado! Digite sair a qualquer comento para encerrar conexão.\n')
        # Exibição do histórico
    
    
    with open(f'{volume_path}\\logaChat.txt', 'r') as file:
        print('Histórico de Mensagens:')
        print(file.read())

    print('Digite sua mensagem:')

    thread1 = threading.Thread(target=receiveMessages, args=[client_socket])
    thread2 = threading.Thread(target=sendMessages, args=[client_socket, username])

    thread1.start()
    thread2.start()

#recebimento de mensagens
def receiveMessages(client_socket):
    while True:
        try:
            #convertendo bytes em string
            msg = client_socket.recv(2048).decode('utf-8')
            print(msg + '\n')
        except:
            print('\nNão foi possível manter conexão com o servidor!\n')
            print('Pressione a tecla <Enter> Para continuar...')
            client_socket.close()
            break
            
#envio de mensagens
def sendMessages(client_socket, username):
    #sempre ouvindo msgns
    while True:
        try:
            msg = input('\n')
            #tranformando string em bytes
            if msg == 'sair':
                client_socket.close()
                break
            client_socket.send(f'{username}: {msg}'.encode('utf-8'))
        except:
            return


main()
