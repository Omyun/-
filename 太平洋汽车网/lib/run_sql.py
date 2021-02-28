
import pymysql
dbs ={
    "localhost":"127.0.0.1",
    "port":3306,
    "db":"dcd",
    "user":"root",
    "pass":"root",
}
def runsql(sqlx):
    conn = pymysql.connect(host=dbs['localhost'],port=dbs['port'],user=dbs['user'],password=dbs['pass'],database=dbs['db'],charset="utf8") #链接数据库
    cursor = conn.cursor()#创建数据库游标
    cursor.execute(sqlx)#载入sql
    conn.commit()#执行sql
    cursor.close()#关闭mysql