n = int(input("numero inteiro de 3 algarismo:"))
c = n//100
n = n%100
d = n//10
n -= (d * 10)
print(f"centenas: {c}\ndezenas: {d}\nunidade: {n}")