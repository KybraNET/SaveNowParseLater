import os
ENCODING="utf-8"

'''Read/Write Strings to file. 
   Read/Write Lists to file
   Read/Write Dictionaries to file'''

#region typing
def tryInt(lInt):
    try:
        return int(lInt)
    except Exception as e:
        return None
#endregion

#region file
def bFileExist(filePath):
    return os.path.exists(filePath)

def write(filePath, sToWrite):
    if not bFileExist(filePath):
        with open(filePath, 'w', encoding=ENCODING) as fw:
            fw.write(sToWrite)
    
def read(filePath):
    if bFileExist(filePath):
        with open(filePath, 'r', encoding=ENCODING) as fr:
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
def dicRead(filePath, delimiter=" ", bIsIntKey = False):
     if bFileExist(filePath):
        with open(filePath, 'r', encoding=ENCODING) as fr:
            dicRet = {}
            for line in fr.readlines():
                lstTuple = line.split(delimiter)
                if len(lstTuple) == 2:
                    key = lstTuple[0]
                    if bIsIntKey:
                        key = tryInt(key)
                        if key is None:
                            print("Not possible to cast this key to int:", lstTuple[0])
                            continue
                    dicRet[key] = lstTuple[1].strip()
            return dicRet

def dicWrite(filePath, dicToWrite, delimiter=" "):
    with open(filePath, "w", encoding=ENCODING) as f:        
       for k, v in dicToWrite.items():
           f.write(k + delimiter + v + "\n")
