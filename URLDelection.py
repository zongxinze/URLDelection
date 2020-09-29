import os
import argparse
import requests
import time
import threading

class my_threads(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        parser()


def delection(url):
    try:
        req = requests.get(url.strip("\n"))
        if (req.status_code != 200):
            raise requests.RequestException(u"Status code error: {}".format(req.status_code))
        return req.status_code
    except requests.RequestException as e:
        e


def io(read):
    fwirte = open("urls.txt","w")
    read = open(read,"r+")
    for i in read.readlines():
        if(delection(i)==200):
            print(i)
            fwirte.write(i)
    print("检测完成！")
    fwirte.close()
    read.close()

def parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t")
    args = parser.parse_args()
    io(args.t)

def main():
    for i in range(10):
        thread = my_threads()
        thread.start()
    #parser()

if __name__=="__main__":
    main()