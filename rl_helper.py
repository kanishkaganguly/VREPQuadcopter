#!/usr/bin/python

import numpy as np
import math
from scipy.stats import norm

'''
This function returns reward based on previous distributions and given location data (x,y,z)
'''
def get_reward(curr_location, orig_location, target_z):
    deviation_x = np.linalg.norm(curr_location[0]-orig_location[0])
    deviation_y = np.linalg.norm(curr_location[1] - orig_location[1])
    deviation_z = np.linalg.norm(target_z - curr_location[2])
    gaussian = norm(0,2)

    reward_x = gaussian.pdf(deviation_x)
    reward_y = gaussian.pdf(deviation_y)
    reward_z = 1-math.exp(deviation_z)

    total_reward = 2*(0.5*reward_x + 0.5*reward_y + reward_z)
    return total_reward