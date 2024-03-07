import math
lado1 = float(input("lado 1:"))
lado2 = float(input("lado 2:"))
lado3 = float(input("lado 3:"))

l = (lado1+lado2+lado3) / 2

area = math.sqrt(l*((l-lado1)*(l-lado2)*(l-lado3)))
print(f"area do triângulo:{area:.2f}")