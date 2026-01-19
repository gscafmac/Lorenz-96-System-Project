import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def animate_circle(data_arr):
    num_sys, num_steps = data_arr.shape

    fig, ax = plt.subplots(figsize=(6,6))
    ax.set_xlim(-1.53, 1.53)
    ax.set_ylim(-1.53, 1.53)
    ax.axis('off')

    # each angle for each circle
    angles = np.linspace(0, 2*np.pi, num_sys, endpoint=False)
    radius = 1.4
    positions = np.array([radius * np.cos(angles), radius * np.sin(angles)]).T # puts each circle in spot with x and y value

    # create circles
    scatter = ax.scatter(positions[:,0], positions[:,1], s=400, c=data_arr[:,0], cmap='viridis')

    cbar = fig.colorbar(scatter, ax=ax)
    cbar.set_label('Value') # Set the label for the colorbar

    # function to update called for each animation frame
    def update(frame):
        scatter.set_array(data_arr[:, frame])
        scatter.set_clim(np.min(data_arr), np.max(data_arr)) # normalize colorS
        return [scatter]

    # actually does the animating
    anim = FuncAnimation(fig, update, frames=num_steps, interval=10, blit=True)
    plt.show()


def plot_time_series(data, dt, N, F, indices=[0, 10, 20, 30]):
    t = np.arange(data.shape[1]) * dt
    
    plt.figure(figsize=(10, 5))
    for i in indices:
        plt.plot(t, data[i], label=f"$x_{i}$")
        
    plt.xlabel("Time")
    plt.ylabel("State Value")
    plt.title(f"System of Size {N} With forcing: {F}")
    plt.legend()
    plt.tight_layout()
    plt.show()


def perturbation_norm(data1, data2, dt, N, F):
    t = np.arange(data1.shape[1]) * dt
    diff = np.linalg.norm(data1 - data2, axis=0)

    plt.figure(figsize=(8, 5))
    plt.semilogy(t, diff)  # log scale vertical axis
    plt.xlabel("Time")
    plt.ylabel(r"$\| x(t) - \tilde{x}(t) \|_2$")
    plt.title(f"System of Size {N} With forcing: {F}")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def hovmoller_plot(data, dt):
    t = np.arange(data.shape[1]) * dt
    x = np.arange(data.shape[0])

    plt.figure(figsize=(10, 5))
    plt.imshow(data, aspect='auto', cmap='viridis',
               extent=[t[0], t[-1], x[-1], x[0]])
    plt.colorbar(label="Value")
    plt.xlabel("Time")
    plt.ylabel("Index (spatial position)")
    plt.title("Hovmöller Plot of Lorenz-96 Dynamics")
    plt.tight_layout()
    plt.show()