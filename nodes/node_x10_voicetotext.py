#!/usr/bin/env python
#-*-coding:utf-8 -*-
import roslib; roslib.load_manifest('vp_x10_voice')
import rospy
import subprocess
import shlex

from std_msgs.msg import String
from std_msgs.msg import Int16

fraza=["люстра","лента","лампа","ночник","елка",
       "люстра включить","лента гори","лампа включить","ночник включить","елка гори",
       "отбой",
       "программа 1","программа 2","программа 3","программа 4","программа 5"]

matrix = [["люстра","быстро"],
          ["лента"],
          ["лампа","лапа"],
          ["ночник","начни"],
          ["елка","елочка"],
          ["люстра включить","люстра ключи","быстро включить"],
          ["лента гори","mp3"],
          ["лампа включить","лампа включи","лампа ключи"],
          ["ночник ключи","ночник включить","ночник включи","ночник горит","ночник гори"],
          ["елка гори","елочка гори","елка горит"],
          ["отбой","всем спать","я спать"],
          ["программа 1","драма 1"],
          ["программа 2","драма 2"],
          ["программа 3","драма 3","программа тв"],
          ["программа 4","драма 4"],
          ["программа 5","драма 5"]]


def talker():
    pub = rospy.Publisher('x10_voicetotext', Int16)
    rospy.init_node('node_x10_voicetotext')

    while not rospy.is_shutdown():
      rospy.loginfo("ожидание записи с микрофона")
      subprocess.Popen('rec -q -c 1 -r 16000 current.wav silence 1 0.2 3% 1 0.2 3%',shell=True,cwd = '/home/petin/ros_pkgs/vp_x10_voice/nodes/').communicate()      
      rospy.loginfo("wav - ok") 
      subprocess.Popen('flac -f -s current.wav -o current.flac',shell=True,cwd = '/home/petin/ros_pkgs/vp_x10_voice/nodes/').communicate()
      rospy.loginfo("flac - ok") 
      proc3=subprocess.Popen('php textfromgoogle.php',shell=True, stdout =   subprocess.PIPE,cwd = '/home/petin/ros_pkgs/vp_x10_voice/nodes/') 
      result=proc3.communicate()[0]
      str1 = "result api google = %s"%result
      rospy.loginfo(str1)
      str2=""
      index=0
      for ind,elements in enumerate(matrix):
        for element in elements:
          if result.count(element)>0:
            str2=fraza[ind]
            index=ind+1
      if(index>0):      
        pub.publish(index)
        rospy.loginfo(str2)
      
if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException: pass

