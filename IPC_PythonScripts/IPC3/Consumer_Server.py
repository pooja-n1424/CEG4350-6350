import os
import pathlib
import random
import socket
import threading
from _thread import *

lock = threading.Lock()
# Store information
def create_consumer_data_file(name, data):
    f = open(os.getcwd() + "/Output/Consumer_Socket/" + name + ".txt", "w")
    f.write(data)
    f.close()

def thread(c):
    while True:
        data = c.recv(4096)
        if not data:
            print('No Messages from Producer')
            # Thread lock release on quit
            lock.release()
            break

        dataString = data.decode("utf-8")
        print("Data Received and storing to a file")
        create_consumer_data_file("consumer_" + str(random.randint(1, 100)), str(dataString))
        c.send("Successfully stored information on the consumer side ".encode())
    c.close()

def Main():
    host = ""
    pathlib.Path(os.getcwd() + "/Output/Consumer_Socket").mkdir(parents=True, exist_ok=True)
    # server port
    port = 51564
    # Socket module to create a Consumer(Server) Socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    print("Plug connected to Port", port)
    s.listen(5)
    print("Outlet Plug is listening")
    while True:
        c, addr = s.accept()
        lock.acquire()
        print('Linked to :', addr[0], ':', addr[1])
        start_new_thread(thread, (c,))
    s.close()

if __name__ == '__main__':
    Main()