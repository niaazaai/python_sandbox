import numpy as np
import matplotlib.pyplot as pt


# Create a grid of x and y values
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
x, y = np.meshgrid(x, y)

# Calculate z values based on the mathematical formula
z = np.sin(np.sqrt(x**2 + y**2))

# Create a 3D plot
fig = pt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot the surface
surface = ax.plot_surface(x, y, z, cmap='viridis', edgecolor='none')

# Add a color bar which maps values to colors
fig.colorbar(surface, shrink=0.5, aspect=10)

# Set titles and labels
ax.set_title('3D Plot of z = sin(sqrt(x^2 + y^2))')
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')

# Show the plot
pt.show()