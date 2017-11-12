#/usr/bin/env python

# Program to control a robot using Explorer Hat Pro and a Wiimote

# Import the modules needed 
import cwiid, time
import explorerhat as eh

# Connects and initialises the wiimote, if none connected the program will exit
button_delay = 0.1
print "Press 1 and 2 on the controller"
time.sleep(1)
try:
    wii = cwiid.Wiimote()
except RuntimeError:
    print "Cannot connect to your wiimote"
    quit()

print "Wiimote connected, ready to roll!"
time.sleep(1)

wii.rpt_mode = cwiid.RPT_BTN
wii.rumble = 1
time.sleep(1)
wii.rumble = 0

# Functions to define the robots movement
def robot_Left():
    eh.motor.one.forwards()
    eh.motor.two.backwards()

def robot_Right():
    eh.motor.one.backwards()
    eh.motor.two.forwards()

def robot_Forwards():
    eh.motor.forwards()

def robot_Backwards():
    eh.motor.backwards()

def robot_Stop():
    eh.motor.stop()


while True:
    # Main loop, checks which buttons are pressed and calls appropriate functions
    buttons = wii.state["buttons"]
    if (buttons & cwiid.BTN_UP):
        robot_Forwards()
        time.sleep(button_delay)
    elif (buttons & cwiid.BTN_DOWN):
        robot_Backwards()
        time.sleep(button_delay)
    elif (buttons & cwiid.BTN_RIGHT):
        robot_Right()
        time.sleep(button_delay)
    elif (buttons & cwiid.BTN_LEFT):
        robot_Left()
        time.sleep(button_delay)
    else:
        robot_Stop()
    
