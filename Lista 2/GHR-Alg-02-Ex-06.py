<<<<<<< HEAD
numero = int(input("digite um numero com 4 digitos:"))
m = numero//1000
numero -= m*1000
c = numero//100
numero -= c*100
d = numero//10
numero -= d*10
soma= m+c+d+numero
=======
numero = int(input("digite um numero com 4 digitos:"))
m = numero//1000
numero -= m*1000
c = numero//100
numero -= c*100
d = numero//10
numero -= d*10
soma= m+c+d+numero
>>>>>>> ce58a64bc5cccad4fb228b3c9f623a9eff247397
print(f"a soma: {soma} {m,+c,d,numero}")