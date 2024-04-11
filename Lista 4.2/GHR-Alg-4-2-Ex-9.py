x = int(input("digite o numero para saber a raiz:"))
raiz = x/2
while abs((raiz*raiz) -x)>(10**-4):
    raiz= ((raiz+(x/raiz)) /2)
print(raiz)
