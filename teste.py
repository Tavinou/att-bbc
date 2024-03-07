import math
import sys

entrada1 = sys.stdin.readline()

parte1 = entrada1.split(" ")
a = float(parte1[0])
b = float(parte1[1])
c = float(parte1[2])

tri = (a*c)/2
area = (3.14159 * (c**2))
trap = ((a+b)*c)/2
quad = b**2
ret = a * b

print(f"TRIANGULO: {tri:.3f}\nCIRCULO: {area:.3f}\nTRAPEZIO: {trap:.3f}\nQUADRADO {quad:.3f}\nRETANGULO: {ret:.3f}")