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

#question3

class mythread3(threading.Thread):
    def __init__(self):
       threading.Thread.__init__(self)

    def run(self):
        l = [1, 2, 3, 4, 5]
        for i in l:
            print(i)
            r=[2,4,6,8,10]
            for j in r:
                time.sleep(j)

thread=mythread3()
thread.start()

#question4

import math

class mythread2(threading.Thread):
    def __init__(self,i):
        threading.Thread.__init__(self)
        self.i=i
    def run(self):
        print(math.factorial(self.i))
i=int(input("enter no. for which u want to calc factorial"))
thre=mythread2(i)
thre.start()
