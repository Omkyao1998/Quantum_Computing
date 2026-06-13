import numpy as np 

#Basic states
ket0 = np.array([1, 0], dtype=complex) #|0�

X = np.array([[0, 1], [1, 0]], dtype=complex) #X(NOT) gate
Z = np.array([[1, 0], [0, -1]], dtype=complex) #Z(Phase flip) gate 
H = (1/np.sqrt(2)) * np.array([[1, 1], [1, -1]], dtype=complex) #Hadamard gate

# Apply a gate = matrix @ state  (note the order: U @ state, not state @ U)
print("X|0>:", (X @ ket0).real)              # [0,1] = |1>
print("H|0>:", np.round((H @ ket0).real, 3)) # [0.707, 0.707] = |+>

# A gate is legal only if it's unitary: U† U = I
def is_unitary(U):
    return np.allclose(U.conj().T @ U, np.eye(len(U)))

print("X unitary?", is_unitary(X))           # True
print("H unitary?", is_unitary(H))           # True

# Hadamard is its own inverse: applying it twice returns the original
print("H@H = I?", np.allclose(H @ H, np.eye(2)))   # True

# Eigenvalues of Z = the possible computational-basis measurement outcomes
vals, _ = np.linalg.eig(Z)
print("Z eigenvalues:", vals.real)           # [1, -1]

A = np.array([[1,1],[0,1]])
print("A",is_unitary(A))