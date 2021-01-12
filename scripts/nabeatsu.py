#!/usr/bin/env python3

import rospy
from std_msgs.msg import String import Int32

def cb(message):
	global n
	n = message.data
	
	if 3 in n:
		word = 'San!!!!'
	else:
		word = '......'

rospy.init_node('nabe')
sub = rospy.Subscriber('count_up', String, cb)
pub = rospy.Publisher('nabeatsu', String, queue_size=1)
rate = rospy.Rate(1)
while not rospy.is_shutdown():
	pub.publish(word)
	rate.sleep()
