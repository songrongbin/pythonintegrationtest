# coding=utf-8
import webbrowser
import time
import urllib2
import re
import os
import thread
import threading

mylock = threading.RLock()

tabcount = 1


def BlogFun(n, url, MaxVisitor, threadnumber):
    visitcount = r'<span class="link_view" title="阅读次数">(\d+)人阅读</span>'
    global tabcount
    while True:
        mylock.acquire()
        if tabcount > 10:
            os.system('taskkill /F /IM chrome.exe')
            tabcount = 1
        else:
            tabcount = tabcount + 1
        mylock.release()
        webbrowser.open(url, new=1)
        request = urllib2.Request(url)
        request.add_header('User-Agent',
                           'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6')
        opener = urllib2.build_opener()
        fblog = opener.open(request)
        htm = fblog.read()
        Ref = re.findall(visitcount, htm)
        time.sleep(n)
        if int(Ref[0]) > MaxVisitor:
            break


if __name__ == "__main__":

    main_url = "http://blog.csdn.net/u013018721/article/details/37996979"

    threadSum = 5
    MaxVisitor = 1050
    timedelay = 3
    print main_url + " 开启模式... " + "\n"
    for threadnumber in range(threadSum):
        thread.start_new_thread(BlogFun, (timedelay, main_url, MaxVisitor, threadnumber,))
        threadnumber = threadnumber + 1

    print "Main Thread Over.............."
