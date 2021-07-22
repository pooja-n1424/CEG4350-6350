import os
import pathlib
import random
import socket

def create_producer_data_file(name):
    no_of_integers_in_a_file = 100;
    f = open(os.getcwd() + "/Output/Producer_Socket/" + name + ".txt", "w")
    for no_of_lines in range(no_of_integers_in_a_file):
        f.write(str(random.randint(1, no_of_integers_in_a_file)))
    f.close()

def Main():

    host = '127.0.0.1'
    port = 51564
    so = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    so.bind((host, 8080))
    so.connect((host, port))
    pathlib.Path(os.getcwd() + "/Output/Producer_Socket").mkdir(parents=True, exist_ok=True)
    produced_file_num = 0;
    while produced_file_num < 100:
        # create a file
        create_producer_data_file("produceddatafile_" + str(produced_file_num))
        # File user send to a Consumer(Server)
        file = open(os.getcwd() + "/Output/Producer_Socket/produceddatafile_" + str(produced_file_num) + ".txt",
                    "rb")
        # Send data
        SendData = file.read(4096)
        so.send(SendData)
        # Message received from Consumer(Server)
        note = so.recv(2048)
        print('Obtained from the server :', str(note.decode('ascii')))
        produced_file_num += 1;
    so.close()


if __name__ == '__main__':
    Main()