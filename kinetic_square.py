#! /usr/bin/env python

import rospy
from sensor_msgs.msg import LaserScan
from std_msgs.msg import Int32

def callback(msg):

  #If the distance to an obstacle in front of the robot is bigger than 2 meter, the robot will print no obstacle
  obstacle = 0

  
  r = [0.12, 0.12, 0.12, 0.12, 0.12, 0.12, 0.12, 0.12, 0.12, 0.12, 0.12, 0.12, 0.12, 0.12, 0.12, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.14, 0.14, 0.14, 0.14, 0.14, 0.14, 0.14, 0.15, 0.15, 0.15, 0.15, 0.15, 0.16, 0.16, 0.16, 0.16, 0.16, 0.17, 0.17, 0.17, 0.18, 0.18, 0.18, 0.19, 0.19, 0.2, 0.2, 0.2, 0.21, 0.21, 0.22, 0.23, 0.23, 0.24, 0.25, 0.26, 0.26, 0.27, 0.28, 0.29, 0.31, 0.32, 0.33, 0.35, 0.37, 0.38, 0.41, 0.43, 0.46, 0.49, 0.52, 0.57, 0.61, 0.67, 0.74, 0.83, 0.94, 0.95, 0.95, 0.95, 0.94, 0.94, 0.94, 0.94, 0.94, 0.94, 0.94, 0.94, 0.95, 0.95, 0.95, 0.95, 0.95, 0.96, 0.96, 0.96, 0.97, 0.97, 0.97, 0.98, 0.98, 0.99, 0.99, 1.0, 1.01, 1.01, 1.02, 1.03, 1.04, 1.05, 1.05, 1.03, 0.99, 0.96, 0.93, 0.91, 0.88, 0.86, 0.84, 0.82, 0.8, 0.78, 0.76, 0.75, 0.73, 0.72, 0.7, 0.69, 0.68, 0.67, 0.65, 0.64, 0.63, 0.62, 0.62, 0.61, 0.6, 0.59, 0.58, 0.58, 0.57, 0.56, 0.56, 0.55, 0.55, 0.54, 0.54, 0.53, 0.53, 0.52, 0.52, 0.51, 0.51, 0.51, 0.5, 0.5, 0.5, 0.5, 0.49, 0.49, 0.49, 0.49, 0.48, 0.48, 0.48, 0.48, 0.48, 0.48, 0.48, 0.48, 0.48, 0.48, 0.48, 0.48]

  for j in range(90,271):
      if msg.ranges[j] > r[j-90]:
          obstacle=0
      else:
          obstacle=1
          break








  pub.publish(obstacle)


rospy.init_node('detect')
sub = rospy.Subscriber('/lidar2D', LaserScan, callback) #We subscribe to the laser's topic
pub = rospy.Publisher('check_square',Int32, queue_size=2)

#while not rospy.is_shutdown():
   # pub.publish(obstacle)

rospy.spin()   
