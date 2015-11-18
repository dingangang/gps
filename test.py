from database import *
from gpsTime_Location import *

# f = open('v_id.txt','w+')
# sql = 'select distinct vehicle_id from gps_temp '
# db = DB(sql)
# while db.next:
#     for i in db.DBget():
#         if i == None:
#             continue
#         else:
#             f.write(str(i)+'\n')



gps = gpsTime_Location()
f = open('v_id.txt','r')
for i in f.readlines():

    sql = 'select pos_longitude,pos_latitude,local_time,move_speed,vehicle_id from gps_temp ' \
          'where vehicle_id = %s'% i

    db = DB(sql)
    while db.next:
        gps.loop_location(db.DBget())
    gps.write_into_file(i.strip('\n'))
    db.closeDB()


