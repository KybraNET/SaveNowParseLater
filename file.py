import os
from urllib.parse import urlparse

ENCODING="utf-8"

'''Read/Write Strings to file. 
   Read/Write Lists to file
   Read/Write Dictionaries to file'''

#region typing
def tryInt(lInt):
    try:
        return int(lInt)
    except Exception as e:
        print("Cant cast these value to INT: ", lInt)
        return None
    
def sHostnameToValidPathdescriptor(sURL):
    return urlparse(sURL).hostname.replace(".", "_")
    #NOTE: Hostnames always need some Top-Level Domain! You can use that too, buts not precise!
    #return urlparse(sURL).hostname.replace(".", "_")[-2]
#endregion

def sUrlPathToValidPathdescriptor(sURL):
    print(urlparse(sURL).path.replace("/", "__"))
    return urlparse(sURL).path.replace("/", "__")

#region Directory
def bIsDir(path):
    return os.path.isdir(path)

def mkDir(path):
    if not bIsDir(path):
        os.mkdir(path)
        return True    
    return False        

def joinDir(path, suffix): 
    return os.path.join(path, suffix)
#endregion

#region file
def bFileExist(filePath):
    return os.path.exists(filePath)

def write(filePath, sToWrite):
    if not bFileExist(filePath):
        with open(filePath, 'wb') as fw:
            fw.write(sToWrite)
    
def read(filePath):
    if bFileExist(filePath):
        with open(filePath, 'rb') as fr:
            return fr.read()
    
def lstReadLines(filePath):
    if bFileExist(filePath):
        with open(filePath, 'r', encoding=ENCODING) as fr:
            return [line.rstrip() for line in fr.readlines()]

#Always Override!
def lstWriteLines(filePath, lstToWrite):                              
    with open(filePath, "w", encoding=ENCODING) as f:        
        f.write("\n".join(lstToWrite))
        
#KeyValue split by delimiter in a row
def dicRead(filePath, delimiter=" ", bIsIntKey = False, bIsIntValue = False):
     if bFileExist(filePath):
        with open(filePath, 'r', encoding=ENCODING) as fr:
            dicRet = {}
            
            for line in fr.readlines():
                lstTuple = line.split(delimiter)
            
                if len(lstTuple) == 2:
                    key = lstTuple[0]
                    value = lstTuple[1]
            
                    if bIsIntKey:
                        key = tryInt(key)
                        if key is None:
                            continue
            
                    if bIsIntValue:
                        value = tryInt(value)
                        if value is None:
                            continue                    
            
                    dicRet[key] = value
            return dicRet

def dicWrite(filePath, dicToWrite, delimiter=" "):
    with open(filePath, "w", encoding=ENCODING) as f:        
       for k, v in dicToWrite.items():
           f.write(str(k) + delimiter + str(v) + "\n")

