moeda = (int(input("Digite a quantidade de centavos de 0 a 99:\n")))

cent50 = moeda//50
moeda -= cent50*50
cent25 = moeda//25
moeda -= cent25*25
cent10 = moeda//10
moeda -= cent10*10
cent5 = moeda//5
moeda -= cent5*5


print(f"quantidade de moedas de 50:{cent50}")
print(f"quantidade de moedas de 25:{cent25}")
print(f"quantidade de moedas de 10:{cent10}")
print(f"quantidade de moedas de 5:{cent5}")
print(f"quantidade de moedas de 1:{moeda}")
