import qiskit as q
import qiskit.quantum_info as qi
from qiskit import QuantumCircuit
import matplotlib.pyplot as plt
import numpy as np

simulator = q.Aer.get_backend('qasm_simulator')

alpha = 1/2
beta = (np.sqrt(3)/2)*1j
initial_state = [alpha, beta]
initial_qubit = q.extensions.Initialize(initial_state)

matrix = [[0.5+0.5j, 0.5-0.5j],
          [0.5-0.5j, 0.5+0.5j]]

sqrt_not = qi.Operator(matrix)


circuit = QuantumCircuit(1, 1)

circuit.append(initial_qubit, [0])
circuit.unitary(sqrt_not, 0, label='sqrt(not)')

circuit.measure(0, 0)

print(circuit.draw(output='text'))

job = q.execute(circuit, simulator, shots=1000000)

result = job.result()

counts = result.get_counts(circuit)
print("0/1", counts)

q.visualization.plot_histogram(counts)
plt.show()
