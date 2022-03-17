from threading import Thread, Lock

i = 0
lock = Lock()

def increment():
    global i
    for _ in range(10*1000*1000):
        lock.acquire()
        i += 1
        lock.release()

t1 = Thread(target=increment, daemon=True)
t2 = Thread(target=increment, daemon=True)
t1.start()
t2.start()

t1.join()
t2.join()

print(i)
