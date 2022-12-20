
import requests

FAKE_AGENT = True

if FAKE_AGENT:
    try:
        # from fake_useragent import UserAgent
        # print("IMPORTE USERAGENT!!!!!!!!!")
        # print({"User-Agent" : UserAgent().random})        
        from fake_useragent import UserAgent
        ua = UserAgent()
    except ImportError:
        FAKE_AGENT = False
        print("Lib fake_useragent not installed.\n If you want to fake the useragent than: pip install fake_useragent")

def getFakeHeader():
    return {"User-Agent" : ua.random}        

def getHtml(sUrl):
    if not FAKE_AGENT:
        oResponse = requests.get(sUrl)
    else:
        oResponse = requests.get(sUrl, headers=getFakeHeader())
        
    return oResponse.content if oResponse.status_code == 200 else None
        
#region tests
# print(getHtml("https://ident.me"))
# print(getHtml("https://httpstat.us/403"))
#endregion
    

