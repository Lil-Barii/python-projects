import socket
import time

def client():
    ip = "127.0.0.1"
    port_number = 5001
    connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Pending for connection.. ")
    connection.connect((ip,port_number))
    message = "Sample-Message-1"
    time.sleep(20)
    connection.sendall(message.encode("utf-8"))
    print("DOne")
    

client()