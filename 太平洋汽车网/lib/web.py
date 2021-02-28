#-*-coding:utf8-*-
import requests
requests.packages.urllib3.disable_warnings() #抑制ssl错误
def GETx(url,head,pro):
    
    if pro!=0:
        proxies = {'http': 'http://localhost:'+pro, 'https':'http://localhost:'+pro}
        httpdata = requests.get(url,headers=head,verify=False,proxies=proxies)
    else:
        httpdata = requests.get(url,headers=head,verify=False)
    return httpdata.text

def POSTx(url,head,data,pro):
    
    if pro!=0:
        proxies = {'http': 'http://localhost:'+pro, 'https':'http://localhost:'+pro}
        httpdata = requests.post(url,headers=head,data=data,verify=False,proxies=proxies)
    else:
        httpdata = requests.post(url,headers=head,data=data,verify=False)
    return httpdata.text