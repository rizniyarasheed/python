from threading import  *

class Mythread(Thread):

    def run(self):
        for i in range(10):
            print("inside thread class ")

obj=Mythread()
obj.run()
#obj.start()
#obj.join()

for i in range(10):
    print(" main thread class")