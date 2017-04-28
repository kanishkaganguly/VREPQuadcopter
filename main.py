#!/usr/bin/python

import vrep
import rl_helper

rl_functions = None
try:
    vrep.simxFinish(-1)
    clientID = vrep.simxStart('127.0.0.1', 19999, True, True, 5000, 5)

    if clientID != -1:
        rl_functions = rl_helper.RL(clientID)
        print('Main Script Started')

        rl_functions.init_sensors()
        rl_functions.start_sim()

        while vrep.simxGetConnectionId(clientID) != -1:
            rl_functions.rotor_data = [5.4, 5.4, 5.4, 5.4]
            rl_functions.do_action()
            rl_functions.target_z = 5.0
            print(rl_functions.get_reward())
    else:
        print "Failed to connect to remote API Server"
        rl_functions.stop_sim()
        vrep.simxFinish(clientID)
except KeyboardInterrupt:
    rl_functions.stop_sim()
    vrep.simxFinish(clientID)
