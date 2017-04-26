#!/usr/bin/python

import vrep

def init_imu(clientID):
    vrep.simxGetFloatSignal(clientID, 'gyroX', vrep.simx_opmode_streaming)
    vrep.simxGetFloatSignal(clientID, 'gyroY', vrep.simx_opmode_streaming)
    vrep.simxGetFloatSignal(clientID, 'gyroZ', vrep.simx_opmode_streaming)

    vrep.simxGetFloatSignal(clientID, 'accelX', vrep.simx_opmode_streaming)
    vrep.simxGetFloatSignal(clientID, 'accelY', vrep.simx_opmode_streaming)
    vrep.simxGetFloatSignal(clientID, 'accelZ', vrep.simx_opmode_streaming)


def get_imu(clientID):
    err, gX = vrep.simxGetFloatSignal(clientID, 'gyroX', vrep.simx_opmode_buffer)
    err, gY = vrep.simxGetFloatSignal(clientID, 'gyroY', vrep.simx_opmode_buffer)
    err, gZ = vrep.simxGetFloatSignal(clientID, 'gyroZ', vrep.simx_opmode_buffer)

    err, aX = vrep.simxGetFloatSignal(clientID, 'accelX', vrep.simx_opmode_buffer)
    err, aY = vrep.simxGetFloatSignal(clientID, 'accelY', vrep.simx_opmode_buffer)
    err, aZ = vrep.simxGetFloatSignal(clientID, 'accelZ', vrep.simx_opmode_buffer)

    print('%.2f,%.2f,%.2f,%.2f,%.2f,%.2f') % (gX, gY, gZ, aX, aY, aZ)
    return [gX, gY, gZ, aX, aY, aZ]
