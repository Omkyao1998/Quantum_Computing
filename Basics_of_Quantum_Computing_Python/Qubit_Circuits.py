#A circuit is product of unitary gates, applied in REVERSE order of how they appear in the diagram.
import numpy as np

ket0 = np.array([1, 0], dtype=complex)
H = (1/np.sqrt(2)) * np.array([[1, 1], [1, -1]], dtype=complex)
Z = np.array([[1, 0], [0, -1]], dtype=complex)

# Circuit drawn as:  |0> --[H]--[Z]--   (H first, then Z)
# REVERSE the order when multiplying matrices:
circuit_U = Z @ H            # correct:  Z·H   (NOT  H @ Z)
out = circuit_U @ ket0
print(np.round(out.real, 3)) # [ 0.707, -0.707 ]  = |->