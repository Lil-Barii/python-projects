import socket
import time

def client():
    ip = "127.0.0.1"
    port_number = 5001
    connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Pending for connection.. ")
    time.sleep(2)
    connection.connect((ip,port_number))
    # time.sleep(60)
    print("DOne")
    connection.close()

client()