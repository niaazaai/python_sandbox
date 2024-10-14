# sub-plots and saving 

import matplotlib.pyplot as plt
import numpy as np

# Generate x values
x = np.linspace(-2 * np.pi, 2 * np.pi, 1000)

# Calculate y values for each function
y_cos = np.cos(x)  # Cosine wave
y_sin = np.sin(x)  # Sine wave
y_tan = np.tan(x)  # Tangent wave

# Create a figure with 3 subplots
fig, axs = plt.subplots(2, 1, figsize=(10, 12))

# Cosine Wave
axs[0].plot(x, y_cos, color='blue', label='Cosine Wave')
axs[0].set_title('Cosine Wave')
axs[0].set_ylabel('cos(x)')
axs[0].set_ylim(-1.5, 1.5)  # Limit y-axis for better visibility
axs[0].grid(True)
axs[0].legend()

# Sine Wave
axs[1].plot(x, y_sin, color='orange', label='Sine Wave')
axs[1].set_title('Sine Wave')
axs[1].set_ylabel('sin(x)')
axs[1].set_ylim(-1.5, 1.5)  # Limit y-axis for better visibility
axs[1].grid(True)
axs[1].legend()

# Tangent Wave
# axs[2].plot(x, y_tan, color='green', label='Tangent Wave')
# axs[2].set_title('Tangent Wave')
# axs[2].set_ylabel('tan(x)')
# axs[2].set_ylim(-10, 10)  # Limit y-axis for better visibility
# axs[2].grid(True)
# axs[2].legend()

# Adjust layout to prevent overlap
plt.tight_layout()
# plt.savefig('subplots.jpeg', dpi=300, transparent = True )
plt.show()
