import socket
import threading
import time

# количество портов у хоста 65536
N = 2**16

def scan(host: str = '127.0.0.1'):
    ports = set()
    opens = set()
    def connect(start: int = 9090, length: int = 100):
        # print(start)
        for port in range(start,min(N,start+length),1):
            # if (port == start):
            #     print("Start: ",start)
            # elif (port == min(N,start+length)-1):
            #     print("End: ", start," ", min(N,start+length)-1)
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # если сокет не ответит в течении 5 секунд, считать его недоступным
            s.settimeout(5.0)
            try:
                # print(port)
                s.connect((host, port))

                # s.create_connect((host, port))
                # print("Порт", port, "открыт")
                opens.add(port)
            except:
                # порт закрыт
                # print("Порт", port, "закрыт")
                pass
            finally:
                ports.remove(port)
                s.close()

    # print(N)
    # print(threading.activeCount())
    ports = set()
    for i in range(0, (N // 100) + 1):
        for j in range(i * 100, min(N, (i + 1) * 100), 1):
            ports.add(j)
    # ports.remove(100)
    # all = len(ports)

    ports_in_thread = 10
    for i in range(0,(N//ports_in_thread)+1):
    # for i in range(4,5):
        # print(i*100)
    #     print("d"+min(N, (0 + 100)))
    #     for j in range(i*100, min(N, (i+1)*100), 1):
        # print(j)
        threading.Thread(target=connect,args=(i*ports_in_thread,ports_in_thread)).start()

    # count = threading.activeCount()-1
    # all = N // 100 + 1
    # print(all)
    # print(count)
    print("Start scanning...")
    while len(ports):
         # if len(ports)<100:
         #    print(ports)

    #      count = threading.activeCount() - 1
    #      all = N//100 + 1
    # #     # print('\r'+str(N//100),end='')
    # #     # print(count)
    #      progress = (all-count)/all
         print(f'\rprogress: {(N-len(ports))/N:.2%}',end='')
         time.sleep(0.5)
    print('\n')


    for open_port in sorted(opens):
        print("Порт", open_port, "открыт")







if __name__ == '__main__':
    scan()


