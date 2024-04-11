preco = 0
while True:
    idade = input("digite a idade (enter para parar) ")
    if idade=="":
        break
    idade = int(idade)
    if idade<=12 and idade>=3:
        preco+=14
    elif idade>=65:
        preco+=18
    else:
        preco+=23  
print(f"{preco:.2f}R$")