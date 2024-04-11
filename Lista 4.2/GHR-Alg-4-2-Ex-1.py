cont = 0
soma = 0
while True:
    n = int(input("digite o numero para fazer a media e 0 para parar:"))
    if n>0:
        soma +=n
        cont+=1 
    elif n==cont:
        print("erro primeiro valor 0")
        break
    elif n==0:
        print(f"a média é {soma/cont}")
        break
