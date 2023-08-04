import matplotlib
matplotlib.use('TkAgg')

import numpy as np
import matplotlib.pyplot as plt

# Generate a random complex state vector
state_vector = np.random.rand(1000) + 1j * np.random.rand(1000)

# Normalize the state vector
state_vector /= np.linalg.norm(state_vector)

# Compute the probabilities
probabilities = np.abs(state_vector)**2

# Create a histogram
plt.hist(probabilities, bins=100)
plt.show()
