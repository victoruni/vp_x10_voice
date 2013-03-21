#!/usr/bin/env python
#-*-coding:utf-8 -*-

# 
#  Слушатель x10_festival
#  
#  и произношение голосом
#  
#


import roslib; roslib.load_manifest('vp_x10_voice')
import rospy
import subprocess
import shlex

from std_msgs.msg import String



def controller(data):

    fraza = data.data
    #command1="festival -b '(begin (SayText "
    #command1+='"'+fraza+'"'
    #command1+="))'"
    command1='echo "'
    command1+=fraza+'"'
    command1+=" | festival --language russian --tts"
    subprocess.Popen(command1,shell=True).communicate()
    rospy.loginfo(command1)

      
def listener():
   rospy.init_node('node_x10_alarm_festival')
   sub = rospy.Subscriber("x10_alarm_festival",String,controller)
   rospy.spin()
 
if __name__ == '__main__':
   listener()
   
