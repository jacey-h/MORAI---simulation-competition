#! /usr/bin/env python

import rospy
from std_msgs.msg import Int32

rospy.init_node('timer')

pub = rospy.Publisher('timer',Int32,queue_size=2)
rate = rospy.Rate(10)

count = 0
while not rospy.is_shutdown():
    pub.publish(count)
    count += 1
    rate.sleep()
