import qiskit as q
import matplotlib.pyplot as plt
import numpy as np

simulator = q.Aer.get_backend('statevector_simulator')

circuit = q.QuantumCircuit(1)

alpha0 = 3+1j
beta0 = 1-2j
norme = np.sqrt(abs(alpha0)**2 + abs(beta0)**2)
alpha, beta = alpha0/norme, beta0/norme
etat_initial = [alpha, beta]
qubit_initial = q.extensions.Initialize(etat_initial)
circuit.append(qubit_initial, [0])

circuit.x(0)

job = q.execute(circuit, simulator)

result = job.result()

coefficients = result.get_statevector()
print("Coef_alpha:", coefficients[0])
print("Coef_beta:", coefficients[1])

print(circuit.draw(output='text'))
