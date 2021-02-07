#!/usr/bin/env python

""" services.py
    -used to handle all services 
"""

class service():
    Status='stopped'

    ActionFrequency_mins=10
    ScriptName=''

    def __init__(self, AssignmentContext, ScriptContext):
        #initial setup
        try:
            RoomID, RoomName, PlantID, PlantName, DeviceID, DeviceName = AssignmentContext
            ScriptName, ActionFrequency_mins = ScriptContext
        except:
            raise Exception("Failed to assign service context information")

    def start(self):
        #prepare to run service
            #TODO validate information to make sure the service can run
            #TODO condition/transform info for easier use in loop
                #TODO convert loop frequency from min to sec

        #run the service
        run_service()

    def terminate(self):
        self.Status='stopped'

    def update_status(self, status):
        #TODO send service status info to database

        #update variable
        self.Status=status

    def run_service(self):
        #main loop for running service
        #update service status
        update_status('running')

        #enter loop
        while self.Status=='running':
            try:
                #TODO loop stuff
            except:
                #main loop exited unexpectedly
                #update service status
                update_status('stopped')
                #TODO send diagnostics
        
        #TODO service is no longer running; do post-service stuff
