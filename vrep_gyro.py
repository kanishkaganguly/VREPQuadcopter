#!/usr/bin/python

import vrep
import time
import array
import numpy as np

vrep.simxFinish(-1)

clientID = vrep.simxStart('127.0.0.1', 19999, True, True, 5000, 5)

err,gX = vrep.simxGetFloatSignal(clientID,'gyroX',vrep.simx_opmode_streaming)
err,gY = vrep.simxGetFloatSignal(clientID,'gyroY',vrep.simx_opmode_streaming)
err,gZ = vrep.simxGetFloatSignal(clientID,'gyroZ',vrep.simx_opmode_streaming)

err,aX = vrep.simxGetFloatSignal(clientID,'accelX',vrep.simx_opmode_streaming)
err,aY = vrep.simxGetFloatSignal(clientID,'accelY',vrep.simx_opmode_streaming)
err,aZ = vrep.simxGetFloatSignal(clientID,'accelZ',vrep.simx_opmode_streaming)

if clientID!=-1:
    print('Connected to remote API server')
    while vrep.simxGetConnectionId(clientID) != -1:
        err, gX = vrep.simxGetFloatSignal(clientID, 'gyroX', vrep.simx_opmode_buffer)
        err, gY = vrep.simxGetFloatSignal(clientID, 'gyroY', vrep.simx_opmode_buffer)
        err, gZ = vrep.simxGetFloatSignal(clientID, 'gyroZ', vrep.simx_opmode_buffer)

        err, aX = vrep.simxGetFloatSignal(clientID, 'accelX', vrep.simx_opmode_buffer)
        err, aY = vrep.simxGetFloatSignal(clientID, 'accelY', vrep.simx_opmode_buffer)
        err, aZ = vrep.simxGetFloatSignal(clientID, 'accelZ', vrep.simx_opmode_buffer)

        print('%.2f,%.2f,%.2f,%.2f,%.2f,%.2f') % (gX, gY, gZ, aX, aY, aZ)
else:
    print "Failed to connect to remote API Server"
    vrep.simxFinish(clientID)