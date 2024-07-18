# Import libraries
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.widgets import Slider

# Define space-time events function
def generate_events(num_events=100):
    time = np.linspace(0, 10, num_events)
    space_x = np.sin(time)
    space_y = np.cos(time)
    return time, space_x, space_y

# Generate events
time, space_x, space_y = generate_events()

# Setup 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot events
ax.scatter(time, space_x, space_y, c='r', marker='o')

# Labels and title
ax.set_xlabel('Time')
ax.set_ylabel('X')
ax.set_zlabel('Y')
ax.set_title('3D Visualization of Minkowski Space-time')

# Show plot
plt.show()
