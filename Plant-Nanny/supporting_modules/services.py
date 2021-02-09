#!/usr/bin/env python

""" services.py
    -used to handle all services 
"""

import time

class service():
    Status='stopped'

    ActionFrequency_mins=10
    LoopFrequency=1 #seconds
    ScriptName=''

    def __init__(self, AssignmentContext, ScriptContext):
        #initial setup
        try:
            RoomID, RoomName, PlantID, PlantName, DeviceID, DeviceName = AssignmentContext
            ScriptName, ActionFrequency_mins, StartWithAction = ScriptContext
        except:
            raise Exception("Failed to assign service context information")

    def start(self):
        #prepare to run service
            #TODO validate information to make sure the service can run
            #TODO condition/transform info for easier use in loop
                #TODO convert action frequency from min to sec


        #run the service
        self.run_service()

    def terminate(self):
        self.Status='stopped'

    def update_status(self, status):
        #TODO send service status info to database

        #update variable
        self.Status=status

    def perform_action(self):
    
    def run_service(self):
        #main loop for running service
        #update service status
        self.update_status('running')

        #enter loop
        if self.StartWithAction:
            self.perform_action()

        loopcounter=1
        while self.Status=='running':
            try:
                #TODO loop stuff
                print("Service Loop is Running!")
                
                time.sleep(self.LoopFrequency)

            except:
                #main loop exited unexpectedly
                #update service status
                self.update_status('stopped')
                #TODO send diagnostics
        
        #TODO service is no longer running; do post-service stuff

if __name__ == "__main__":
    testService=service([1,"Test Room",None,None,2,"Test Plant"],["TestScript.py", 0.25 , True])
    testService.start()
