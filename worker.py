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

#If some url not working, how much retrys until killing the 
MAX_TRY_ATTEMTPS = 10

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
        self.errorcounter = 0
        
    def download(self):
        oResponse = getHtml(self.url)

        if issubclass(type(oResponse), Exception):
            logger.error(f"Failed to download {self.url} Exception: {str(oResponse)} xxxCallStackxxx: {traceback.format_exc()}")
        elif oResponse.status_code != 200:
            logger.error(f"Failed to download {self.url}: Code {oResponse.status_code} Header: {oResponse.request.headers}")            
        else:
            logger.info(f"Successfully downloaded {self.url} and waiting {self.intervall}")                
            sPath = joinDir(self.path, sUrlPathToValidPathdescriptor(self.url) + sDate(dt.now()))        
            write(sPath + ".html", oResponse.content)
            return True
        
        return False
                
    def run(self):
        
        try:
            while True:
                if self.errorcounter >= 10:
                    raise Exception("Tried 10 times now killing the thread")
                if not self.download():
                    self.errorcounter += 1            
                    
                    #We increment the wating time by the error counter
                    time.sleep((self.intervall * self.errorcounter) * SEC_PER_MINUTE)                    
                else:
                    #if last download was sucessfull, than we rest the errorcounter
                    self.errorcounter = 0    
                    time.sleep(self.intervall * SEC_PER_MINUTE)
                
                                        
        except Exception as e:
            logger.error(f"Failed to download {self.url}: {e} xxxCallStackxxx: {traceback.format_exc()}")

        

def work():
    if bCanWork():  #I know twice time reading, but for later CLI and reading a file into dic cost not much
        dicToDownload = dicRead(CONFIG_PATH, bIsIntValue=True) 
        
        for k in dicToDownload:
            sPath = joinDir(WORKING_DIR ,sHostnameToValidPathdescriptor(k))
            mkDir(sPath)
                
            oToDownload = ToDownload(k, dicToDownload[k], sPath)    
            oToDownload.start()
            
        ip = None   
        try:
            ip = getHtml("https://ident.me").content
        except:
            pass
        logger.info(f"Worker Startet. My IP is: {ip}")                

    else:
        print("Cant start worker, no config data!")
 
def bCanWork():
    dicToDownload = dicRead("config.txt", bIsIntValue=True)
    if len(dicToDownload) > 0:
        return True    
    return False

work()
