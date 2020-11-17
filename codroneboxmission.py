# -*- coding: utf-8 -*-
"""CoDroneBoxMission.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/14ei-kkpoEjpwZarjriN0lAIERH4SzaYw
"""

import pandas as pd 
import CoDrone
drone = CoDrone.CoDrone() 
drone.pair()  # pairs to previous drone

#Opens up the Excel file 
table=pd.read_excel('Book1.xlsx', sheet_name="Sheet2")

# Reads the values from the Excel to a variable

# Each leg of the box will be 100 cm. Tello uses cm units by default.
pitch_power = table['Value'][0]
pitch_power = pitch_power

# Yaw 90 degrees
yaw_power = table['Value'][1]
yaw_power = yaw_power

drone.takeoff(2)           # takeoff for 2 seconds
drone.hover(3)            # hover for 3 seconds

drone.set_pitch(pitch_power)       # set positive pitch at 30% power
drone.move(2)             # forward for 2 seconds

drone.set_pitch(0)        # reset pitch
drone.set_yaw(yaw_power)       # set positive yaw at 50 %power
drone.move(2)             # left for 2 seconds

drone.set_pitch(pitch_power)       # set positive pitch at 30% power
drone.move(2)             # forward for 2 seconds

drone.set_pitch(0)        # reset pitch
drone.set_yaw(yaw_power)         # set positive yaw at 50% power
drone.move(2)

drone.set_pitch(pitch_power)       # set positive pitch at 30% power
drone.move(2)                 # forward for 2 seconds

drone.set_pitch(0)        # reset pitch
drone.set_yaw(yaw_power)       # set positive yaw at 50% power
drone.move(2)

drone.set_pitch(pitch_power)       # set positive pitch at 30% power
drone.move(2)             # forward for 2 seconds

drone.set_pitch(0)        # reset pitch
drone.set_yaw(yaw_power)       # set positive yaw at 50% power
drone.move(2)

drone.land()              # lands the CoDrone
drone.close()             # disconnects CoDrone