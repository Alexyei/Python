import socket
import threading
import os
#
# UDP_MAX_SIZE = 65535
ENCODING = "utf-8"
#
# def listen(s: socket.socket):
#     while True:
#         msg, addr = s.recvfrom(UDP_MAX_SIZE)
#         print('\r'+msg.decode(ENCODING)+'\n'+f'you: ',end='')


# nickname: str = 'noname'
def connect(host: str = '127.0.0.1',port: int = 9090):
    # s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))

    def receive():
        while True:
            try:
                # Receive Message From Server
                # If 'NICK' Send Nickname
                message = s.recv(1024).decode(ENCODING)
                if message == 'FILE':
                    filename = s.recv(1024).decode(ENCODING)
                    file = open(filename, "wb")
                    image_chunk = s.recv(2048)  # stream-based protocol

                    while image_chunk:
                        file.write(image_chunk)
                        image_chunk = s.recv(2048)

                    file.close()
                    print("File "+filename+" gotten successfully!");
                else:
                    print(message)
            except:
                # Close Connection When Error
                print("An error occured!")
                s.close()
                break

    def write():
        while True:
            # message = '{}: {}'.format(nickname, input())
            message = input()
            s.send(message.encode(ENCODING))

    # Starting Threads For Listening And Writing
    receive_thread = threading.Thread(target=receive)
    receive_thread.start()

    write_thread = threading.Thread(target=write)
    write_thread.start()

    # # получаем сообщения от других пользователей в фоновом режиме
    # threading.Thread(target=listen, args=(s,),daemon=True).start()
    #
    #
    # s.sendto('__join'.encode(ENCODING),(host, port))
    #
    # while True:
    #     try:
    #         msg = input(f'you: ')
    #     except KeyboardInterrupt as k:
    #         s.sendto("__exit".encode(ENCODING), (host, port))
    #         s.close()
    #         exit()
    #     s.sendto(msg.encode(ENCODING), (host, port))

if __name__ == '__main__':
    os.system('cls')
    nickname = input("Choose your nickname: ")
    print('Welcome to chat')
    connect(nickname=nickname)