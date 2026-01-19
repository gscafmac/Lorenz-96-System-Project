import numpy as np
import matplotlib.pyplot as plt

def lorenz96_jacobian(F, N):
    J = np.zeros((N, N))
    
    for i in range(N):
        ip1 = (i + 1) % N   # i+1, cyclic
        im1 = (i - 1) % N   # i-1, cyclic
        im2 = (i - 2) % N   # i-2, cyclic
        
        J[i, im2] = -F       # derivative w.r.t x_{i-2}
        J[i, im1] = 0        # derivative w.r.t x_{i-1} at equilibrium
        J[i, i]   = -1       # derivative w.r.t x_i
        J[i, ip1] = F        # derivative w.r.t x_{i+1}
        #this only computes with respect to the neighbors because all other derivatives are 0
    
    return J

#here 
# Parameters
N = 40  # system size
forcing_values = np.linspace(-8, 12, 50)  # create 50 numbers between 2 and 12 for forcing
max_real_eigen = []

for F in forcing_values:
    J = lorenz96_jacobian(F, N)
    eigenvals = np.linalg.eigvals(J)
    max_real_eigen.append(np.max(np.real(eigenvals)))

# Plot largest real part of eigenvalues vs forcing
plt.figure(figsize=(10,6))
plt.plot(forcing_values, max_real_eigen, 'o-', color='blue')
plt.axhline(0, color='red', linestyle='--', label='Re(λ)=0')
plt.xlabel("Forcing F")
plt.ylabel("Largest real part of eigenvalues")
plt.title("Linear Stability of L96 Equilibrium vs Forcing")
plt.legend()
plt.grid(True)
plt.show()