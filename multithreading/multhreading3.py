import threading
import time

def display():
    for i in range(1,5):
        time.sleep(3)
        print("child thread is executing")
    print(threading.currentThread().getName())


t=threading.Thread(target=display)
t.start()


for i in range(1,5):
    time.sleep(3)
    print("main thread is executing")
print(threading.currentThread().getName())