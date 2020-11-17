# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 18:20:30 2020

@author: Archille
"""

import unidrone
import app
import pandas as pd

# table= pd.read_excel('Book1.xlsx')
# droneT=table['Value'][0]
# droneT=droneT

# lift_off = table['Value'][1]
# lift_off = lift_off

# p1=table['Parameters'][2]
# value1=table['Value'][2]

# p2=table['Parameters'][3]
# value2=table['Value'][3]

# p3=table['Parameters'][4]
# value3=table['Value'][4]

# p4=table['Parameters'][5]
# value4=table['Value'][5]

# p5=table['Parameters'][6]
# value5=table['Value'][6]

# p6=table['Parameters'][7]
# value6=table['Value'][7]

# ctrlList=['Forward','Backward','Hover','Yaw right','Yaw left','Roll right','Roll left']
# paraList=[p1,p2,p3,p4,p5,p6]
#paraDict= 
# vaueList=[value1,value2,value3,value4,value5,value6]

# ctrl_dict=

# if droneT=='TelloDrone':
#     TelloDrone=unidrone.drone(droneType=2)
#     if lift_off =='ON'
#     TelloDrone.takeOff()
    
      

#Testing tello
# TelloDrone = unidrone.drone(droneType=2) 
# TelloDrone.takeOff()
# TelloDrone.Forward(20)
# TelloDrone.Rollright(10)
# TelloDrone.Land()

# Testing codrone
# codrone = unidrone.drone(droneType=1)
# codrone.takeOff(5)
# codrone.Forward(50)
# codrone.Rollright(30)
# codrone.Land()
file_name='command.txt'
tellodrone=unidrone.Tello()
startdrone=app.start(file_name)
tellodrone.__init__()
tellodrone.send_command()
tellodrone.add_response()
tellodrone._receive_thread()
app.start(file_name)



# if droneT == 'TelloDrone':
#     Tello=drone(droneType=2)
#     yaw_direction = "cw"
#     # Put Tello into command mode
#     send("command", 3)

#     # Send the takeoff command
#     send("takeoff", 5)

#     # Fly forward
#     send("forward " + str(box_leg_distance), 4)

#     # Yaw right
#     send("cw " + str(yaw_angle), 3)

#     # Fly forward
#     send("forward " + str(box_leg_distance), 4)

#     # Yaw right
#     send("cw " + str(yaw_angle), 3)

#     # Fly forward
#     send("forward " + str(box_leg_distance), 4)

#     # Yaw right
#     send("cw " + str(yaw_angle), 3)

#     # Fly forward
#     send("forward " + str(box_leg_distance), 4)

#     # Yaw right
#     send("cw " + str(yaw_angle), 3)

#     # Land
#     send("land", 5)

#     # Print message
#     print("Mission completed successfully!")

#     # Close the socket
#     sock.close()
    

