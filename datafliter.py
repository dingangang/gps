class DataFilter():
    "数据采集和过滤"
    def __init__(self):
        self.pos = {}

    def dataCollect(self,data):
        for i in data:
            if not self.pos.has_key(i):
                self.pos[i] = 1
            else:
                self.pos[i] += 1
        return self.pos
                
    def dataFilter(self):
        for i  in self.pos.keys():
            if self.pos[i] == 1:
                del self.pos[i]
        return self.pos


