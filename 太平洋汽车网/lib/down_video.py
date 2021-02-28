import requests
import json
import time
import sys
import pymysql
import os
import datetime
import configparser
import _thread
import random
import threading
import urllib.parse
import base64
filex='./mp4_'+str(int(time.time()))
os.mkdir(filex)
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

def download_img(img_url,file):
    r = requests.get(img_url, stream=True)
    print(r.status_code) # 返回状态码
    if r.status_code == 200:
        open(filex+"/"+str(file)+".MP4", 'wb').write(r.content) # 将内容写入图片
        print (img_url,"完成")
    del r


def down_in(vid,nam):
    pdata = {
        "vid": str(vid)
    }
    head= {
        "authorization":""
    }
    #https://www.dongchedi.com/motor/info/ugc/video/token/
    url = 'https://www.dongchedi.com/motor/info/ugc/video/token/'
    data = POSTx(url=url,head="",data=pdata,pro=0)
    jsda = json.loads(data)
    #data.bussiness_token
    head['authorization'] = jsda['data']['auth_token']
    url2 = 'https://vas.snssdk.com/video/openapi/v1/?action=GetPlayInfo&video_id='+pdata['vid']+'&nobase64=false&vfrom=xgplayer&ptoken='+jsda['data']['bussiness_token']
    data = GETx(url=url2,head=head,pro=0)
    gjsd = json.loads(data)
    basedata = gjsd['data']['video_list']['video_1']['main_url']
    mp4file = base64.b64decode(basedata)
    download_img(img_url=mp4file,file=nam)