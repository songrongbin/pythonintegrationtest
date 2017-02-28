import threading
import time

mylock = threading.RLock()
num = 0


class myThread(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.t_name = name

    def run(self):
        global num
        while True:
            mylock.acquire()
            print '\nThread(%s) locked, Number: %d' % (self.t_name, num)
            if num >= 10:
                mylock.release()
                print 'num >=10 thread over!'
                break
            num += 1
            print '\nThread(%s) released, Number: %d' % (self.t_name, num)
            time.sleep(1)
            mylock.release()


def test():
    thread1 = myThread('A')
    thread2 = myThread('B')
    thread1.start()
    thread2.start()


if __name__ == '__main__':
    test()
