import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
'''
class DerivEquation:
    def __init__(self, index, sys_size, forcing):
        self.index = index
        self.sys_size = sys_size
        self.forcing = forcing
    
    def solve(self, state_vec, t):
        # case where need to wrap x_n-1 to last n and x_n-2 to second to last
        if self.index == 0:
            return (state_vec[self.index+1] - state_vec[self.sys_size-2]) * state_vec[self.sys_size-1] - state_vec[self.index] + self.forcing(t)
        
        # case where need to wrap x_n-2 to last n
        if self.index == 1:
            return (state_vec[self.index+1] - state_vec[self.sys_size-1]) * state_vec[self.index-1] - state_vec[self.index] + self.forcing(t) 
          
        # case where need to wrap x_n+1 to first term
        if self.index == self.sys_size-1:
            return (state_vec[0] - state_vec[self.index-2]) * state_vec[self.index-1] - state_vec[self.index] + self.forcing(t)

        # normal case
        return (state_vec[self.index+1] - state_vec[self.index-2]) * state_vec[self.index-1] - state_vec[self.index] + self.forcing(t)
'''


class DerivEquation:
    def __init__(self, index, sys_size, forcing):
        self.index = index
        self.sys_size = sys_size
        self.forcing = forcing
    
    def solve(self, state_vec, t):
        # case where need to wrap x_n-1 to last n and x_n-2 to second to last
        if self.index == 0:
            return (state_vec[self.index+1] - 1) * 1 - state_vec[self.index] + self.forcing(t)
        
        # case where need to wrap x_n-2 to last n
        if self.index == 1:
            return (state_vec[self.index+1] - 1) * state_vec[self.index-1] - state_vec[self.index] + self.forcing(t) 
          
        # case where need to wrap x_n+1 to first term
        if self.index == self.sys_size-1:
            return (1 - state_vec[self.index-2]) * state_vec[self.index-1] - state_vec[self.index] + self.forcing(t)

        # normal case
        return (state_vec[self.index+1] - state_vec[self.index-2]) * state_vec[self.index-1] - state_vec[self.index] + self.forcing(t)
    

class LorenzSystemEquations:
    def __init__(self, sys_size, forcing):
        self.sys_size = sys_size
        self.forcing = forcing
        # list of equation objects
        self.eq_list = [DerivEquation(i, self.sys_size, self.forcing) for i in range(sys_size)]# make new list full of each equation starting from x_0

    def get_size(self):
        return self.sys_size
    
    def get_eqs(self):
        return self.eq_list
    
    def random_initial(self, lower=1, upper=5):
        return np.random.randint(lower, upper, self.sys_size)