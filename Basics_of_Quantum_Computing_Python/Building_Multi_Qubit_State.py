import numpy as np

#Basic states
ket0 = np.array([1, 0], dtype=complex) #|0�
ket1 = np.array([0, 1], dtype=complex) #|1�

#Calculating the tensor product = Kronecker product
ket00 = np.kron(ket0, ket0)     #|00⟩ -> [1,0,0,0]
ket01 = np.kron(ket0, ket1)     #|01⟩ -> [0,1,0,0] (order matters)
ket10 = np.kron(ket1, ket0)     #|10⟩ -> [0,0,1,0] (order matters)
ket11 = np.kron(ket1, ket1)     #|11⟩ -> [0,0,0,1]

print("ket00:|00⟩", ket00)
print("ket01:|01⟩", ket01)
print("ket10:|10⟩", ket10)
print("ket11:|11⟩", ket11)

#Building the Bell State |Φ+⟩ = (|00⟩ + |11⟩)/√2 - an entangled state
bell_state = (np.kron(ket0, ket0) + np.kron(ket1, ket1)) / np.sqrt(2)
print("Bell State |Φ+⟩:", np.round(bell_state.real, 3)) # [0.70710678, 0, 0, 0.70710678]

#Validation of the one rule
print("Norm <Φ+|Φ+>:", round(np.vdot(bell_state, bell_state).real, 6)) # 1.0 -> valid state

#Probabilities of measuring |00⟩, |01⟩, |10⟩, |11⟩
probs = np.abs(bell_state)**2
print("P(00,01,10,11):", np.round(probs.real, 3))    # [0.5, 0, 0, 0.5]

