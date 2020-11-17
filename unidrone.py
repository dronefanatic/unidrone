import pandas as pd 
import CoDrone
import math
import socket
import time
import threading
from datetime import datetime


class Stats(object):
    def __init__(self, command, id):
        """
        Constructor.
        :param command: The command sent.
        :param id: The identifier.
        """
        self.command = command
        self.response = None
        self.id = id

        self.start_time = datetime.now()
        self.end_time = None
        self.duration = None

    def add_response(self, response):
        """
        Adds the response.
        :param response: Response.
        :return: None.
        """
        self.response = response
        self.end_time = datetime.now()
        self.duration = self.get_duration()

    def get_duration(self):
        """
        Gets the duration.
        :return: Duration.
        """
        diff = self.end_time - self.start_time
        return diff.total_seconds()

    def print_stats(self):
        """
        Prints the statistics.
        :return: None.
        """
        print(f'\nid {self.id}')
        print(f'command: {self.command}')
        print(f'response: {self.response}')
        print(f'start_time: {self.start_time}')
        print(f'end_time: {self.end_time}')
        print(f'duration: {self.duration}')

    def got_response(self):
        """
        Returns a boolean if a response was received.
        :return: Boolean.
        """
        
        if self.response is None:
            return False
        else:
            return True

    def return_stats(self):
        """
        Returns the statistics.
        :return: Statistics.
        """
        str = ''
        str +=  f'\nid: {self.id}\n'
        str += f'command: {self.command}\n'
        str += f'response: {self.response}\n'
        str += f'start_time: {self.start_time}\n'
        str += f'end_time: {self.end_time}\n'
        str += f'duration: {self.duration}\n'
        return str
    
class Tello(object):
    def __init__(self):
        """
        Constructor.
        """
        self.local_ip = ''
        self.local_port = 9000
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.bind((self.local_ip, self.local_port))

        # thread for receiving cmd ack
        self.receive_thread = threading.Thread(target=self._receive_thread)
        self.receive_thread.daemon = True
        self.receive_thread.start()

        self.tello_address = ('192.168.10.1',8889)
        self.log = []

        self.MAX_TIME_OUT = 15.0

    def send_command(self, command):
        """
        Send a command to the ip address. Will be blocked until
        the last command receives an 'OK'.
        If the command fails (either b/c time out or error),
        will try to resend the command
        :param command: (str) the command to send
        :param ip: (str) the ip of Tello
        :return: The latest command response
        """
        self.log.append(Stats(command, len(self.log)))

        self.socket.sendto(command.encode('utf-8'), self.tello_address)
        print(f'sending command: {command} to {self.tello_ip}')

        start = time.time()
        while not self.log[-1].got_response():
            now = time.time()
            diff = now - start
            if diff > self.MAX_TIME_OUT:
                print(f'Max timeout exceeded... command {command}')
                return
        print(f'Done!!! sent command: {command} to {self.tello_ip}')

    def _receive_thread(self):
        """
        Listen to responses from the Tello.
        Runs as a thread, sets self.response to whatever the Tello last returned.
        """
        while True:
            try:
                self.response, ip = self.socket.recvfrom(1024)
                print(f'from {ip}: {self.response}')

                self.log[-1].add_response(self.response)
            except Exception as exc:
                print(f'Caught exception socket.error : {exc}')

    def on_close(self):
        """
        On close.
        :returns: None.
        """
        pass

    def get_log(self):
        """
        Gets the logs.
        :returns: Logs.
        """
        return self.log
    
# class drone:
    # def __init__(self, droneType):
    #     self.droneType = droneType

    #     #initializing CoDrone
    #     if droneType == 1:
    #         self.drone = CoDrone.CoDrone()

    #     #initializing Tello
    #     elif droneType == 2:
    #         import socket
    #         import threading
    #         import time

    #         # IP and port of Tello
    #         tello_address = ('192.168.10.1', 8889)

    #         # IP and port of local computer
    #         local_address = (('', 9000))

    #         # Create a UDP connection that we'll send the command to
    #         sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    #         # Bind to the local address and port
    #         sock.bind(local_address)

    #         #Send the values to the socket


    #         # Send the message to Tello and allow for a delay in seconds
    #         def send(message, delay):
    #           # Try to send the message otherwise print the exception
    #           try:
    #             sock.sendto(message.encode(), tello_address)
    #             print("Sending message: " + message)
    #           except Exception as e:
    #             print("Error sending: " + str(e))

    #           # Delay for a user-defined period of time
    #           time.sleep(delay)

    #         # Receive the message from Tello
    #         def receive():
    #           # Continuously loop and listen for incoming messages
    #           while True:
    #             # Try to receive the message otherwise print the exception
    #             try:
    #               response, ip_address = sock.recvfrom(128)
    #               print("Received message: " + response.decode(encoding='utf-8'))
    #             except Exception as e:
    #               # If there's an error close the socket and break out of the loop
    #               sock.close()
    #               print("Error receiving: " + str(e))
    #               break

    #         # Create and start a listening thread that runs in the background
    #         # This utilizes our receive functions and will continuously monitor for incoming messages
    #         receiveThread = threading.Thread(target=receive)
    #         receiveThread.daemon = True
    #         receiveThread.start()

            # Put Tello into command mode
            # send("command", 3)
            # printM()
            # printM()
            # printM()
            # printM()
            # printM()
            # printM()
            # printM()
            # Print message
            # print("Mission completed successfully!")
            # Close the socket
            # sock.close()
        
            
#    recieve()
# if a == 'takeoff':
#     msg='send("%s",%d)'%(a,c)
#     def printM():
#         print(msg)
# elif cmd == 'forward':
#     msg='send("%s"+%d,%d)'%(cmd,dist,val)
#     def printM():
#         print(msg)
# elif cmd == 'backward':
#     msg='send("%s"+%d,%d)'%(cmd,dist,val)
#     def printM():
#         print(msg)
# elif cmd == 'cw':
#     msg='send("%s"+%d,%d)'%(cmd,dist,val)
#     def printM():
#         print(msg)
# elif cmd == 'ccw':
#     msg='send("%s"+%d,%d)'%(cmd,dist,val)
#     def printM():
#         print(msg)
# elif cmd == 'right':
#     msg='send("%s"+%d,%d)'%(cmd,dist,val)
#     def printM():
#         print(msg)
# elif cmd == 'left':
#     msg='send("%s"+%d,%d)'%(cmd,dist,val)
#     def printM():
#         print(msg)
# elif cmd == 'land':
#     msg='send("%s"+%d,%d)'%(cmd,dist,val)
#     def printM():
#         print(msg)
    
    # def takeOff(self, duration=None):
    #     # CoDrone
    #     if self.droneType == 1:
    #         self.takeoff(duration)
    #     # Tello
    #     elif self.droneType == 2:
    #         def recieve():
    #             a='takeoff'
    #             b=0
    #             c=5
    #             return a,b,c
            
    # def turncw (self, yaw_angle):
    #     #CoDrone
    #     if self.droneType == 1:
    #        self.drone.set_yaw(yaw_angle) 
    #        self.drone.move(2)
    #     #Tello
    #     elif self.droneType == 2:
    #         def recieve():
    #             a='cw'
    #             b=yaw_angle
    #             c=3
    #             return a,b,c
            
    # def turnccw (self, yaw_angle):
    #     #CoDrone
    #     if self.droneType == 1:
    #        self.drone.set_yaw(-(yaw_angle)) 
    #        self.drone.move(2)
    #     #Tello
    #     elif self.droneType == 2:
    #         def recieve():
    #             a='ccw'
    #             b=yaw_angle
    #             c=3
    #             return a,b,c

    # def Forward(self, distance):
    #     # CoDrone
    #     if self.droneType == 1:
    #         speed = 20
    #         time= distance/ speed 
    #         self.drone.set_pitch(30) 
    #         self.drone.move(time)

    #     # Tello
    #     elif self.droneType == 2:
    #         def recieve():
    #             a='forward'
    #             b=distance
    #             c=4
    #             return a,b,c
            
            
    # def Backward(self, distance):
    #     # CoDrone
    #     if self.droneType == 1:
    #         speed = 20
    #         time= distance/ speed 
    #         self.drone.set_pitch(-distance) 
    #         self.drone.move(time)

    #     # Tello
    #     elif self.droneType == 2:
    #         def recieve():
    #             a='back'
    #             b=distance
    #             c=4
    #             return a,b,c
            
        
            
    # def Rollright(self, roll_dist):
    #     # CoDrone
    #     if self.droneType == 1:
    #         self.drone.set_roll(roll_dist) # power represents power out of 100%
    #         self.drone.move(2)

    #     # Tello
    #     elif self.droneType == 2:
    #         def recieve():
    #             a='right'
    #             b=roll_dist
    #             c=4
    #             return a,b,c
            
            
    # def Rollleft(self, roll_dist):
    #     # CoDrone
    #     if self.droneType == 1:
    #         self.drone.set_roll(-roll_dist) # power represents power out of 100%
    #         self.drone.move(2)

    #     # Tello
    #     elif self.droneType == 2:
    #         def recieve():
    #             a='left'
    #             b=roll_dist
    #             c=4   
    #             return a,b,c

    # def Land(self, duration=None):
    #     # CoDrone
    #     if self.droneType == 1:
    #         self.drone.land() 
    #     # Tello
    #     elif self.droneType == 2:
    #         def recieve():
    #             a='land'
    #             b=0
    #             c=5
    #             return a,b,c
   
   



# Jack = drone(droneType=1)

