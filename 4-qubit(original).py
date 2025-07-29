from qiskit import QuantumCircuit, transpile
from qiskit_aer import Aer
from qiskit.visualization import plot_bloch_multivector, plot_histogram
import matplotlib.pyplot as plt
import numpy as np

# Step 1: Create a 4-qubit circuit
qc = QuantumCircuit(4)

# Step 2: Simulate electron sharing (covalent bonds)
qc.h(0)
qc.cx(0, 1)
qc.cx(1, 2)
qc.cx(2, 3)

# (Optional) print circuit
print(qc)

# Step 3: Transpile for statevector simulator & run
backend_sv = Aer.get_backend('statevector_simulator')
qc_sv = transpile(qc, backend_sv)
job_sv = backend_sv.run(qc_sv)
statevector = job_sv.result().get_statevector()

# Step 4: Visualize Bloch spheres
plot_bloch_multivector(statevector)
plt.show()  # Shows the Bloch spheres

print("Quantum statevector of your 4-atom lattice:\n", statevector)

# Step 5: Add measurement to all qubits for histogram
qc.measure_all()

# Step 6: Transpile & run on qasm simulator for measurements
backend_qasm = Aer.get_backend('qasm_simulator')
qc_qasm = transpile(qc, backend_qasm)
job_qasm = backend_qasm.run(qc_qasm, shots=1000)
counts = job_qasm.result().get_counts()

# Step 7: Plot measurement histogram
plot_histogram(counts)
plt.show()  # Shows the histogram