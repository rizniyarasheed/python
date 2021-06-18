import threading
import time

def display():
    for i in range(1,8):
        time.sleep(3)
        print("child thread executing")
    print(threading.currentThread().getName())

t=threading.Thread(target=display)
t.start()

begintime=time.time()
print("begin time",begintime)
t.join()

for i in range(1,8):
    time.sleep(3)
    print("main thread is executing")
print(threading.currentThread().getName())

endtime=time.time()
total=endtime-begintime
print("total time taken",total)


