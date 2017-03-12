from ev3dev.ev3 import *
import os,time

Gyro = GyroSensor('in4')
Motor_L = LargeMotor('outA')
Motor_R = LargeMotor('outD')


def motion_right(speed):
        Motor_L.run_timed(time_sp=3000,speed_sp=-speed)
        Motor_R.run_timed(time_sp=3000,speed_sp=speed)
def motion_left(speed):
        Motor_L.run_timed(time_sp=3000,speed_sp=speed)
        Motor_R.run_timed(time_sp=3000,speed_sp=-speed)
 
while True:
    angle=Gyro.value()
    if angle>=0:
      motion_left(500)
    else:
      motion_right(500)




