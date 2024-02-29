suco = int(input("quantos sucos?"))
prato =int(input("quantos pratos"))
sobremesa =int(input("quantas sobremesa"))

suco = suco *2
prato = prato *10
sobremesa = sobremesa *1

valor = (suco + prato + sobremesa)
taxa = valor * 0.10
valor = valor + taxa 
print(valor)
