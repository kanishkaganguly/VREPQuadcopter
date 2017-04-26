import vrep

propellers = ['propeller1Vel','propeller2Vel','propeller3Vel','propeller4Vel']

vrep.simxFinish(-1)
clientID = vrep.simxStart('127.0.0.1', 19999, True, True, 5000, 5)

if clientID!=-1:
    print('Propeller Controller Started')

    # Clear all signals
    for i in range(len(propellers)):
        vrep.simxClearFloatSignal(clientID, propellers[i], vrep.simx_opmode_oneshot)

    # Set all propellers to zero
    for i in range(len(propellers)):
        vrep.simxSetFloatSignal(clientID, propellers[i], 0.0, vrep.simx_opmode_oneshot)

    while vrep.simxGetConnectionId(clientID) != -1:
        vrep.simxSetFloatSignal(clientID, propellers[0], 5.2, vrep.simx_opmode_oneshot)
        vrep.simxSetFloatSignal(clientID, propellers[1], 5.2, vrep.simx_opmode_oneshot)
        vrep.simxSetFloatSignal(clientID, propellers[2], 5.2, vrep.simx_opmode_oneshot)
        vrep.simxSetFloatSignal(clientID, propellers[3], 5.2, vrep.simx_opmode_oneshot)

else:
    print "Failed to connect to remote API Server"
    vrep.simxFinish(clientID)