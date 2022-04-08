#!/usr/bin/env python 
# license removed for brevity 
import rospy 
from std_msgs.msg import String,Int32

def talker():    
    rospy.init_node('talker')
    pub = rospy.Publisher('numeros', Int32, queue_size=10)

    #rate = rospy.Rate(10) # 10hz
    counter=0
    while not rospy.is_shutdown():
        numero = input("introduce un numero entero: ")

        pub.publish(numero)

if __name__ == '__main__':
    try: 
        talker() 
    except rospy.ROSInterruptException:
        pass
