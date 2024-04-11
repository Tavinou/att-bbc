valor = 4.95
print("valor\t|\tdesconto|\t valor final")
for i in range(0,25,5):
    i += valor
    porcentagem = i*0.6
    desconto = i-porcentagem
    print(f"{i:.2f}\t|\t{porcentagem:.2f}\t|\t{desconto:.2f}")