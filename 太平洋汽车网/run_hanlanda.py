#-*-coding:utf8-*-
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
import lib.web
import lib.down
import lib.run_sql

filex='./img_'+'hanlanda_'+str(int(time.time()))
lx = "汉兰达"
os.mkdir(filex)
url = 'https://www.dongchedi.com/motor/car_page/v3/get_picture/?version_code=445&category=wg&series_id=536&offset=0&car_id=null'
data = lib.web.GETx(url=url,head="",pro=0)
jsond = json.loads(data)
#data.list[1].info.car_name
#data.list[1].info.toutiaourl
#data.paging.total_count
total_count = jsond['data']['paging']['total_count']#总数量
offset = 0
while offset+30<total_count:
    url = 'https://www.dongchedi.com/motor/car_page/v3/get_picture/?version_code=445&category=wg&series_id=536&offset='+str(offset)+'&car_id=null'
    offset += 30
    data = lib.web.GETx(url=url,head="",pro=0)
    jsond = json.loads(data)
    data_list = jsond['data']['list']
    for key in data_list:
        if key.get('info') != None:
            if key['info'].get('car_name') != None:
                ret = str(time.time())+"_"+str(random.randint(3,7))

                car_name = key['info']['car_name']+ret
                toutiaourl = key['info']['toutiaourl']
                lib.down.download_img(img_url=toutiaourl,file=car_name)
                sql = "INSERT INTO `dcd`.`img` (`url`, `file`, `name`,`lx`) VALUES ('"+toutiaourl+"', './img/"+car_name+".jpg', '"+car_name+"', '"+lx+"')"
                lib.run_sql.runsql(sql)


