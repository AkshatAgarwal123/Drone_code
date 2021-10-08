from djitellopy import tello
from time import sleep

#me is what we call an instance tello.Tello class
#me is like a handle– it allows us to interact with the drone. it can be thought of as a cursor
me = tello.Tello()

#connect to drone
me.connect()

#make sure battery is good
print(me.get_battery())

me.takeoff()
me.send_rc_control(0, 50, 0, 0)
sleep(2)
me.send_rc_control(0, 0, 0, 0)
sleep(2)
me.send_rc_control(0, 0, 0, 0)
me.land()
