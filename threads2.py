import logging
import random
import threading
import time

logging.basicConfig(
    level=logging.DEBUG,
    format='(%(threadName)-10s) %(message)s',
)


class Counter(object):
    def __init__(self, start=0):
        self.lock = threading.Lock()
        self.value = start

    def increment(self):
        logging.debug('Waiting for lock')
        self.lock.acquire()
        try:
            logging.debug('Acquired lock')
            self.value = self.value + 1
        finally:
            logging.debug('Release lock')
            time.sleep(1)
            self.lock.release()


def worker(counter):
    for index in range(2):
        counter.increment()
    logging.debug('Done')


counter = Counter()
for index in range(2):
    t1 = threading.Thread(target=worker, args=(counter,))
    t1.start()

logging.debug('Waiting for worker threads')

main_thread = threading.currentThread()
for t1 in threading.enumerate():
    if t1 is not main_thread:
        t1.join()

logging.debug('Counter: %d', counter.value)
