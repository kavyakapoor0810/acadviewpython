#question1
import threading
from threading import Thread
import time
class mythread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        time.sleep(5)
        print("Value after 5seconds")
th=mythread()
th.start()

#question2

class mythread1(threading.Thread):
    def __init__(self):
       threading.Thread.__init__(self)

    def run(self):
        for i in range(1,11):
            time.sleep(1)
            print(i)
thr=mythread1()
thr.start()

#question4

class mythread2(threading.Thread):
    def __init__(self,i):
        threading.Thread.__init__(self)
        self.i=i

    def factorial(n):
        if n == 0:
            return n
        else:
            return n * factorial(n - 1)
thre=mythread2()
thre.factorial(5)
thre.start()
