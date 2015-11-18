#-*- coding:utf8 -*-
#coding=utf-8
from database import *
from filetool import *
from datafliter import *

data = DB()
tool = Filetool('gps.txt')
datafilter = DataFilter()
sql = "select pos_latitude,pos_longitude from gps_7days where" \
      " to_days(local_time)-to_days('2013-01-01') <=1 ;"
pos = {}
pos = datafilter.dataCollect(data.DBget(sql))#数据采集
datafilter.dataFilter() #数据过滤

tool.write(pos)