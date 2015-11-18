#-*- coding:utf8 -*-
#coding=utf-8
class Filetool():
    "数据的写入"
    def __init__(self,txt):
        self.f = open(txt,'w+')

    def write(self,datas):                              #写入数据
        try:
            data = ''
            if type(datas) == type((1,)):               #tuple写入
                for d in datas:
                    data += str(d)+' '
                self.f.write(data+'\n')
            elif type(datas)==type({}):                 #dict写入
                for d in datas.keys():
                    data += str(d)+' '+str(datas[d])+'\n'
                self.f.write(data+'\n')
            else:
                datas = str(datas)
                self.f.write(datas+'\n')
        except IOError as err:
            print('File Error:'+str(err))
