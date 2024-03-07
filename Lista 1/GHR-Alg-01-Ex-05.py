qnt1 = int(input("digite a quantidade de vasilhames de 1 litro ou menos: "))
qnt2 = int(input("digite a quantidade de vasilhames de mais de 1 litro: "))
precoqnt1 = qnt1 * 0.10
precoqnt2 = qnt2 *0.25

print(f"tem {(precoqnt1+precoqnt2):.2f}")