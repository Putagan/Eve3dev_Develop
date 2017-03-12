from ev3dev.ev3 import *
import os,time
import pid
import sys
import Motion
# os.system('espeak -s 120 -v zh \'woyaoshiyong\' --stdout|aplay')
# os.system('espeak -s 120 -v en-us \'p i d\' --stdout|aplay')
# os.system('espeak -s 120 -v zh \'suanfa\' --stdout|aplay')

# pid= pid.PID(P=sys.argv[1],I=sys.argv[2],D=sys.argv[3])
pid=pid.PID(P=0.2,I=0.2,D=0.3)
motion = Motion.motion()



while True:
    # time.sleep(1)
    angle=motion.getGyro()
    pid.update(angle)
    out = int(pid.output*10)
    print "\n"
    print angle
    print out
    print motion.getDist()


    if out>=1000:
        out=1000
    elif out<=-1000:
        out=-1000    


    if angle>=0:
        motion.motion_left(-out)
    else:
        motion.motion_right(out)

