while True:
    bits = input("digite a sequencia de 8 bits:")
    lbits = list(bits)
    um = lbits.count("1")
    zero = lbits.count("0")
    if bits=="":
        break
    if len(bits)!=8:
        print("ERRO n tem 8 caracteres")
    elif um+zero!=8:
        print("digite só 0 e 1")
    elif um%2==0:
        print("paridade par")
    elif um%2!=0:
        print("paridade impar")