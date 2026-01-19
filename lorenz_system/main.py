from equation_objects import LorenzSystemEquations, DerivEquation
from forcing import ConstantForcing, SinForcing, ConstantHeavySideForcing
from solvers import eulers_method_sys
from visualizations import animate_circle, plot_time_series, perturbation_norm
import numpy as np
#time series
'''
# Create system
size = 40
dt = 0.01
force = SinForcing(11,.1)
system1 = LorenzSystemEquations(size, force)

# baseline run
data1 = eulers_method_sys(system1, dt, final_time=150)

plot_time_series(data1, dt, size, force)
'''
'''
size = 40
force0 = SinForcing(1,.1)  # just pick one value to generate IC
system0 = LorenzSystemEquations(size, force0)

# generate a random IC (or you can hard-code one)
initial_state = system0.random_initial(lower=1, upper=5)

forcing_values = [1, 3, 7, 10, 12]
dt = .01
final_time = 200
results = {}


for F in forcing_values:
    force = SinForcing(F,.1)
    
    system1 = LorenzSystemEquations(size, force)
    data1 = eulers_method_sys(system1, dt=dt, final_time=final_time, initial_state=initial_state)

    results[F] = data1


for F in forcing_values:
    data1 = results[F]
    plot_time_series(data1, dt, size, F)
'''

'''
#used to plot the perturbation stuff

size = 40
force0 = ConstantForcing(3)  # just pick one value to generate IC
system0 = LorenzSystemEquations(size, force0)

# generate a random IC (or you can hard-code one)
initial_state = system0.random_initial(lower=1, upper=5)

forcing_values = [2, 4, 6, 8, 10]
dt = .01
final_time = 200

perturbation_size = 1e-6
perturbation_results = {}

for F in forcing_values:
    force = ConstantForcing(F)
    
    system1 = LorenzSystemEquations(size, force)
    data1 = eulers_method_sys(system1, dt=dt, final_time=final_time, initial_state=initial_state)

    system2 = LorenzSystemEquations(size, force)
    init_perturbed = data1[:,0].copy()
    init_perturbed[0] += perturbation_size

    data2 = eulers_method_sys(system2, dt=dt, final_time=final_time, initial_state=init_perturbed)
    
    # store perturbation_results[F] = (data1, data2)

for F in forcing_values:
    data1, data2 = perturbation_results[F]
    lyapunov_exp(data1, data2, dt, size, F)
'''

'''
size = 40
force0 = ConstantHeavySideForcing(20,1)  # just pick one value to generate IC
system0 = LorenzSystemEquations(size, force0)

# generate a random IC (or you can hard-code one)
initial_state = system0.random_initial(lower=1, upper=5)

forcing_values = [1, 3, 7, 10, 12]
dt = .01
final_time = 40
results = {}


for F in forcing_values:
    force = ConstantHeavySideForcing(F,20)
    
    system1 = LorenzSystemEquations(size, force)
    data1 = eulers_method_sys(system1, dt=dt, final_time=final_time, initial_state=initial_state)

    results[F] = data1


for F in forcing_values:
    data1 = results[F]
    plot_time_series(data1, dt, size, F)
'''

#initial_state = np.zeros((40))

size = 40
dt = 0.01
force = ConstantForcing(3)
system1 = LorenzSystemEquations(size, force)

# baseline run
data1 = eulers_method_sys(system1, dt, final_time=150)

animate_circle(data1)