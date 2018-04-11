'''
import threading
class x(threading.Thread):
    def run(self):
        for i in range(10):
            print i
x1=x()
x1.start()
for s in range(10,20):
    print s

import threading
import time
class x(threading.Thread):
    def run(self):
        time.sleep(2)
        for p in range(10):
            print p
class y(threading.Thread):
    def run(self):
        for s in range(10,20):
            print s
x1=x()
x1.start()
y1=y()
y1.start()

'''
import threading
import time
class thread1(threading.Thread):
    def run(self):
        threadlock.acquire()
        f1("python")
        threadlock.release()
class thread2(threading.Thread):
    def run(self):
        threadlock.acquire()
        f1("hadoop")
        threadlock.release()
def f1(x):
    print "[hello[",x
    time.sleep(5)
    print "]world]"
threadlock=threading.Lock()
t1=thread1()
t1.start()
t2=thread2()
t2.start()

    
