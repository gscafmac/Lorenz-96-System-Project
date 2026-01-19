import numpy as np

def eulers_method_sys(system, dt, final_time, initial_state=None):
    num_steps = int(final_time/dt)
    size = system.get_size()
    t = 0.0


    all_vals = np.zeros((size, num_steps))

    if initial_state is None:
        current_state = system.random_initial()
    else:
        current_state = initial_state.copy()

    all_vals[:,0] = current_state.copy()
    next_state = np.zeros(size)

    for i in range(num_steps-1):
        for j in range(size):
            derivative = system.get_eqs()[j].solve(current_state, t)
            next_state[j] = current_state[j] + (derivative * dt)
        all_vals[:,i+1] = next_state
        current_state = next_state.copy()
        t += dt

    return all_vals