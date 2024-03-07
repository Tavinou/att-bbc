<<<<<<< HEAD
import math
lado = float(input("comprimento do lado:"))
num = int(input("número de lados:"))

area = (num* lado**2)/(4*math.tan(math.pi/num))

=======
import math
lado = float(input("comprimento do lado:"))
num = int(input("número de lados:"))

area = (num* lado**2)/(4*math.tan(math.pi/num))

>>>>>>> ce58a64bc5cccad4fb228b3c9f623a9eff247397
print(f"A area do polígono regular{area:.2f}")