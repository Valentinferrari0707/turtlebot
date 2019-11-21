#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from std_msgs.msg import Float32 
from sensor_msgs.msg import LaserScan
from kobuki_msgs.msg import  Sound




class MinDistFeedback:
    """ A ros collision node
    """

    def __init__(self):
        self.configure_ros()

    def configure_ros(self):
        """Configure all Ros content
        """
        self.distance_min=0
        
        rospy.init_node('min_dist_feedback', anonymous=True)
        self.soundPub = rospy.Publisher('/mobile_base/commands/sound', Sound, queue_size=1)
        rospy.Subscriber('/min_dist', Float32 , self.feedbackCallback)
    
    def feedbackCallback(self,data):
        """ Grab minimal distance
        """
        print(data)
        # if data < 1:
        # self.soundPub.publish(0)


if __name__== '__main__':
    f=MinDistFeedback()
    rospy.spin()