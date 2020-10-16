import os
import argparse
import requests
import time
import threading
import queue
from concurrent.futures import ThreadPoolExecutor

class Threads(threading.Thread):
    def __init__(self,url):
        threading.Thread.__init__(self)
        self.url =url
    def run(self):
        fwirte = open("urls.txt", "w")
        while(True):
            if self.url.empty():
                break
            u = self.url.get()
            code = delection(u)
            if(code == 200):
                print(u)
                fwirte.write(u)

def delection(url):
    try:
        req = requests.get(url.strip("\n"))
        if (req.status_code != 200):
            raise requests.RequestException(u"Status code error: {}".format(req.status_code))
        return req.status_code
    except requests.RequestException as e:
        e


def io(read,threads):

    read = open(read,"r+")
    threadlist = []
    ip_queque = queue.Queue()
    for i in read.readlines():
        ip_queque.put(i)

    for x in range(threads):
        threadlist.append(Threads(ip_queque))

    for thd in threadlist:
        thd.start()

    for thd in threadlist:
        thd.join()

    print("检测完成！")
    read.close()

def parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t")
    parser.add_argument("-s",type=int)
    args = parser.parse_args()
    io(args.t,args.s)

def main():
    parser()

if __name__=="__main__":
    main()