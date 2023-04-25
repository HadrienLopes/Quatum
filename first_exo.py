import qiskit as q
import matplotlib.pyplot as plt

simulator = q.Aer.get_backend('qasm_simulator')

circuit = q.QuantumCircuit(1, 1)

circuit.x(0)
circuit.h(0)
circuit.h(0)

circuit.measure(0, 0)

print(circuit.draw(output='text'))

job = q.execute(circuit, simulator, shots=1000)

result = job.result()

counts = result.get_counts(circuit)
print("0/1", counts)

q.visualization.plot_histogram(counts)
plt.show()
