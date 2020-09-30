import os
import argparse
import requests
import time
import threading
from concurrent.futures import ThreadPoolExecutor

def delection(url):
    try:
        req = requests.get(url.strip("\n"))
        if (req.status_code != 200):
            raise requests.RequestException(u"Status code error: {}".format(req.status_code))
        return req.status_code
    except requests.RequestException as e:
        e


def io(read,threads):
    fwirte = open("urls.txt","w")
    read = open(read,"r+")
    poo = ThreadPoolExecutor(max_workers=threads)
    #for i in range(100):
        #thread = my_threads(read,i)
        #thread.start()
    for i in read.readlines():
        for x in range(threads):
            stat = poo.submit(delection,i)
        if(stat.result()==200):
            print(i)
            fwirte.write(i)

    print("检测完成！")
    fwirte.close()
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