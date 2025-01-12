# FILE: /3d-light-cone-plot/3d-light-cone-plot/src/light_cone_plot.py
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define parameters for the light cone
def generate_light_cone(t_max, num_points):
    t = np.linspace(0, t_max, num_points)
    x = t
    y_pos = np.sqrt(t**2)  # Light travels at speed c=1
    y_neg = -np.sqrt(t**2)
    return t, x, y_pos, y_neg

# Plotting function
def plot_light_cone(t_max=10, num_points=100):
    t, x, y_pos, y_neg = generate_light_cone(t_max, num_points)

    # Set up the 3D plot
    fig = plt.figure(figsize=(10, 8), facecolor='black')
    ax = fig.add_subplot(111, projection='3d')

    # Create the light cone surfaces
    ax.plot(x, y_pos, t, color='cyan', linewidth=2, label='Light Cone (Forward)')
    ax.plot(x, y_neg, t, color='magenta', linewidth=2, label='Light Cone (Backward)')
    
    # Customize the plot
    ax.fill_between(x, y_pos, y_neg, t, color='blue', alpha=0.1)
    ax.set_xlim(0, t_max)
    ax.set_ylim(-t_max, t_max)
    ax.set_zlim(0, t_max)
    
    # Labels and title
    ax.set_title('3D Light Cone Plot', color='cyan', fontsize=16)
    ax.set_xlabel('Time', color='white', fontsize=14)
    ax.set_ylabel('Space', color='white', fontsize=14)
    ax.set_zlabel('Light Path', color='white', fontsize=14)
    
    plt.legend()
    plt.show()

if __name__ == "__main__":
    plot_light_cone()