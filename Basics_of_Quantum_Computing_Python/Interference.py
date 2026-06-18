import numpy as np

H = (1/np.sqrt(2)) * np.array([[1, 1], [1, -1]], dtype=complex)
ket0 = np.array([1, 0], dtype=complex) 

once  = H @ ket0 # |+> : an even superposition
twice = H @ (H @ ket0) # back to |0> !

print("after 1 H:", np.round(once.real, 3))    # [0.707, 0.707]
print("after 2 H:", np.round(twice.real, 3))   # [1. 0.]  -> |0>
print("H@H = I? ", np.allclose(H @ H, np.eye(2)))  # True