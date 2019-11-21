#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from std_msgs.msg import Float32 
from kobuki_msgs.msg import BumperEvent, Sound


   

class Collision:
    """ A ros collision node
    """

    def __init__(self):
        self.configure_ros()

    def configure_ros(self):
        """Configure all Ros content
        """
        rospy.init_node('collision_warning', anonymous=True)
        self.soundPub = rospy.Publisher('/mobile_base/commands/sound', Sound, queue_size=1)
        rospy.Subscriber('/mobile_base/events/bumper', BumperEvent , self.bumperCallback)
    
    def bumperCallback(self,data):
        """ Emit sound when bumper hold
        param
            - data: BumperEvent representing the bumper state
        """
        if data.state == 1 :
            rospy.loginfo("Bumper enfonce") 
            self.soundPub.publish(0)        

if __name__== '__main__':
    c=Collision()
    rospy.spin()