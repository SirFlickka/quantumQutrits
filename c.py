import numpy as np

# A complex quantum state vector
quantum_data = np.array([1+1j, 0, 0, 1-1j])

# Get the real and imaginary parts
real_part = np.real(quantum_data)
imag_part = np.imag(quantum_data)

print("Real part:", real_part)
print("Imaginary part:", imag_part)
