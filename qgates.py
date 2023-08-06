import itertools
import numpy as np
import json
from qiskit import QuantumCircuit, execute, Aer

# The gates we will be using, without the rotation gates
gates = ['h', 'x', 'y', 'z', 's', 't']

# We will discretize the parameter space of the rotation gates into 10 steps
rotation_steps = np.linspace(0, 2*np.pi, 10)

# Create a list to store all possible gate sequences
gate_sequences = []

# Generate all possible combinations of the non-rotation gates
for r in range(1, len(gates) + 1):
    for gate_sequence in itertools.combinations(gates, r):
        gate_sequences.append(gate_sequence)

# Add the rotation gates to the gate sequences
for r in range(1, len(rotation_steps) + 1):
    for rotation_sequence in itertools.combinations(rotation_steps, r):
        gate_sequences.append(('rx', rotation_sequence))
        gate_sequences.append(('ry', rotation_sequence))
        gate_sequences.append(('rz', rotation_sequence))

# Create a quantum circuit with a single qubit
qc = QuantumCircuit(1)

# Dictionary to store results
results = {}

# Iterate over all possible gate sequences
for gate_sequence in gate_sequences:
    # Reset the circuit
    qc.reset(0)
    # Apply each gate in the sequence
    for gate in gate_sequence:
        if isinstance(gate, tuple):
            # If the gate is a rotation gate, apply it with the specified parameters
            getattr(qc, gate[0])(gate[1], 0)
        else:
            # Otherwise, just apply the gate
            getattr(qc, gate)(0)
    # Simulate the circuit and print the result
    result = execute(qc, Aer.get_backend('statevector_simulator')).result()
    statevector = result.get_statevector()
    
    # Add results to dictionary
    results[str(gate_sequence)] = statevector.tolist()

# Save results to a JSON file
with open('quantum_states.json', 'w') as f:
    json.dump(results, f)
