import numpy as np
import pandas as pd
from qiskit import QuantumCircuit, Aer, transpile

# Define the quantum circuit
qc = QuantumCircuit(192, 192)
qc.h(range(192))
qc.measure(range(192), range(192))

# Simulate the circuit
simulator = Aer.get_backend('qasm_simulator')
tc = transpile(qc, simulator)
result = simulator.run(tc, shots=100).result()

# Convert the result to a DataFrame
counts = result.get_counts()
df = pd.DataFrame([{"state": state, "counts": counts} for state, counts in counts.items()])

# Set up the initial state (all zeros)
initial_state = np.zeros(192, dtype=int)

# Set up the state transition matrix
transition_matrix = np.array([[0.25, 0.25, 0.25, 0.25]] * 4)

# Perform the simulation
state = initial_state
states = []  # List to store the states
for _ in range(100):  # however many steps you want
    for i in range(192):
        state[i] = np.random.choice(4, p=transition_matrix[state[i]])
    states.append(state.copy())  # Store the state

# Convert the states to a DataFrame and append to the previous DataFrame
states_df = pd.DataFrame(states)
df = df.append(states_df)

# Sort the DataFrame and remove duplicates
df = df.sort_values(by=list(df.columns))
df = df.drop_duplicates()

# Define a categorization function
def categorize(row):
    total = row.sum()
    if total < 50:
        return 'Low'
    elif total < 100:
        return 'Medium'
    elif total < 350:
        return 'High'
    else:
        return 'Over'

# Apply the function to each row
df['Category'] = df.apply(categorize, axis=1)

# Save the DataFrame to a .csv file
df.to_csv('integrated_results.csv', index=False)
