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
    # local host IP '127.0.0.1'
    host = '127.0.0.1'

    # Define the port on which Consumer(Server) want to connect with Producer(Client)
    port = 12345

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, 8080))

    # Connect to Consumer(Server) on local Producer(Client) System
    s.connect((host, port))

    pathlib.Path(os.getcwd() + "/Output/Producer_Socket").mkdir(parents=True, exist_ok=True)

    produced_file_num = 0;

    while produced_file_num < 100:
        # create a file
        create_producer_data_file("produceddatafile_" + str(produced_file_num))

        # s.send(f"produceddatafile_" + str(produced_file_num).encode())

        # File user send to a Consumer(Server)
        file = open(os.getcwd() + "/Output/Producer_Socket/produceddatafile_" + str(produced_file_num) + ".txt",
                    "rb")

        # Send data
        SendData = file.read(4096)

        # Data sent to Consumer(Server)
        s.send(SendData)

        # Messaga received from Consumer(Server)
        message = s.recv(1024)

        # Message from the Consumer(Server)
        print('Received from the server :', str(message.decode('ascii')))

        produced_file_num += 1;
    # close the connection
    s.close()


if __name__ == '__main__':
    Main()