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
            #TODO validate information to make sure the service can run
            validate_assignmentcontext(AssignmentContext)
            validate_scriptcontext(ScriptContext)
            self.RoomID, self.RoomName, self.PlantID, self.PlantName, self.DeviceID, self.DeviceName = AssignmentContext
            self.ScriptName, self.ActionFrequency_mins, self.StartWithAction = ScriptContext
        except:
            raise Exception("Failed to assign service context information")

    def start(self):
        #prepare to run service
            #TODO condition/transform info for easier use in loop
                #TODO convert action frequency from min to sec
        self.looplength=60*self.ActionFrequency_mins/self.LoopFrequency
        #run the service
        self.run_service()

    def terminate(self):
        self.Status='stopped'

    def update_status(self, status):
        #TODO send service status info to database

        #update variable
        self.Status=status

    def perform_action(self):
        #TODO This stuff
        print("perform_action was called")

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
                #TODO all math for calculating looping parameters is wrong
                print("Service Loop is Running (%s / %s)" %(loopcounter, self.looplength))

                if loopcounter<self.looplength:
                    loopcounter+=1
                else:
                    self.perform_action()
                    loopcounter=0

                time.sleep(self.LoopFrequency)

            except:
                #main loop exited unexpectedly
                #update service status
                self.update_status('stopped')
                #TODO send diagnostics
        
        #TODO service is no longer running; do post-service stuff

def validate_assignmentcontext(AssignmentContext):
    #Checks that the script data supplied to the service is usable
    RoomID, RoomName, PlantID, PlantName, DeviceID, DeviceName = AssignmentContext
    
    #Variable Checks
    assert isinstance(RoomID, int) or RoomID is None , "RoomID was not assigned properly"
    assert isinstance(PlantID, int) or PlantID is None, "PlantID was not assigned properly"
    assert isinstance(DeviceID, int) or DeviceID is None, "DeviceID was not assigned properly"

    #Context Checks
    assert ((RoomID is not None) or (PlantID is not None)), "RoomID and PlantID were not provided; at least one of these must be provided"
    assert (RoomID )

def validate_scriptcontext(ScriptContext):
    #Checks that the script data supplied to the service is usable
    ScriptName, ActionFrequency_mins, StartWithAction = ScriptContext


if __name__ == "__main__":
    testService=service([1,"Test Room",None,None,2,"Test Plant"],["TestScript.py", 0.25 , True])
    testService.start()
