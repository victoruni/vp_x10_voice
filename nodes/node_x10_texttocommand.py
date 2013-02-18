#!/usr/bin/env python
#-*-coding:utf-8 -*-

# 
#  Слушатель x10_voicetotext
#  
#  и отправка команд и установка параметров
#  для управления ardrone 2.0
#


import roslib; roslib.load_manifest('vp_x10_voice')
import rospy
import subprocess
import shlex

from vp_x10_voice.msg import X10
from std_msgs.msg import String
from std_msgs.msg import Int16
from std_msgs.msg import Empty


HOUSE_A=6       #B00110

UNIT_1=12	#B01100
UNIT_2=28	#B11100
UNIT_3=4	#B00100
UNIT_4=20	#B10100
UNIT_5=2	#B00010
UNIT_6=18	#B10010
UNIT_7=10	#B01010
UNIT_8=26	#B11010
UNIT_9=14	#B01110
UNIT_10=30	#B11110
UNIT_11=6	#B00110
UNIT_12=22	#B10110
UNIT_13=0	#B00000
UNIT_14=16	#B10000
UNIT_15=8	#B01000
UNIT_16=24	#B11000

ALL_UNITS_OFF=1	#B00001
ALL_LIGHTS_ON=3	#B00011
ON=5			#B00101
OFF=7			#B00111
DIM=9			#B01001
BRIGHT=11		#B01011
ALL_LIGHTS_OFF=13	#B01101


arr_commands=[[[HOUSE_A,UNIT_5,1],[HOUSE_A,OFF,1]],        #люстра выключить
              [[HOUSE_A,UNIT_6,1],[HOUSE_A,OFF,1]],        #лента выключить
              [[HOUSE_A,UNIT_4,1],[HOUSE_A,OFF,1]],        #лампа выключить
              [[HOUSE_A,UNIT_2,1],[HOUSE_A,OFF,1]],        #ночник выключить
              [[HOUSE_A,UNIT_6,1],[HOUSE_A,OFF,1]],        #гирлянда выключить
              [[HOUSE_A,UNIT_5,1],[HOUSE_A,ON,1]],        #люстра включить
              [[HOUSE_A,UNIT_6,1],[HOUSE_A,ON,1]],        #лента включить
              [[HOUSE_A,UNIT_4,1],[HOUSE_A,ON,1]],        #лампа включить
              [[HOUSE_A,UNIT_2,1],[HOUSE_A,ON,1]],        #ночник включить
              [[HOUSE_A,UNIT_6,1],[HOUSE_A,ON,1]],        #гирлянда включить
              [[HOUSE_A,UNIT_5,1],[HOUSE_A,OFF,1],[HOUSE_A,UNIT_6,1],[HOUSE_A,ON,1],[HOUSE_A,UNIT_4,1],[HOUSE_A,OFF,1],[HOUSE_A,UNIT_2,1],[HOUSE_A,OFF,1],[HOUSE_A,UNIT_6,1],[HOUSE_A,OFF,1]],        #отбой
              [[HOUSE_A,UNIT_5,1],[HOUSE_A,OFF,1],[HOUSE_A,UNIT_6,1],[HOUSE_A,ON,1],[HOUSE_A,UNIT_4,1],[HOUSE_A,OFF,1],[HOUSE_A,UNIT_2,1],[HOUSE_A,ON,1],[HOUSE_A,UNIT_6,1],[HOUSE_A,OFF,1]],        #программа 1
              [[HOUSE_A,UNIT_5,1],[HOUSE_A,OFF,1],[HOUSE_A,UNIT_6,1],[HOUSE_A,OFF,1],[HOUSE_A,UNIT_4,1],[HOUSE_A,ON,1],[HOUSE_A,UNIT_2,1],[HOUSE_A,OFF,1],[HOUSE_A,UNIT_6,1],[HOUSE_A,OFF,1]],        #программа 2
              [[HOUSE_A,ALL_LIGHTS_OFF,1]],        #программа 3
              [[HOUSE_A,ALL_LIGHTS_OFF,1]],        #программа 4
              [[HOUSE_A,ALL_LIGHTS_OFF,1]]         #программа 5
              ]

def controller(data):

    index = data.data
    data1=X10()
    for ind,elements in enumerate(arr_commands[index-1]):
          data1.command1=elements[0]
          data1.command2=elements[1]
          data1.repeatTime=elements[2]
          pub1 = rospy.Publisher('data_to_x10', X10)
          pub1.publish(data1)
          rospy.loginfo(data1)
    #data1.command1=arr_commands[index-1][0][0]
    #data1.command2=arr_commands[index-1][0][1]
    #data1.repeatTime=arr_commands[index-1][0][2]
    #pub1 = rospy.Publisher('x10_texttocommand', X10)
    #pub1.publish(data1)
    
    # лог
    #rospy.loginfo(data1)
    # публиковать в тему ardrone1_move
    #pub1=rospy.Publisher('data_to_x10', X10)
    #pub1.publish(data1) 
    #rospy.loginfo(str)


      
def listener():
   rospy.init_node('node_x10_texttocommand')
   sub = rospy.Subscriber("x10_voicetotext",Int16,controller)
   rospy.spin()
 
if __name__ == '__main__':
   listener()
   
