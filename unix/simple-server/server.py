# import socket
#
# sock = socket.socket()
# sock.bind(('', 9090))
# sock.listen(0)
# conn, addr = sock.accept()
# print(addr)
#
# msg = ''
#
# while True:
#     data = conn.recv(1024)
#     if not data:
#         print("BREAK")
#         break
#     msg += data.decode()
#     conn.send(data)
#
# print(msg)
#
# conn.close()
# !/usr/bin/env python
# -*- coding: utf-8 -*-

import socket

sock = socket.socket()
port = input("введите порт:")
if port == '':
    port = 9090
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind(('', int(port)))

while True:
    print("слушаем порт", int(port))
    sock.listen(1)

    try:
        conn, addr = sock.accept()
    except KeyboardInterrupt as k:
        print(k)
        print("Stop program")
        exit()

    print('connection established:', addr[1])

    while True:

        try:
            data = conn.recv(1024).decode("utf8")
        except ConnectionResetError as e:
            print(e)
            print("lost connection from client")
            exit()
        except KeyboardInterrupt as k:
            print(k)
            print("Stop program")
            print("lost connection from client")
            exit()

        if not data:
            print("Конец связи")
            break

        if data in ['sstop','exit']:
            conn.send(data.upper().encode())
            break
        conn.send(data.upper().encode())

    if data in ['sstop','exit']:
        break

conn.close()

