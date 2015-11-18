#-*- coding:utf8 -*-
#coding=utf-8
import MySQLdb

class DB():
    "连接数据库操作"
    def __init__(self,sql):
        self.conn = MySQLdb.connect(host = 'localhost',user = 'root',passwd = '123456',
                                   port = 3306,db = 'gpsdata') # gpsdata数据库专用
        self.cur = self.conn.cursor()       #构建cursor对象
        self.cur.execute(sql)           #执行单条语句
        self.next = True

    def DBget(self):
        try:
            result = self.cur.fetchone()                        #获取对象
            if result != None:
                self.next = True
            else:
                self.next = False
            return result
        except MySQLdb.Error,e:
            print 'Mysql error %d : %s' %(e.args[0],e.args[1])



    def select_db(self,db):                                 #数据库切换
        self.conn = self.conn.select_db(db)


    def closeDB(self):
            self.cur.close()                                     #关闭cur对象
            self.conn.close()                               #关闭数据库连接
