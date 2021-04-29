import datetime
import socket

# Проверять работу через браузер: http://127.0.0.1:8080/

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1',8080))
server.listen(4)
print('Server working...')
# print(datetime.datetime.utcnow())
# print(len('Well done, buddy...'.encode('utf-8')))
client_socket, address = server.accept()

data = client_socket.recv(1024).decode('utf-8')
print(data)
# пустая строка в конце HDRS нужна для отделение заголовка от ответа
HDRS = f'HTTP/1.1 200 OK\r\nServer: SelfMadeServer v0.0.1\r\nContent-type: text/html; charset=utf-8\r\nDate: {datetime.datetime.utcnow()}\r\nContent-Length: "{19}"\r\nConnection: close\r\n\r\n'
content = 'Well done, buddy...'.encode('utf-8')

client_socket.send(HDRS.encode('utf-8')+content)
print('Server shutdown')