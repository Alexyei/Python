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
                # print("message")
                if message == 'FILE':
                    filename = s.recv(1024).decode(ENCODING)
                    file = open("_client_folder/"+filename, "wb")
                    file_chunk = s.recv(2048)  # stream-based protocol

                    while file_chunk:
                        if b'\x00' == file_chunk:
                            break
                        file.write(file_chunk)
                        file_chunk = s.recv(2048)
                        # print(file_chunk)
                        # print("cicle")
                    # print("stop get")
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
            if message.startswith("send "):
                words = message.split(' ')
                # command = words[0]
                parametrs = words[1:]
                if (len(parametrs) < 1):
                    print('need 1 parameter: file name')
                    continue
                if not os.path.isfile("_client_folder/"+parametrs[0]):
                    print("file not found")
                    continue
                s.send(message.encode(ENCODING))
                # s.send('FILE'.encode(ENCODING))
                # s.send(parametrs[0].encode(ENCODING))
                file = open("_client_folder/"+parametrs[0], 'rb')
                file_data = file.read(2048)

                while file_data:
                    # print("1")
                    # print(file_data)
                    s.send(file_data)
                    file_data = file.read(2048)

                # print("stop send")
                file.close()
                s.send(b'\x00')

                print("file " + parametrs[0] + " sent successfully!")
            else:
                s.send(message.encode(ENCODING))
            # print("send")

    # Starting Threads For Listening And Writing
    receive_thread = threading.Thread(target=receive)
    receive_thread.start()

    write_thread = threading.Thread(target=write)
    write_thread.start()


if __name__ == '__main__':
    os.system('cls')
    # nickname = input("Choose your nickname: ")
    print('Welcome to chat')
    # nickname=nickname
    connect()