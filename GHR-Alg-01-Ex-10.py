import math
a = int(input("digite um valor inteiro:"))
b = int(input("digite um valor inteiro:"))

soma = a + b

diferenca = b - a

produto = a * b

quociente = a / b

resto = a % b

resultadolog = math.log10(a)

resultadoaeb = a**b

print(f"soma: {soma}")
print(f"diferença: {diferenca}")
print(f"quociente: {quociente}")
print(f"resto: {resto}")
print(f"resultado de log10a: {resultadolog}")
print(f"resultado de a^b: {resultadoaeb}")