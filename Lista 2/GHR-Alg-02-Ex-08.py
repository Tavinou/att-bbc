n = int(input("numero inteiro de 3 algarismo:"))
c = n//100 #acha a centena q já vira unidade
n = n%100 #pego oq sobrou
d = n//10 #acha dezena
n -= (d * 10) #acha unidade
d = d*10 #transforma em dezena
n = n *100 # transforma em centena
print(n+d+c)
