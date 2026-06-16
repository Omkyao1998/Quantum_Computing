import numpy as np 

#Bell State
bell_state = np.array([1, 0, 0, 1], dtype=complex)/np.sqrt(2)
probs = np.abs(bell_state)**2

#Simulate 1000 shots = sample outcomes from distribution
outcomes = ['00', '01', '10', '11']
samples = np.random.choice(outcomes, size=1000, p=probs)

#Tally the counts
unique,counts = np.unique(samples, return_counts=True)
print(dict(zip(unique, counts))) # Output will show counts for '00' and '11' close to 500 each, and '01' and '10' close to 0, reflecting the Bell state probabilities. e.g. {'00': 507, '11': 493}

# Expectation value <Z> on qubit 0:  +1 if q0==0, -1 if q0==1
z0 = np.where(np.char.startswith(samples, '0'), 1, -1)
print("<Z0> estimate:", round(z0.mean(), 3))   # ~ 0.0  (q0 is 50/50)