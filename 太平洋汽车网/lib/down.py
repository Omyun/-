import requests
import time
import os
filex='./img_'+'leiling'+str(int(time.time()))
os.mkdir(filex)
def download_img(img_url,file):
    r = requests.get(img_url, stream=True)
    print(r.status_code) # 返回状态码
    if r.status_code == 200:
        open(filex+"/"+str(file)+".jpg", 'wb').write(r.content) # 将内容写入图片
        print (img_url,"完成")
    del r