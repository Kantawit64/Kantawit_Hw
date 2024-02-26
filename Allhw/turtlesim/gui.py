#!/usr/bin/env python3
from tkinter import*
import rospy
from geometry_msgs.msg import Twist
from std_srvs.srv import Empty  # Import the service message type


frame = Tk()
frame.title("REMOTE")
frame.geometry("300x200")

rospy.init_node("GUI_Remote")
pub = rospy.Publisher("turtle1/cmd_vel",Twist, queue_size=10)

def fw():
    print("fw")
    cmd = Twist()
    cmd.linear.x = 1.0
    cmd.angular.z=0.0
    pub.publish(cmd)
def bw():
    print("bw")
    cmd = Twist()
    cmd.linear.x = -1.0
    cmd.angular.z=0.0
    pub.publish(cmd)
def lt():
    print("lt")
    cmd = Twist()
    cmd.linear.y = 1.0
    cmd.angular.z= 0.0
    pub.publish(cmd)
def rt():
    print("rt")
    cmd = Twist()
    cmd.linear.y = -1.0
    cmd.angular.z= 0.0
    pub.publish(cmd)

def rol():
    print("rol")
    cmd = Twist()
    cmd.linear.y = 0.0
    cmd.angular.z= 1.0
    pub.publish(cmd)

def ror():
    print("ror")
    cmd = Twist()
    cmd.linear.y = 0.0
    cmd.angular.z= -1.0
    pub.publish(cmd)

def reset_BT():
    print("reset")
    try:
        rospy.wait_for_service('/reset')
        reset_service = rospy.ServiceProxy('/reset', Empty)
        response = reset_service()
        if response:
            rospy.loginfo("Turtlesim reset successful")
        else:
            rospy.logwarn("Turtlesim reset failed")
    except rospy.ServiceException as e:
        rospy.logerr("Service call failed: %s" % e)


B1 = Button(text = "FW", command=fw)
B1.place(x=73, y=20)

B2 = Button(text = "BW", command=bw)
B2.place(x=73, y=130)

B3 = Button(text = "LT", command=lt)
B3.place(x=20, y=80)

B4 = Button(text = "RT", command=rt)
B4.place(x=128, y=80)

B5 = Button(text = "ROL", command=rol)
B5.place(x=200, y=20)

B6= Button(text = "ROR", command=ror)
B6.place(x=200, y=80)

B7= Button(text = "RST", command=reset_BT)
B7.place(x=200, y=150)

frame.mainloop()