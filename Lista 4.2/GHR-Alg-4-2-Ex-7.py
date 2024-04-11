
pi_aproximado = 0
for n in range(1, 15 + 1):
    termo = (-1) ** (n - 1) / (2 * n - 1)
    pi_aproximado += 4 * termo
print(f"Aproximação {n}: {pi_aproximado}")

