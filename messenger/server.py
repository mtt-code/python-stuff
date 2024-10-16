import socket
import threading

HOST = '127.0.0.1'
PORT = 1234
LISTENER_LIMIT = 5

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        server.bind((HOST, PORT))
    except:
        print('Unable to bind HOST and PORT')

    server.listen(LISTENER_LIMIT)
    while 1:
        client, address = server.accept()
        print(f'Successfully connected to client {address[0]} {address[1]}')

if __name__ == '__main__':
    main()