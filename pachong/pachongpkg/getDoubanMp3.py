# coding=utf-8

import urllib
import urllib2
import re
import time


def SaveTop20Music(currtime):
    rex = r'<a href="javascript:;">(.*?)</a>';
    url = 'http://music.douban.com/chart';
    Response = urllib2.urlopen(url);
    Html = Response.read();
    listsofsong = re.findall(rex, Html);
    print len(listsofsong);
    f = open('%s.txt' % currtime, 'w');
    x = 1;
    for line in listsofsong:
        f.write('top' + str(x) + ':' + line);
        f.write('\n');
        x = x + 1;
        f.flush();

    f.close();
    print currtime + '.txt' + '\t\t' + 'SaveOver'


def timer(n):
    while True:
        currtime = time.strftime("Savetime_%H-%M-%S", time.localtime())
        print currtime
        SaveTop20Music(currtime)
        time.sleep(n)


if __name__ == "__main__":
    timer(5)
