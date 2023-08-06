# Importing necessary functions
import json
from qiskit import QuantumCircuit, transpile, assemble, Aer, execute
from qiskit.visualization import plot_bloch_multivector, plot_histogram

# Create a quantum circuit with two qubits
qc = QuantumCircuit(316)
for i in range(316):
    qc.h(i)

# Apply Hadamard gate on each qubit
for i in range(316):
    qc.h(i)

# Now apply a CNOT gate
# qc.cx(0, 1)

# Visualize the circuit
print(qc)

# Now, let's simulate this circuit

# Use Aer's qasm_simulator
simulator = Aer.get_backend('qasm_simulator')

# Execute the circuit on the qasm simulator
job = execute(qc, simulator, shots=100000)

# Grab results from the job
result = job.result()

# Returns counts
counts = result.get_counts(qc)
print("\nTotal count for 00 and 11 are:",counts)

# Convert the counts to JSON
counts_json = json.dumps(counts)
print("\nCounts in JSON format:", counts_json)

# If you want to save it to a file
with open('resultsd.json', 'w') as f:
    json.dump(counts, f)
