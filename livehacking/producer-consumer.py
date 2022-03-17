from threading import Thread
from queue import Queue
import time

q = Queue()

def consume():
    global q

    while True:
        item = q.get()
        print(item)

def produce():
    global q

    for i in range(10):
        q.put(i)
        time.sleep(3)

producers = []
for _ in range(3):
    producers.append(Thread(target=produce, daemon=True))

consumers = []
for _ in range(5):
    consumers.append(Thread(target=consume, daemon=True))

for t in producers:
    t.start()
for t in consumers:
    t.start()

for t in producers:
    t.join()
for t in consumers:
    t.join()


