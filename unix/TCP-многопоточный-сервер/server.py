import socket
import threading
# UDP_MAX_SIZE = 65535
ENCODING = "utf-8"



def listen(host: str = '127.0.0.1',port: int = 9090):
    # socket.AF_INET -ipv4, socket.SOCK_STREAM - протокол TCP
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((host, port))
    # listen без аргументов, количество клиентов не ограниченно
    s.listen()
    print(f'Listening at {host}:{port}')

    # Lists For Clients and Their Nicknames
    clients = []
    nicknames = []

    def broadcast(message, author):
        for client in clients:
            if author != client:
                client.send(message)

    # Handling Messages From Clients
    def handle(client):
        while True:
            try:
                # Broadcasting Messages
                message = client.recv(1024)
                broadcast(message, client)
            except:
                # Removing And Closing Clients
                # print("LEFT")
                index = clients.index(client)
                clients.remove(client)
                client.close()
                nickname = nicknames[index]
                print('{} left!'.format(nickname))
                broadcast('{} left!'.format(nickname).encode(ENCODING), client)
                nicknames.remove(nickname)
                break

    while True:
        # Accept Connection
        client, address = s.accept()
        print("Connected with {}".format(str(address)))

        # Request And Store Nickname
        client.send('NICK'.encode(ENCODING))
        nickname = client.recv(1024).decode('ascii')
        nicknames.append(nickname)
        clients.append(client)

        # Print And Broadcast Nickname
        print("Nickname is {}".format(nickname))
        broadcast("{} joined!".format(nickname).encode(ENCODING), client)
        client.send('Connected to server!'.encode(ENCODING))

        # Start Handling Thread For Client
        thread = threading.Thread(target=handle, args=(client,))

        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")
    # members = set()
    # while True:
    #     try:
    #         msg, addr = s.recvfrom(UDP_MAX_SIZE)
    #     except ConnectionResetError as e:
    #         print("ERR")
    #         continue
    #         # print(e)
    #
    #
    #     # print("MESSAGE")
    #     # print(msg.decode(ENCODING))
    #
    #     # добавить пользователя к участникам чата
    #     if addr not in members:
    #         members.add(addr)
    #
    #     # если сообщение пустое ничего не делать
    #     if not msg:
    #         continue
    #
    #     # addr - хост, порт
    #     # здесь для упрощения client_id == port, хотя они могут повторятся если клиенты на разных хостах (компьютерах)
    #     client_id = addr[1]
    #     if msg.decode(ENCODING) == '__join':
    #         # print(f'Client {client_id} joined chat')
    #         msg = f'Client {client_id} joined chat'
    #         print(msg)
    #         # continue
    #     elif msg.decode(ENCODING) == '__exit':
    #         members.remove(addr)
    #         msg = f'Client {client_id} exit from chat'
    #         print(msg)
    #     else:
    #         msg = f'client {client_id}:{msg.decode(ENCODING)}'
    #     # msg = f'client {client_id}:{msg.decode(ENCODING)}'
    #     # отправить сообщение другим полдьзователям
    #     for member in members:
    #         if member == addr:
    #             continue
    #         try:
    #             result = s.sendto(msg.encode(ENCODING),member)
    #         #     print("RESULT")
    #         #     print(result)
    #         #     if not result:
    #         #         raise Exception("нет данных!")
    #         except ConnectionResetError as e:
    #             print("mess ERR")
    #             continue


if __name__ == '__main__':
    listen()