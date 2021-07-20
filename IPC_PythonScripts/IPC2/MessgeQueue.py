import logging
import os
import pathlib
import random
import threading
import time

try:
    import queue
except ImportError:
    import Queue as queue

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-9s) %(message)s', )

BUF_SIZE = 20
q = queue.Queue(BUF_SIZE)

class Utils():
    def create_producer_data_file(self, name):
        no_of_integers_in_a_file = 100;
        f = open(os.getcwd() + "/Data/RunOutput/Producer/" + name + ".txt", "w")
        for no_of_lines in range(no_of_integers_in_a_file):
            f.write(str(random.randint(1, no_of_integers_in_a_file)))
        f.close()

    def create_consumer_data_file(self, name, data):
        f = open(os.getcwd() + "/Data/RunOutput/Consumer/" + name + ".txt", "w")
        f.write(data)
        f.close()

class ProducerThread(threading.Thread):
    def __init__(self, group=None, target=None, name=None,
                 args=(), kwargs=None, verbose=None):
        pathlib.Path(os.getcwd() + "/Data/RunOutput/Producer").mkdir(parents=True, exist_ok=True)
        super(ProducerThread, self).__init__()
        self.target = target
        self.name = name

    def run(self):
        utils = Utils();
        produced_file_num = 0;
        while produced_file_num < 100:
            if not q.full():
                utils.create_producer_data_file("producer_data_file_" + str(produced_file_num))
                item = open(
                    os.getcwd() + "/Data/RunOutput/Producer/producer_data_file_" + str(produced_file_num) + ".txt", "r")
                q.put(item.read())
                logging.debug('Putting ' + str("producer_data_file_" + str(produced_file_num))
                              + ' : ' + str(q.qsize()) + ' items in queue')
                time.sleep(1)
                produced_file_num += 1;
        return

class ConsumerThread(threading.Thread):
    def __init__(self, group=None, target=None, name=None,
                 args=(), kwargs=None, verbose=None):
        pathlib.Path(os.getcwd() + "/Data/RunOutput/Consumer").mkdir(parents=True, exist_ok=True)
        super(ConsumerThread, self).__init__()
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
                time.sleep(1)
                consumed_files += 1;
        return

if __name__ == '__main__':
    p = ProducerThread(name='producer')
    c = ConsumerThread(name='consumer')

    p.start()
    time.sleep(2)
    c.start()
    time.sleep(2)