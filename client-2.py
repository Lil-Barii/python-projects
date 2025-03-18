import socket
import time

def client():
    ip = "127.0.0.1"
    port_number = 5001
    connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Pending for connection.. ")
    connection.connect((ip,port_number))
    message = "Sample-Message-2"
    time.sleep(10)
    connection.sendall(message.encode("utf-8"))
    print("DOne")
    

client()