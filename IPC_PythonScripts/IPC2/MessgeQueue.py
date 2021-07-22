import logging
from os import getcwd
from pathlib import Path
from random import randint
from threading import Thread
from time import sleep

# Importing Queue libraries
try:
    import queue
except ImportError:
    import queue as q

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-5s) %(message)s', )

buffer_size = 20
q = queue.Queue(buffer_size)

class Utils():
    def create_producer_data_file(self, name):
        no_of_integers_in_a_file = 100;
        f = open(getcwd() + "/Output/Producer/" + name + ".txt", "w")
        for no_of_lines in range(no_of_integers_in_a_file):
            f.write(str(randint(1, no_of_integers_in_a_file)))
        f.close()

    def create_consumer_data_file(self, name, data):
        f = open(getcwd() + "/Output/Consumer/" + name + ".txt", "w")
        f.write(data)
        f.close()

class producer_thread(Thread):
    def __init__(self, group=None, target=None, name=None,
                 args=(), kwargs={}, verbose=None):
        Path(getcwd() + "/Output/Producer").mkdir(parents=True, exist_ok=True)
        super(producer_thread, self).__init__()
        self.target = target
        self.name = name

    def run(self):
        utils = Utils();
        produced_file_num = 0;
        while produced_file_num < 100:
            if not q.full():
                utils.create_producer_data_file("producer_data_file_" + str(produced_file_num))
                item = open(
                    getcwd() + "/Output/Producer/producer_data_file_" + str(produced_file_num) + ".txt", "r")
                q.put(item.read())
                logging.debug('Putting ' + str("producer_data_file_" + str(produced_file_num))
                              + ' : ' + str(q.qsize()) + ' items in queue')
                sleep(1)
                produced_file_num += 1;
        return

class consumer_thread(Thread):
    def __init__(self, group=None, target=None, name=None,
                 args=(), kwargs={}, verbose=None):
        Path(getcwd() + "/Output/Consumer").mkdir(parents=True, exist_ok=True)
        super(consumer_thread, self).__init__()
        self.target = target
        self.name = name
        return

    def run(self):
        utils = Utils();
        consumed_files = 0
        while consumed_files < 100:
            if not q.empty():
                data = q.get()
                utils.create_consumer_data_file("consumer_data_file_" + str(consumed_files), data)
                logging.debug('Getting ' + str("producer_data_file_" + str(consumed_files))
                              + ' : ' + str(q.qsize()) + ' items in queue')
                sleep(1)
                consumed_files += 1;
        return

if __name__ == '__main__':
    p = producer_thread(name='producer')
    c = consumer_thread(name='consumer')

    p.start()
    sleep(2)
    c.start()
    sleep(2)