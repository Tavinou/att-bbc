import math
unidade = input("digite unidade de medida (ex m):")
raio = float(input("digite o raio:"))

area = math.pi * raio**2
volume = (4/3) * math.pi * raio**3

print(f"area do circulo é {area:.2f}{unidade}²")
print(f"area do circulo é {volume:.2f}{unidade}³")