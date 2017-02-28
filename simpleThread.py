import thread


def childthread(threadid):
    print "I am child thread", threadid


def parentthread():
    i = 0
    while 1:
        i += 1
        thread.start_new_thread(childthread, (i,))
        if raw_input() == 'q':
            break


parentthread()
