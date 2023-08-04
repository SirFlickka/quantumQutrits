from qiskit import QuantumCircuit, transpile, assemble, Aer, execute
from qiskit.visualization import plot_histogram

# Create a quantum circuit with 2 qubits
qc = QuantumCircuit(2)

# Apply a Hadamard gate to the first qubit
qc.h(0)

# Apply a CNOT gate with the first qubit as control and the second as target
qc.cx(0, 1)

# Use the statevector_simulator
simulator = Aer.get_backend('statevector_simulator')

# Execute the circuit on the simulator
job = execute(qc, simulator)

# Get the result
result = job.result()

# Get the statevector
statevector = result.get_statevector()
print("\nStatevector is:",statevector)
