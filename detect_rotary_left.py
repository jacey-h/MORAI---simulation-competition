#! /usr/bin/env python

import rospy
from sensor_msgs.msg import LaserScan
from std_msgs.msg import Int32

def callback(msg):


  for i in range(130,180):
      if msg.ranges[i] > 1.4:
          obstacle=0
      else:
          obstacle=1
          break

  pub.publish(obstacle)


rospy.init_node('detect')
sub = rospy.Subscriber('/lidar2D', LaserScan, callback) #We subscribe to the laser's topic
pub = rospy.Publisher('check_rotary_left',Int32, queue_size=2)

#while not rospy.is_shutdown():
   # pub.publish(obstacle)

rospy.spin()   
