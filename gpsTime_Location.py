#usr/bin/python
#coding=utf-8
class gpsTime_Location():
    '用于计算网格中停留时间。。'
    def __init__(self):
        '''times用于计时间 ，xy是辅助计算的，temp用于接收变量。
            x,y的递增可以根据实际选定的区间范围来进行调整'''
        self.temp = ()
        self.times = {(x, y):0 for x in range(1, 101) for y in range(1, 101)}
        self.pos_longitude = dict(zip([round(112.09 + y*(0.23/100.0),4)  for y in range(0,100)]
                                   ,[x for x in range(1,101)]))
        self.pos_latitude = dict(zip([round(28.09 + x*(0.18/100.0),4)  for x in range(0,100)]
                                   ,[y for y in range(1,101)]))

    def loop_location(self,data):
        '''data(latitude,longitude,localtime,speed)\
        data(pos_longitude,pos_latitude,local_time,move_speed)
        每次接受一条信息，与temp进行比较并且进行计算'''
        if data:
            if self.inlocation(data):
                if self.temp == ():
                    self.temp = data
                elif data[3] == 0:
                    if self.matrix(self.temp) == self.matrix(data): #矩阵内坐标相等
                        print self.matrix(data)
                        self.write_time(self.matrix(data),
                                        self.counttime(self.temp,data)) #计算两者时间差并写入到计数字典
                        self.temp = data
                else:
                    self.temp = ()

    def standare(self,data):
        '将数据化成4位小数便于计算'
        data = round(data,4)
        if data*10000%2 == 0:
            return data
        else:
            return round(data-0.001,2)

    def inlocation(self, data):
        '判断位置是否在所限定范围内'
        temp_pos_longitude = self.standare(data[0])
        temp_pos_latitude = self.standare(data[1])
        if 112.09 <= temp_pos_longitude <= 112.32 and 28.09 <= temp_pos_latitude <= 28.27: #此处根据实际给定网格边缘定义
            return True
        else:
            return False

    def matrix(self, data):
        '得到矩阵times内的坐标'
        tempx = int((data[0]-112.09)*10000/23)+1
        tempy = int((data[1]-28.09)*10000/18)+1

        print tempx,tempy
        return (tempx,tempy)


    def counttime(self, data1, data2):
        '计算停留时间'
        return  (data2[2] - data1[2]).seconds

    def write_time(self,location,time):
        '在对应位置写入时间'
        self.times[location] += time


    def write_into_file(self,id):
        '一个ID统计完毕就进行一次写入'
        try:
            f = open('gpstime.txt','a')
            for data in self.times.keys():
                if self.times[data] != 0:
                    str1 = str(id)+','+str(data)+','+str(self.times[data])
                    f.write(str1+'\n')
            f.close()
        except IOError as err:
            print 'file err'


    def printt(self):
        print 'just a print test'
        print 'another test'


