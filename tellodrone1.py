from djitellopy import Tello
import cv2

#Camera capture dimensions
width = 320
height = 240

#0 = drone should fly, 1 = drone won't
startCounter = 0

#Connect to Tello
me = Tello()
me.connect()
me.for_back_velocity = 0
me.left_right_velocity = 0
me.up_down_velocity = 0
me.yaw_velocity = 0
me.speed = 0

#Display whether battery is good for flight
print(me.get_battery())

me.streamoff()
me.streamon()

while True:
    frame_read = me.get_frame_read()
    myFrame = frame_read.frame
    img = cv2.resize(myFrame, (width, height))

    #Initial takeoff, if drone hasn't already (startCounter)
    if startCounter == 0:
        me.takeoff()
        #20 centimeters to the left
        me.move_left(20)
        #90 degrees clockwise
        me.rotate_clockwise(90)
        startCounter = 1

    cv2.imshow("MyResult", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        me.land()
        break
