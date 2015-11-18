#-*- coding:utf8 -*-
#coding=utf-8
pos_longitude = dict(zip([round(112.09 + (y*(0.23/100.0)),4)  for y in range(0,100)]
                                   ,[x for x in range(1,101)]))
pos_latitude = dict(zip([round(28.09 + x*(0.18/100.0),4)  for x in range(0,100)]
                                   ,[y for y in range(1,101)]))

for i in sorted(pos_longitude.keys()):
    print i,pos_longitude[i]

for i in sorted(pos_latitude.keys()):
    print i,pos_latitude[i]

tempx = int((112.0911-112.09)*10000/23)+1
print tempx


tempy = int((28.0955-28.09)*10000/18)+1
print tempy