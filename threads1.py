import time
import threading

def worker(number):
    print('Worker {0}'.format(number))
    time.sleep(100)



threads = []
for index in range(5):
    thread = threading.Thread(target=worker, args=(index,))
    thread.start()
    
    threads.append(thread)


print("End")
