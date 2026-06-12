import numpy as np  # type: ignore

#Basic states 
ket0 = np.array([1, 0], dtype=complex) #|0⟩
ket1 = np.array([0, 1], dtype=complex) #|1⟩

#Build the superposition state |+⟩
alpha = 1/np.sqrt(2) #Coefficient for |0⟩
beta = 1/np.sqrt(2) #Coefficient for |1⟩
psi = alpha * ket0 + beta * ket1 #|ψ⟩ = α|0⟩ + β|1⟩ #the state vector [α, β]

#Validation for <psi|psi> = 1
#np.vdot conjugates the FIRST argument -> exactly the bra-ket inner product
norm = np.vdot(psi, psi).real
print("Norm <psi|psi>:", round(norm, 6))        # 1.0  -> valid state

#Measurement probabilities
p0,p1 = abs(alpha)**2, abs(beta)**2
print("P(0):", p0, " P(1):", p1)                 # 0.5  0.5

#Simulate 1000 measurements
shots = np.random.choice([0, 1], size=1000, p=[p0, p1])
print("Counts [n0, n1]:", np.bincount(shots))    # ~ [500, 500]