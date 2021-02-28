#-*-coding:utf8-*-
from bs4 import BeautifulSoup
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
import urllib
import base64
import lib.web
import lib.run_sql
import lib.configw
import lib.dbx

wdg = lib.configw.text_g_d("534")
dbx = lib.dbx.dbs
btime = int(time.time())
lx = "雷凌"

def getHtml(url):
    response = urllib.urlopen(url)
    html = response.read()
    return html 

def urlcode(urld):
    urld = str(urllib.parse.urlencode(urld))
    urld = urld.replace("+", "")
    urld = urld.replace("/", '%2f')
    return urld


def scount(wmpoiid):
    conn = pymysql.connect(host=dbx['localhost'],port=dbx['port'],user=dbx['user'],password=dbx['pass'],database=dbx['db'],charset="utf8mb4") #链接数据库
    cursor = conn.cursor()#创建数据库游标
    sql = "SELECT * FROM `dcd`.`txt` where wmpoiid = '"+str(wmpoiid)+"'"
    cursor.execute(sql)
    results = cursor.fetchall()
    conn.commit()#执行sql
    cursor.close()#关闭mysql
    return len(results)

#data[0].unique_id
#data[0].info.video_duration

def str_r(stra):
    tempr = str(stra)
    tempr = tempr.replace("'", " ")
    tempr = tempr.replace("（", " ")
    tempr = tempr.replace("）", " ")
    tempr = tempr.replace("\\", " ")
    tempr = tempr.replace("*", " ")
    tempr = tempr.replace("|", " ")
    tempr = tempr.replace("/", " ")
    tempr = tempr.replace("-", " ")
    tempr = tempr.replace(";", " ")
    return str(tempr)
#data[0].info.abstract_content
#data[0].info.title
#data[0].info.behot_time
rtime = btime
while True:
    rtime -= 3500
    wdg['max_behot_time'] = str(rtime)
    urlw = 'https://www.dongchedi.com/motor/stream_entrance/get_feed/v47/?'
    urlw += urlcode(wdg)
    data = lib.web.GETx(url=urlw,head="",pro=0)
    jdata = json.loads(data)
    ldata = jdata['data']
    for xkey in ldata:
        rtix =  xkey['info']['behot_time']
        if int(rtix)+604800 < btime:
            print("检测到文章大于7天，自动结束.")
            exit()
        unique_id = xkey['unique_id']
        if scount(unique_id) >0:
            print("发现重复文章.[跳过]",unique_id)
            continue
        if xkey['info'].get('source') == None:
            print("属于私人文章不予收录.[跳过]")
            continue
        video_duration = xkey['info']['video_duration']
        title = xkey['info']['title']
        if int(video_duration) != 0:
            print("该链接为纯视频.[跳过]")
            continue
        
        abstract_content = xkey['info']['abstract_content']
        urlt = 'https://www.dongchedi.com/article/'+str(unique_id)

        
        response = urllib.request.urlopen(urlt)
        html = response.read()
        clean = BeautifulSoup(html).get_text()
        
        ytix = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(rtix))
        print(title,ytix)
        sql = "INSERT INTO `dcd`.`txt` (`abstract_content`, `url`, `title`, `text`, `lx`, `wmpoiid`, `time`) VALUES ('"+str_r(abstract_content)+"', '"+urlt+"', '"+str_r(title)+"', '"+str_r(clean)+"', '"+lx+"', '"+str(unique_id)+"', '"+str(ytix)+"')"
        
        lib.run_sql.runsql(sql)
        
        
        
 






