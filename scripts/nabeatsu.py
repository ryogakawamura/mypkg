#!/usr/bin/env python3

import rospy
from std_msgs.msg import Int32

n = 0
word = 0

def cb(message):
    global n
    global word
    n = message.data
	
    if str(3) in str(n):
        word = 3
    else:
        word = 0

rospy.init_node('nabe')
sub = rospy.Subscriber('count_up', Int32, cb)
pub = rospy.Publisher('nabeatsu', Int32, queue_size=1)
rate = rospy.Rate(7)
while not rospy.is_shutdown():
    pub.publish(word)
    rate.sleep()
