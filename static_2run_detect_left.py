#! /usr/bin/env python

import rospy
from sensor_msgs.msg import LaserScan
from std_msgs.msg import Int32

def callback(msg):

  #If the distance to an obstacle in front of the robot is bigger than 2 meter, the robot will print no obstacle


  for i in range(185,190):
      if msg.ranges[i] > 2:
          obstacle=0
      else:
          obstacle=1
          break





  pub.publish(obstacle)


rospy.init_node('detect')
sub = rospy.Subscriber('/lidar2D', LaserScan, callback) #We subscribe to the laser's topic
pub = rospy.Publisher('check_object_2',Int32, queue_size=2)

#while not rospy.is_shutdown():
   # pub.publish(obstacle)

rospy.spin()   
