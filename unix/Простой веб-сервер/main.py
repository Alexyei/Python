import datetime
import socket


# Проверять работу через браузер: http://127.0.0.1:8080/
def start_my_server():
    try:
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind(('127.0.0.1', 8080))
        server.listen(4)
        print('Server working...')
        while True:
            # print(datetime.datetime.utcnow())
            # print(len('Well done, buddy...'.encode('utf-8')))
            client_socket, address = server.accept()

            data = client_socket.recv(1024).decode('utf-8')
            if not data:
                continue
            print(data)
            content = load_page_from_get_request(data)

            client_socket.send(content)
            client_socket.shutdown(socket.SHUT_WR)
    except KeyboardInterrupt:
        server.close()
        print('Server shutdown')


def load_page_from_get_request(request_data):
    # из строки GET /openserver/phpmyadmin/index.php HTTP/1.1
    # получаем /openserver/phpmyadmin/index.php
    print(request_data)
    path = request_data.split(' ')[1]

    if path == '/':
        path = '/index.html'
    response = ''
    try:
        with open('views' + path, 'rb') as file:
            response = file.read()

        # пустая строка в конце HDRS нужна для отделение заголовка от ответа
        HDRS = f'HTTP/1.1 200 OK\r\nServer: SelfMadeServer v0.0.1\r\nContent-type: text/html; charset=utf-8\r\nDate: {datetime.datetime.utcnow()}\r\nContent-Length: "{len(response)}"\r\nConnection: close\r\n\r\n'

        return HDRS.encode('utf-8') + response
    except FileNotFoundError:
        response = '404 NOT FOUND'.encode('utf-8')
        # пустая строка в конце HDRS нужна для отделение заголовка от ответа
        HDRS_404 = f'HTTP/1.1 404 OK\r\nServer: SelfMadeServer v0.0.1\r\nContent-type: text/html; charset=utf-8\r\nDate: {datetime.datetime.utcnow()}\r\nContent-Length: "{len(response)}"\r\nConnection: close\r\n\r\n'

        return HDRS_404.encode('utf-8') + response



if __name__ == '__main__':
    start_my_server()
