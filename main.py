#!/usr/bin/python

import vrep
import vrep_imu
import vrep_camera
import vrep_rotors
import cv2

try:
    vrep.simxFinish(-1)
    clientID = vrep.simxStart('127.0.0.1', 19999, True, True, 5000, 5)

    if clientID!=-1:
        print('Main Script Started')

        # Initialize IMU
        err, quadHandle = vrep.simxGetObjectHandle(clientID,'Quadricopter_base',vrep.simx_opmode_blocking)
        vrep_imu.init_imu(clientID,quadHandle)

        # Initialize Camera
        camHandle = vrep_camera.init_cam(clientID)

        # Initialize Rotors
        vrep_rotors.init_rotors(clientID)

        # Reset quadcopter position
        err, pos = vrep.simxGetObjectPosition(clientID, quadHandle, -1, vrep.simx_opmode_buffer)
        pos[2] = 0.0
        vrep.simxSetObjectPosition(clientID, quadHandle, -1, pos, vrep.simx_opmode_oneshot)

        # Start simulation
        vrep.simxStartSimulation(clientID, vrep.simx_opmode_oneshot_wait)

        throttle = 5.0
        while vrep.simxGetConnectionId(clientID) != -1:
            if throttle < 5.4:
                throttle=throttle+0.001

            # Get IMU
            imu = vrep_imu.get_imu(clientID)
            height = vrep_imu.get_height(clientID, quadHandle)
            print(height)

            # Send Rotor Command
            rotor_vels = [throttle,throttle,throttle,throttle]
            vrep_rotors.move_rotors(clientID, rotor_vels)

            # Get Camera
            err,img = vrep_camera.get_cam(clientID,camHandle)
            if err is 1:
                cv2.imshow('DroneCam', img)
                cv2.waitKey(1)
            else:
                pass
        cv2.destroyAllWindows()
    else:
        print "Failed to connect to remote API Server"
        vrep.simxStopSimulation(clientID, vrep.simx_opmode_oneshot_wait)
        vrep.simxFinish(clientID)
except KeyboardInterrupt:
    vrep.simxStopSimulation(clientID, vrep.simx_opmode_oneshot_wait)
    vrep.simxFinish(clientID)