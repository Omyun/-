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
import base64
import lib.web
import lib.run_sql
import lib.down_video
import lib.configw
wdg = lib.configw.video_g_d("534")
btime = int(time.time())
wdg['max_behot_time'] = str(btime)

lx = "雷凌"
def urlcode(urld):
    urld = str(urllib.parse.urlencode(urld))
    urld = urld.replace("+", "")
    urld = urld.replace("/", '%2f')
    return urld

#data[0].info.display_time
#data[0].info.video_id
#data[0].info.abstract_content
#data[0].info.title 


while True:
    urlw = "https://www.dongchedi.com/motor/stream_entrance/get_feed/v47/?"
    urlw += urlcode(wdg)
    dw = lib.web.GETx(url=urlw,head="",pro=0)
    dwj = json.loads(dw)
    dwjdata = dwj['data']
    for dwjkey in dwjdata:
        if int(dwjkey['info']['display_time'])+604800 > btime:
            infoid = str(dwjkey['info']['video_id'])
            title = str(dwjkey['info']['title'])
            abstract_content = str(dwjkey['info']['abstract_content'])
            nam = lx+str(int(dwjkey['info']['display_time']))
            lib.down_video.down_in(vid=infoid,nam=nam)
            sql = "INSERT INTO `dcd`.`mp4` (`mp`,`abstract_content`, `lx`, `title`) VALUES ('"+nam+"',  '"+abstract_content+"', '"+lx+"', '"+title+"')"
            lib.run_sql.runsql(sql)
        else:
            print("已经大于7天自动退出.")
            exit()
    wdg['max_behot_time'] = str(int(wdg['max_behot_time'])+3500)

    






