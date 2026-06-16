# Quantum Computing

A personal learning repository for exploring Quantum Computing concepts using two languages:
- **Q#** (Q Sharp) — Microsoft's domain-specific language for quantum programming
- **Python** — using NumPy for simulating quantum states and operations

## Purpose

This repository is built for learning purposes. It covers fundamental quantum computing concepts through hands-on programs, from basic qubit operations to well-known quantum protocols, implemented in both Q# and Python.

## Repository Structure

```
Basics_of_Quantum_Computing_QSharp/
├── Basic_DumpMachine.qs         # Inspecting qubit states using DumpMachine
├── Bell_State.qs                # Creating entangled Bell states
├── Multiple_Qubits.qs           # Working with multi-qubit systems
├── Quantum_Teleportation.qs     # Quantum teleportation protocol
├── Random_Number.qs             # Quantum random number generation
├── Skwed_randombit_generator.qs # Skewed/biased random bit generation
└── main.qs                      # Entry point

Basics_of_Quantum_Computing_Python/
├── Representation_and_Measuring_Qubit.py  # Qubit states, superposition, and measurement probabilities
├── Building_Multi_Qubit_State.py          # Tensor products, multi-qubit states, and Bell states
├── Gates_as_Matrices.py                   # Quantum gates represented as NumPy matrices
├── Qubit_Circuits.py                      # Building and simulating simple qubit circuits
├── Bell_State.py                          # Constructing Bell states using H gate and CNOT
└── Measuring_with_Shot.py                 # Simulating measurement shots and computing expectation values
```

## Topics Covered

- Qubit initialization and measurement
- Superposition and quantum gates
- Quantum entanglement (Bell states)
- Multi-qubit operations and tensor products
- Quantum teleportation
- Quantum randomness

## Prerequisites

### For Q# programs
- [.NET SDK](https://dotnet.microsoft.com/download)
- [Microsoft Quantum Development Kit (QDK)](https://learn.microsoft.com/en-us/azure/quantum/install-overview-qdk)

### For Python programs
- Python 3.9+
- NumPy (`pip install numpy`)

## Getting Started

**Clone the repo:**
```bash
git clone https://github.com/Omkyao1998/Quantum_Computing.git
cd Quantum_Computing
```

**Run a Q# program:**
```bash
cd Basics_of_Quantum_Computing_QSharp
dotnet run
```

**Run a Python program:**
```bash
cd Basics_of_Quantum_Computing_Python
python3 Representation_and_Measuring_Qubit.py
```

## Languages

| Language | Purpose |
|----------|---------|
| **Q#** | Quantum hardware-level programming via Microsoft QDK |
| **Python + NumPy** | Simulating quantum states and operations classically |

---

*This is a learning project. Contributions and suggestions are welcome.*
