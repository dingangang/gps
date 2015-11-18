#-*- coding:utf8 -*-
#coding=utf-8
import MySQLdb

class DB():
    "连接数据库操作"
    def __init__(self):
        self.conn = MySQLdb.connect(host = 'localhost',user = 'root',passwd = '123456',
                                   port = 3306,db = 'gpsdata') # gpsdata数据库专用

    def DBget(self,sql):
        try:
            cur = self.conn.cursor()                        #构建cursor对象
            cur.execute(sql)                                #执行单条语句
            result = cur.fetchall()                        #获取对象
            return result
        except MySQLdb.Error,e:
            print 'Mysql error %d : %s' %(e.args[0],e.args[1])
        finally:
            cur.close()                                     #关闭cur对象
            self.conn.close()                               #关闭数据库连接

    def select_db(self,db):                                 #数据库切换
        self.conn = self.conn.select_db(db)
