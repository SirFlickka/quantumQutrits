# Suppose we have a large state vector
state_vector = np.random.rand(1000) + 1j * np.random.rand(1000)

# We're only interested in states with amplitude greater than a threshold
threshold = 0.1

# Find the indices of the relevant states
relevant_indices = np.where(np.abs(state_vector) > threshold)[0]

# Save the relevant states and their indices
with open('relevant_quantum_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    for index in relevant_indices:
        writer.writerow([index, state_vector[index].real, state_vector[index].imag])
