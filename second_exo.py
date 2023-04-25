import qiskit as q
import matplotlib.pyplot as plt
import numpy as np

simulator = q.Aer.get_backend('statevector_simulator')

circuit = q.QuantumCircuit(1)

alpha0 = np.sqrt(3)/2
beta0 = (1-1j)/(2*np.sqrt(2))
norme = np.sqrt(abs(alpha0)**2 + abs(beta0)**2)

print("alpha0: ", alpha0)
print("beta0: ", beta0)
print("norme: ", norme)
if (int(round(norme)) == 1):
    alpha, beta = alpha0, beta0
    print("qubit deja normalisee")
else:
    alpha, beta = alpha0/norme, beta0/norme

print("alpha: ", alpha)
print("beta: ", beta)

etat_initial = [alpha, beta]
qubit_initial = q.extensions.Initialize(etat_initial)
circuit.append(qubit_initial, [0])

circuit.h(0)
circuit.x(0)
circuit.y(0)

print(circuit.draw(output='text'))

job = q.execute(circuit, simulator)

result = job.result()

coefficients = result.get_statevector()
print("Coef_alpha:", coefficients[0])
print("Coef_beta:", coefficients[1])

