pais_a = 80000
pais_b = 200000
anos = 0

while pais_a < pais_b:
    pais_a += pais_a * (0.03)
    pais_b += pais_b * (1.5)
    anos += 1

print(f"{a:.2f}")
print(anos)