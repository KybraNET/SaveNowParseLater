
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
    try:                                        
        return requests.get(sUrl) if not FAKE_AGENT else requests.get(sUrl, headers=getFakeHeader())
    except Exception as e:
        return e
#region tests
# print(getHtml("https://ident.me"))
# print(getHtml("https://httpstat.us/403"))
#endregion
    

