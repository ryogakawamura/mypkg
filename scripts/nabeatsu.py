#!/usr/bin/env python3

import rospy
from std_msgs.msg import Int32

n = 0

def cb(message):
	global n
	n = message.data*3

rospy.init_node('nabe')
sub = rospy.Subscriber('count_up', Int32, cb)
pub = rospy.Publisher('nabeatsu', Int32, queue_size=1)
rate = rospy.Rate(100)
while not rospy.is_shutdown():
	pub.publish(n)
	rate.sleep()
