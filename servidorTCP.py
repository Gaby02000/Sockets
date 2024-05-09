import socket
import random


def suma(connection):
    data = connection.recv(4096)
    args = data.decode().split(' ')
    msg=''
    for i in args:
        try:
            int(i)
        except ValueError:
            msg += f'{i} no es un entero. '
    if msg != '':
        connection.send(msg.encode())
        return False

    resultado = int(args[0]) + int(args[1])
    connection.sendall(str(resultado).encode())

def echo(connection):
    data = connection.recv(4096)
    connection.sendall(data)

def characterGenerator(connection):
    random_char = random.choice("abcdefghijklmnopqrstuvwxyz")
    connection.sendall(random_char.encode())


def service():
    print('====== Starting service in 0.0.0.0:12345 ======')
    server_address = (('0.0.0.0', 12345))
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(server_address)
    server.listen()
    while True:
        connection, client_address = server.accept()
        try:
            while True:
                characterGenerator(connection)
        except:
            print('received data is not printable')
            connection.close()
        print('====== Service down ======')


def main():
    service()

if __name__ == '__main__':
    main()