n=int(input("digite o numero para fazer fatoração:"))
fator = 2
fatoração =[]
if n<2:
    print("erro numero menor que 2")
else:
    while fator<=n:
        if n%fator==0:
            fatoração.append(fator)
            n= n//fator    
        else:
            fator+=1

print(fatoração)