import os
from re import T
from file import *
from downloader import *
from datetime import datetime as dt
import time
from threading import Thread

#CHANGE: To the directory,where you want to Save the Data
WORKING_DIR = os.getcwd()
CONFIG_PATH = joinDir(WORKING_DIR, 'config.txt')
SEC_PER_MINUTE = 60

def sDate(dtToString):
    return dt.strftime(dtToString,'%d%m%Y_%H%M%S')

class ToDownload(Thread):
    def __init__(self, sUrl, lInterval, sPath):
        Thread.__init__(self)
        self.url = sUrl
        self.path = sPath
        self.intervall = lInterval 
        self.counter = 1
        
    def download(self):
        sPath = joinDir(self.path, sDate(dt.now()))
        html = getHtml(self.url)
        if html is not None:
            write(sPath + ".html", html)
            return True
        return False

    def run(self):
        while True:
            self.download()
            print("Downloaded: {0} Waiting {1} minutes".format(self.url, str(self.intervall)))
            time.sleep(self.intervall * SEC_PER_MINUTE)

def work():
    if bCanWork():  #I know twice time reading, but for later CLI and reading a file into dic cost not much
        dicToDownload = dicRead(CONFIG_PATH, bIsIntValue=True) 
        
        for k in dicToDownload:
            sPath = joinDir(WORKING_DIR ,sHostnameToValidPathdescriptor(k))
            mkDir(sPath)
                
            oToDownload = ToDownload(k, dicToDownload[k], sPath)    
            oToDownload.start()
    else:
        print("Cant start worker, no config data!")
 
def bCanWork():
    dicToDownload = dicRead("config.txt", bIsIntValue=True)
    if len(dicToDownload) > 0:
        return True    
    return False

work()