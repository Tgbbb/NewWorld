import threading
import time

threadLock = threading.Lock()

class Mbank:
    global sum
    sum=2000
    def take(k):
        global sum
        temp=sum
        temp=temp - k
        time.sleep(0.2)
        sum = temp
        print('sum=',sum)
class MyThread(threading.Thread):
    tickets=10
    def __init__ (self):
        threading.Thread.__init__(self)
    def run(self):
        for i in range(1,5):
            threadLock.acquire()
            Mbank.take(100)
            threadLock.release()
def main():
    t1 = MyThread()
    t1.start()
    t2 = MyThread()
    t2.start()
if __name__ =="__main__":
    main()