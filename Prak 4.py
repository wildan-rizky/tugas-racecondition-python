import threading

lock1 = threading.Lock()
lock2 = threading.Lock()

def high_priority():
    while True:
        with lock1:
            with lock2:
                # kerja sangat cepat, tanpa sleep
                pass

def thread1():
    with lock1:
        with lock2:
            print("Thread 1 selesai")

def thread2():
    with lock1:
        with lock2:
            print("Thread 2 selesai")

t_high = threading.Thread(target=high_priority)
t1 = threading.Thread(target=thread1)
t2 = threading.Thread(target=thread2)

t_high.start()
t1.start()
t2.start()
