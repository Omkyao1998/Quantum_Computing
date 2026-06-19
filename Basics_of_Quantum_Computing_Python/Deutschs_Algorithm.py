import numpy as np

ket0 = np.array([1,0], dtype=complex)
ket1 = np.array([0,1],dtype=complex)

H = (1/np.sqrt(2)) * np.array([[1, 1], [1, -1]], dtype=complex)
I = np.eye(2, dtype=complex)
CNOT = np.array([[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]], dtype=complex)

state = np.kron(ket0, ket1)  # inputs: top |0>, ancilla |1>  -> |01>
state = np.kron(H, H) @ state   # Step 1: spread  -> |+>|->
state = CNOT @ state            # Step 2: ONE oracle call (f(x)=x, balanced)
state = np.kron(H, I) @ state   # Step 3: H on top qubit only

probs = np.abs(state)**2                  # over |00>,|01>,|10>,|11>
p_top0 = (probs[0] + probs[1]).real       # top qubit reads 0
p_top1 = (probs[2] + probs[3]).real       # top qubit reads 1
print("P(top=0):", round(p_top0,3), " P(top=1):", round(p_top1,3))
# -> P(top=1) = 1.0  =>  BALANCED, found in ONE oracle call