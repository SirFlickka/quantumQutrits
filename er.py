# Import necessary libraries
import numpy as np
import pandas as pd
from qiskit import QuantumCircuit, Aer, transpile, assemble

qc = QuantumCircuit(192)
qc.h(191)
qc.draw()

qc.draw(output='mpl', filename='my_circuit.png')
print(qc)