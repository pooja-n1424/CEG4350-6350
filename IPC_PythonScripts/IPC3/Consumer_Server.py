import os
import pathlib
import random
import socket
import threading
from _thread import *

print_lock = threading.Lock()


# Store information
def create_consumer_data_file(name, data):
    f = open(os.getcwd() + "/Output/Consumer_Socket/" + name + ".txt", "w")
    f.write(data)
    f.close()


# thread function
def threaded(c):
    while True:
        # Data received from Producer(Client)
        data = c.recv(4096)
        if not data:
            print('No Messages from Producer, Good Bye!')
            # lock released on exit
            print_lock.release()
            break

        dataString = data.decode("utf-8")
        print("Data Received and storing to a file")

        # reverse the given string from Producer(Client)
        create_consumer_data_file("consumer_" + str(random.randint(1, 100)), str(dataString))
        # send back reversed string to Producer(Client)
        c.send("Successfully stored data on the consumer side ".encode())

    # connection closed
    c.close()


def Main():
    host = ""
    pathlib.Path(os.getcwd() + "/Output/Consumer_Socket").mkdir(parents=True, exist_ok=True)

    # server port
    port = 12345

    # Socket module to create a Consumer(Server) Socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    print("socket bind-ed to port", port)

    # Establish the socket into listening mode for Producer(Client) data reading
    s.listen(5)
    print("socket is listening")

    # a forever loop until client wants to exit
    while True:
        # Establish connection with Producer(Client)
        c, addr = s.accept()
        # Lock acquired by Producer(Client)
        print_lock.acquire()
        print('Connected to :', addr[0], ':', addr[1])
        # Start a new thread and return its identifier
        start_new_thread(threaded, (c,))
    s.close()


if __name__ == '__main__':
    Main()