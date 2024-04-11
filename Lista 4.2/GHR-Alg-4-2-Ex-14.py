bit = str(input("digite os bit em binario:"))
qntbit = len(bit)
listade=[]
listab=[]
for i in range(0,qntbit):
    listade.append(2**i)
contrario = listade[::-1]
for i in (bit):
    listab.append(i)


for i in range(qntbit):
    if listab[i]=="0":
        pos = contrario[i]
        contrario[i]=0
soma = 0
for i in contrario:
    soma+=i
print("decimal",soma)