import os
import pathlib
import random

def create_producer_data_file(name):
    no_of_integers_in_a_file = 100;
    f = open(os.getcwd() + "/Output/Producer/" + name + ".txt", "w")
    for no_of_lines in range(no_of_integers_in_a_file):
        f.write(str(random.randint(1, no_of_integers_in_a_file)))
    f.close()

#Store information
def create_consumer_data_file(name, data):
    f = open(os.getcwd() + "/Output/Consumer/" + name + ".txt", "w")
    f.write(data)
    f.close()

def communication(producer_file_name, producer_file_data):
    re, wr = os.pipe()
    process_id = os.fork()
    if process_id:
        os.close(wr)
        re = os.fdopen(re)
        print ("Parent_Process read")
        str = re.read()
        print( "Parent_Process reads =", str)
    else:
        os.close(re)
        wr = os.fdopen(wr, 'w')
        print ("Child_Process writing")
        wr.write(producer_file_data)
        print("Child_Process writes = ", producer_file_data)
        create_consumer_data_file(producer_file_name, producer_file_data)
        wr.close()

if __name__ == '__main__':
    pathlib.Path(os.getcwd() + "/Output/consumer/").mkdir(parents=True, exist_ok=True)
    pathlib.Path(os.getcwd() + "/Output/producer/").mkdir(parents=True, exist_ok=True)
    for x in range(2):
        producer_file_name = "produceddatafile_" + str(x)
        create_producer_data_file(producer_file_name)
        producer_file = os.open(os.getcwd() + "/Output/producer/" + producer_file_name + ".txt", os.O_RDWR | os.O_CREAT)
        re = os.fdopen(producer_file)
        producer_file_data = re.read()
        communication(producer_file_name, producer_file_data)