suco = int(input("quantos sucos?"))
prato =int(input("quantos pratos?"))
sobremesa =int(input("quantas sobremesa?"))
#tirar o preço de cada produto
suco = suco *2
prato = prato *10
sobremesa = sobremesa *1

valor = (suco + prato + sobremesa) #pegar valor
taxa = valor * 0.10 #ver quanto fica a taxa de 10%
valor = valor + taxa #soma valor e taxa
print(f"o valor foi {(valor):.2f}")
