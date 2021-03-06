#!/usr/bin/env python
#-*-coding:utf-8 -*-

# 
#  Слушатель x10_mediaplayer
#  
#  и запуск медиапроигрывателя
#  
#


import roslib; roslib.load_manifest('vp_x10_voice')
import rospy
import subprocess
import shlex

from std_msgs.msg import String

PATH_RINGTONS="ros_pkgs/vp_x10_voice/nodes/ringtons/"

def controller(data):

    rington_file = data.data
    command1='smplayer "'
    command1+=PATH_RINGTONS+rington_file+'"'
    subprocess.Popen(command1,shell=True).communicate()
    rospy.loginfo(command1)
    

      
def listener():
   rospy.init_node('node_x10_alarm_mediaplayer')
   sub = rospy.Subscriber("x10_alarm_mediaplayer",String,controller)
   rospy.spin()
 
if __name__ == '__main__':
   listener()
   
