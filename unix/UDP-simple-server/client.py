import socket
import threading
import os

UDP_MAX_SIZE = 65535
ENCODING = "utf-8"

def listen(s: socket.socket):
    while True:
        msg, addr = s.recvfrom(UDP_MAX_SIZE)
        print('\r'+msg.decode(ENCODING)+'\n'+f'you: ',end='')

def connect(host: str = '127.0.0.1',port: int = 9090):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect((host, port))

    # получаем сообщения от других пользователей в фоновом режиме
    threading.Thread(target=listen, args=(s,),daemon=True).start()


    s.sendto('__join'.encode(ENCODING),(host, port))

    while True:
        try:
            msg = input(f'you: ')
        except KeyboardInterrupt as k:
            s.sendto("__exit".encode(ENCODING), (host, port))
            s.close()
            exit()
        s.sendto(msg.encode(ENCODING), (host, port))

if __name__ == '__main__':
    os.system('cls')
    print('Welcome to chat')
    connect()