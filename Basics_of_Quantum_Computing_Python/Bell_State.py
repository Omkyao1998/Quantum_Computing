import numpy as np 

ket0 = np.array([1, 0], dtype=complex)
H = (1/np.sqrt(2)) * np.array([[1, 1], [1, -1]], dtype=complex)
I = np.eye(2, dtype=complex)
CNOT = np.array([[1,0,0,0],
                 [0,1,0,0],
                 [0,0,0,1],
                 [0,0,1,0]], dtype=complex)

state = np.kron(ket0, ket0) # |00>  ->  [1,0,0,0]

#Step 1: Apply H to the first qubit, H on qubit 0, nothing on qubit 1  ->  apply (H ⊗ I)
state = np.kron(H, I) @ state  # (|00> + |10>)/sqrt(2)

# Step 2: CNOT entangles them
state = CNOT @ state               # (|00> + |11>)/sqrt(2)  = Bell state
print(np.round(state.real, 3))     # [0.707, 0, 0, 0.707]
print("P:", np.round(np.abs(state)**2, 3))   # [0.5, 0, 0, 0.5]