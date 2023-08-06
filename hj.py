# Import necessary libraries
import pandas as pd
from qiskit import QuantumCircuit, Aer, transpile, assemble

# Define the quantum circuit
qc = QuantumCircuit(64, 64)
for i in range(64):
    qc.h(i)
qc.measure(range(64), range(64))

# Simulate the circuit
simulator = Aer.get_backend('qasm_simulator')
tc = transpile(qc, simulator)
qobj = assemble(tc, shots=100)
result = simulator.run(qobj).result()

# Convert the result to a DataFrame
counts = result.get_counts()
df = pd.DataFrame([{"state": state, "counts": count} for state, count in counts.items()])

# Define your quadrant_number function
def quadrant_number(n):
    pass  # Your quadrant_number function code here

# Define the mapping from quadrants to binary states
quadrant_states = {
    'even2,4': '00',
    'even6,8': '01',
    'odd0,5': '10',
    'odd1,3,7,9': '11'
}

# Convert each state to a number (taking the first 10 bits as an example)
df['Number'] = df['state'].apply(lambda x: int(x[:10], 2))

# Classify each number into a quadrant
df['Quadrant'] = df['Number'].apply(quadrant_number)

# Map the quadrant to a binary state
df['Quadrant State'] = df['Quadrant'].apply(lambda x: quadrant_states.get(x, 'Unknown'))

print(df)

# Save the DataFrame to a .csv file
df.to_csv('quantum_resulta.csv', index=False)
