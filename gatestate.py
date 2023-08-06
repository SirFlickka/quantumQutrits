import csv
from qiskit import QuantumCircuit, transpile, assemble, Aer, execute

# Define the backend
simulator = Aer.get_backend('qasm_simulator')

# Define the gate sequences
gate_sequences = ['h', 's', 't', 'x', 'y', 'z', 'rx', 'ry', 'rz']

# Initialize a dictionary to store the results
results = {}

# Loop through the gate sequences
for gate_sequence in gate_sequences:
    # Create a quantum circuit with one qubit
    qc = QuantumCircuit(1)
    
    # Apply the gates
    for gate in gate_sequence:
        if gate == 'h':
            qc.h(0)
        elif gate == 's':
            qc.s(0)
        elif gate == 't':
            qc.t(0)
        elif gate == 'x':
            qc.x(0)
        elif gate == 'y':
            qc.y(0)
        elif gate == 'z':
            qc.z(0)
        elif gate == 'rx':
            qc.rx(1.5708, 0)
        elif gate == 'ry':
            qc.ry(1.5708, 0)
        elif gate == 'rz':
            qc.rz(1.5708, 0)
    
    # Simulate the circuit
    job = execute(qc, simulator, shots=18889465)
    
    # Get the results
    result = job.result()
    
    # Get the counts
    counts = result.get_counts(qc)
    
    # Store the results
    results[gate_sequence] = counts

# Write the results to a CSV file
with open('gate_results.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['Gate Sequence', 'Resulting State'])
    for gate_sequence, counts in results.items():
        writer.writerow([gate_sequence, counts])
