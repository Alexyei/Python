import socket

UDP_MAX_SIZE = 65535
ENCODING = "utf-8"

def listen(host: str = '127.0.0.1',port: int = 9090):
    # socket.AF_INET -ipv4, socket.SOCK_DGRAM - протокол UDP
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((host, port))
    print(f'Listening at {host}:{port}')

    members = set()
    while True:
        try:
            msg, addr = s.recvfrom(UDP_MAX_SIZE)
        except ConnectionResetError as e:
            print("ERR")
            continue
            # print(e)


        # print("MESSAGE")
        # print(msg.decode(ENCODING))

        # добавить пользователя к участникам чата
        if addr not in members:
            members.add(addr)

        # если сообщение пустое ничего не делать
        if not msg:
            continue

        # addr - хост, порт
        # здесь для упрощения client_id == port, хотя они могут повторятся если клиенты на разных хостах (компьютерах)
        client_id = addr[1]
        if msg.decode(ENCODING) == '__join':
            # print(f'Client {client_id} joined chat')
            msg = f'Client {client_id} joined chat'
            print(msg)
            # continue
        elif msg.decode(ENCODING) == '__exit':
            members.remove(addr)
            msg = f'Client {client_id} exit from chat'
            print(msg)
        else:
            msg = f'client {client_id}:{msg.decode(ENCODING)}'
        # msg = f'client {client_id}:{msg.decode(ENCODING)}'
        # отправить сообщение другим полдьзователям
        for member in members:
            if member == addr:
                continue
            try:
                result = s.sendto(msg.encode(ENCODING),member)
            #     print("RESULT")
            #     print(result)
            #     if not result:
            #         raise Exception("нет данных!")
            except ConnectionResetError as e:
                print("mess ERR")
                continue


if __name__ == '__main__':
    listen()