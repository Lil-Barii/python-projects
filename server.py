import socket
import time

from threading import *

#print(socket.gethostbyname(socket.gethostname()))
def serv():
    ip="127.0.0.1"
    port_number= 5001
    connection = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    connection.bind((ip,port_number))
    print("Pending to load the system")
    connection.listen(3)
    return connection



def server(connection):
    conn, addr = connection.accept()
    # time.sleep(10)
    while True:
        message = conn.recv(1024).decode("utf-8")
        if message:
            print(message)
        else:
            break
    print("DOne")
    connection.close()
connection=serv()
t1=Thread(target=server , args=( connection ,))
t2=Thread(target=server , args=( connection ,))
t3=Thread(target=server , args=( connection ,))
t1.start()
t2.start()
t3.start()