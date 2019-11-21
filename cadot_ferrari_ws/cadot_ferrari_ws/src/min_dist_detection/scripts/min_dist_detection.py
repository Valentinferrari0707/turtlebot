#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from std_msgs.msg import Float32 
from sensor_msgs.msg import LaserScan



class MinDistDetection:
    """ A ros collision node
    """

    def __init__(self):
        self.configure_ros()

    def configure_ros(self):
        """Configure all Ros content
        """
        self.distance_min=0
        
        rospy.init_node('min_dist_detection', anonymous=True)
        self.min_Dist = rospy.Publisher('/min_dist',Float32, queue_size=1)
        rospy.Subscriber('/scan', LaserScan , self.obstacleCallback)
    
    def obstacleCallback(self,data):
        """ Grab minimal distance
        """
        self.distance_min=data.range_min
        self.min_Dist.publish(self.distance_min)


if __name__== '__main__':
    d=MinDistDetection()
    rospy.spin()