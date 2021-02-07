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

    def start():
        #prepare to run service
        
        #run the service

    def terminate():
        #perform post-script stuff

    def update_status():
        #sends service status info to database

    def run_service():
        #main loop for running service
        
        #update service status
        #start loop
            try:
                #main loop
            except:
                #main loop exited unexpectedly
                #update service status
                #send diagnostics