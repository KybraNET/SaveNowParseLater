import os
from re import T
from file import *
from downloader import *
from datetime import datetime as dt
import time
from threading import Thread
import traceback, sys
import logging

#CHANGE: To the directory,where you want to Save the Data
WORKING_DIR = os.getcwd()
CONFIG_PATH = joinDir(WORKING_DIR, 'config.txt')
SEC_PER_MINUTE = 60

LOGS = WORKING_DIR + "logs.txt"

#https://pythonexamples.org/python-logging-info/
#region Logging-Init
logger = logging.getLogger('mylogger')
#set logger level
logger.setLevel(logging.INFO)
#or you can set the following level
#logger.setLevel(logging.DEBUG)

handler = logging.FileHandler('mylog.log')
# create a logging format
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
#endregion

#region helper
def sDate(dtToString):
    return dt.strftime(dtToString,'%d%m%Y_%H%M%S')

def writeLog(sToLog):
    with open(LOGS, 'a') as fw:
        fw.write(sToLog)
#endregion
    
class ToDownload(Thread):
    def __init__(self, sUrl, lInterval, sPath):
        Thread.__init__(self)
        self.url = sUrl
        self.path = sPath
        self.intervall = lInterval 
        self.counter = 1
        
    def download(self):
        sPath = joinDir(self.path, sUrlPathToValidPathdescriptor(self.url) + sDate(dt.now()))        
        #print(sPath)
        html = getHtml(self.url)
        if html is not None:
            write(sPath + ".html", html)
            return True
        return False

    def run(self):
        
        try:
            while True:
                if self.download():
                #print("Downloaded: {0} Waiting {1} minutes".format(self.url, str(self.intervall)))
                    logger.info(f"Successfully downloaded {self.url} and waiting {self.intervall}")                
                    time.sleep(self.intervall * SEC_PER_MINUTE)
                elif self.download():
                    logger.info(f"Successfully downloaded {self.url} and waiting {self.intervall}")                
                    time.sleep(self.intervall * SEC_PER_MINUTE)
                else:
                    raise Exception('Server Response is not a 200 ok code!')
                    
        except Exception as e:

            logger.error(f"Failed to download {self.url}: {e} xxxCallStackxxx: {traceback.format_exc()}")
            
            #TODO: Den ganzen StakcTrace noch mit Loggen ?
            
            #TODO: Wollen wir nach ner bestimmenten anzahl
            #z.B der ist hier drei mal hintereinander rein gelaufen, dann
            # fegen wir den raus aus den worker, quee, oder benachrichtigen ggf?
            
            # #NOTE: Logging after Download if faile!
            # print("WRITE LOGS")
            # exc = sys.exc_info()[0]
            # #stack = traceback.extract_stack()[:-1]  # last one would be full_stack()
            # writeLog(str(dt.now()) + "__" + self.url + "__" + "xxxSTACKxxx: " + traceback.format_exc())
        

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
