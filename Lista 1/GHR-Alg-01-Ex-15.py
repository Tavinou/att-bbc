import math
lado = float(input("comprimento do lado:"))
num = int(input("número de lados:"))

area = (num* lado**2)/(4*math.tan(math.pi/num))

print(f"A area do polígono regular{area:.2f}")