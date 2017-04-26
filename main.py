import vrep
import vrep_gyro
import vrep_camera
import vrep_rotors
import cv2

try:
    vrep.simxFinish(-1)
    clientID = vrep.simxStart('127.0.0.1', 19999, True, True, 5000, 5)

    if clientID!=-1:
        print('Main Script Started')

        # Initialize IMU
        vrep_gyro.init_imu(clientID)

        # Initialize Camera
        camHandle = vrep_camera.init_cam(clientID)

        # Initialize Rotors
        vrep_rotors.init_rotors(clientID)

        # Start simulation
        vrep.simxStartSimulation(clientID, vrep.simx_opmode_oneshot_wait)

        while vrep.simxGetConnectionId(clientID) != -1:
            # Get IMU
            imu = vrep_gyro.get_imu(clientID)

            # Send Rotor Command
            rotor_vels = [5.3, 5.3, 5.3, 5.3]
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