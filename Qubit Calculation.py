 Qubit Probability Calculation

import math

 Input amplitudes
alpha = float(input("Enter amplitude alpha (for |0>): "))
beta = float(input("Enter amplitude beta (for |1>): "))
Calculate probabilities
P0 = alpha ** 2
P1 = beta ** 2

 Normalization check
total = P0 + P1

print("\n--- Qubit Calculation ---")
print("Amplitude alpha =", alpha)
print("Amplitude beta  =", beta)

print("Probability of |0> =", round(P0, 4))
print("Probability of |1> =", round(P1, 4))
print("Sum of probabilities =", round(total, 4))

if math.isclose(total, 1.0):
    print("The qubit is normalized.")
else:
    print("The qubit is not normalized.")
