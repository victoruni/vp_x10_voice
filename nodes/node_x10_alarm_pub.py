#!/usr/bin/env python
#-*-coding:utf-8 -*-

# 
#  Ожидание событий будильника
#  
#  и отправка команд в темы для
#  x10, festival(голос), медиаплейер(музыка)
#

import roslib; roslib.load_manifest('vp_x10_voice')
import rospy
import subprocess
import shlex
import time
from datetime import datetime, timedelta

from std_msgs.msg import String
from std_msgs.msg import Int16


alarm_events=[
   ["10:30",3,4,[0,1,2,3,4,5,6],{1:"rington13.mp3;29",2:"Белочка приём лекарства"}],
   ["06:25",2,5,[0,1,2,3,4,5,6],{1:"rington2.mp3;23",2:"Надо прогулять Графа "}],
   ["06:15",3,4,[0,1,2,3,4,5,6],{1:"rington6.mp3;17",2:"Подъём  пора на работу, вставай Виктор Александрович ",4:"12"}],
   ["9:00",50,30,[0,1,2,3,4,5,6],{1:"rington6.mp3;19",3:"Время "}],
   ["18:30",2,5,[0,1,2,3,4,5,6],{1:"rington2.mp3;23",2:"Надо прогулять Графа "}],
   ["23:00",2,5,[0,1,2,3,4,5,6],{1:"rington2.mp3;23",2:"Надо прогулять Графа "}],
   ];
name_hours=[
           [{1,21},"час"],
           [{2,3,4,22,23},"часа"],
           [{5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20},"часов"],
          ]
name_minutes=[
           [{1,21,31,41,51},"минута"],
           [{2,3,4,22,23,24,32,33,34,42,43,44,52,53,54},"минуты"],
           [{5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,25,26,27,28,29,30,35,36,37,38,39,40,45,46,47,48,49,50,55,56,57,58,59},"минут"],
          ]


def my_alarm():
    pub1 = rospy.Publisher('x10_alarm_mediaplayer',String)
    pub2 = rospy.Publisher('x10_alarm_festival', String)
    rospy.init_node('node_x10_alarm_events')

    d=datetime.today()        
    dh=d.hour;dm=d.minute;
    while not rospy.is_shutdown():
      d=datetime.today()
      if(d.hour!=dh or d.minute!=dm):
        for element in alarm_events:
          for dt in range(element[1]):  # кол-во повторений element[1]
            alarm_time=element[0]
            dminutes=dt*element[2]      # промежуток повторения 
            dd=timedelta(minutes=dminutes)
            d1=d-dd
            if(d.hour<10):
               this_time="0"+str(d.hour)
            else:
               this_time=str(d.hour)
            if(d.minute<10):
               this_time+=":0"+str(d.minute)
            else:
               this_time+=":"+str(d.minute)
            #this_time=str(d.hour)+":"+str(d.minute)
            cor_this_time=str(d1.hour)+":"+str(d1.minute)
            #rospy.loginfo(this_time)
            try:
              element[3].index(d.weekday()) 
              if (alarm_time==cor_this_time):
                rospy.loginfo("!!!!!!!!!!!!==="+alarm_time+"---"+this_time)
                for key in element[4]:
                   if key==1:
                     rington_file=element[4][key].split(";")[0];
                     pub1.publish(rington_file)
                     time.sleep(int(element[4][key].split(";")[1]))
                     rospy.loginfo("program 1 ")
                   elif key==2:
                     pub2.publish(element[4][key])
                     time.sleep(5)
                     rospy.loginfo("program 2 ")
                   elif key==3:
                     for ho in name_hours:
                       if d.hour in ho[0]:
                         strtime1= str(d.hour)+" "+ho[1]
                         break
                     if d.minute>0:
                       for mi in name_minutes:
                         if d.minute in mi[0]:
                            strtime2=" "+str(d.minute)+" "+mi[1]
                            break
                     strtime2=strtime2.replace("01","одна")
                     strtime2=strtime2.replace("21","двадцать одна")
                     strtime2=strtime2.replace("31","тридцать одна")
                     strtime2=strtime2.replace("41","сорок одна")
                     strtime2=strtime2.replace("51","пятьдесят одна")
                     strtime2=strtime2.replace("02","две")
                     strtime2=strtime2.replace("22","двадцать две")
                     strtime2=strtime2.replace("32","тридцать две")
                     strtime2=strtime2.replace("42","сорок две")
                     strtime2=strtime2.replace("52","пятьдесят две")
                     pub2.publish(element[4][key]+strtime1+strtime2)
                     time.sleep(5)
                     rospy.loginfo("program 3 ")
                   elif key==4:
                     pub4.publish(int(element[4][key]))
                     time.sleep(1)
                     rospy.loginfo("program 4 ")
                   else:
                     pass
            except ValueError:
              pass
        dh=d.hour;dm=d.minute;
      else:
        time.sleep(10)
              
      
if __name__ == '__main__':
    try:
        my_alarm()
    except rospy.ROSInterruptException: pass

