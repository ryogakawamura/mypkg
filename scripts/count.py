#!/usr/bin/env python3

# SPDX-LICENSE-Identifer: BSD-2-Clause
# Copyright (C) 2020 Ryuichi Ueda. All rights reserved.

import rospy
from std_msgs.msg import Int32

rospy.init_node('count')
pub = rospy.Publisher('count_up', Int32, queue_size=1)
rate = rospy.Rate(10)
n = 0
while not rospy.is_shutdown():
    n += 1
    pub.publish(n)
    rate.sleep()
