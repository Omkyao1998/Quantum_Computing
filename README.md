# Quantum Computing

A personal learning repository for exploring Quantum Computing concepts using **Q#** (Q Sharp) — Microsoft's domain-specific language for quantum programming.

## Purpose

This repository is built for learning purposes. It covers fundamental quantum computing concepts through hands-on Q# programs, from basic qubit operations to well-known quantum protocols.

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
```

## Topics Covered

- Qubit initialization and measurement
- Superposition and quantum gates
- Quantum entanglement (Bell states)
- Multi-qubit operations
- Quantum teleportation
- Quantum randomness

## Prerequisites

- [.NET SDK](https://dotnet.microsoft.com/download)
- [Microsoft Quantum Development Kit (QDK)](https://learn.microsoft.com/en-us/azure/quantum/install-overview-qdk)

## Getting Started

Clone the repo and run any `.qs` file using the QDK:

```bash
git clone https://github.com/Omkyao1998/Quantum_Computing.git
cd Quantum_Computing/Basics_of_Quantum_Computing_QSharp
dotnet run
```

## Language

All programs are written in **Q#** — a language designed by Microsoft specifically for expressing quantum algorithms.

---

*This is a learning project. Contributions and suggestions are welcome.*
