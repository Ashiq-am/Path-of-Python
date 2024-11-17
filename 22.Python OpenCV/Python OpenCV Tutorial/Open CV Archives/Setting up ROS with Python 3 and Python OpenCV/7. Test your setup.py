#!/usr/bin/env python3

import rospy
import cv2


def main():
    rospy.init_node('opencv_ros_node', anonymous=True)
    rospy.loginfo("OpenCV ROS Node Initialized")

    # Your OpenCV code here
    # For example:
    cap = cv2.VideoCapture(0)
    while not rospy.is_shutdown():
        ret, frame = cap.read()
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
