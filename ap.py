import numpy as np
import pandas as pd

# Set up the initial state (all zeros)
initial_state = np.zeros(192, dtype=int)

# Set up the state transition matrix
transition_matrix = np.array([[0.25, 0.25, 0.25, 0.25]] * 4)

# Perform the simulation
state = initial_state
states = []  # List to store the states
for _ in range(10000):  # however many steps you want
    for i in range(192):
        state[i] = np.random.choice(4, p=transition_matrix[state[i]])
    states.append(state.copy())  # Store the state

# Convert the states to a DataFrame and save to a CSV file
df = pd.DataFrame(states)
df.to_csv('statese.csv', index=False)
