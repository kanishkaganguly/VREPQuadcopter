#!/usr/bin/python

import vrep
import time
import array
import numpy as np
import cv2
from PIL import Image

vrep.simxFinish(-1)

clientID = vrep.simxStart('127.0.0.1', 19999, True, True, 5000, 5)

if clientID!=-1:
    print('Connected to remote API server')

    res, frontCamHandle = vrep.simxGetObjectHandle(clientID, 'FrontCam', vrep.simx_opmode_oneshot_wait)
    if res == vrep.simx_return_ok:
        print('Got Camera Handle')
        print('Starting camera stream')
        err, resolution, image = vrep.simxGetVisionSensorImage(clientID, frontCamHandle, 0, vrep.simx_opmode_streaming)
        time.sleep(1)
        while vrep.simxGetConnectionId(clientID) != -1:
            err, resolution, image = vrep.simxGetVisionSensorImage(clientID, frontCamHandle, 0, vrep.simx_opmode_buffer)
            if err == vrep.simx_return_ok:
              image_byte_array = array.array('b', image)
              image_buffer = Image.frombuffer("RGB", (resolution[0], resolution[1]), image_byte_array, "raw", "RGB", 0, 1)
              img_out = np.asarray(image_buffer)
              img_out = cv2.flip(img_out, 0)
              cv2.imshow("DroneCamera",img_out)
              cv2.waitKey(1)
            elif err == vrep.simx_return_novalue_flag:
              print "no image yet"
              pass
            else:
              print err
else:
    print "Failed to connect to remote API Server"
    vrep.simxFinish(clientID)
cv2.destroyAllWindows()