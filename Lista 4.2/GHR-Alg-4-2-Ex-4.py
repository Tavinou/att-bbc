dist = 0
import math
cont = 0
xn2 = 0
yn2 = 0
while True:
    if cont==0:
        xn1 = int(input("Digite a coordenada x de um ponto:"))
        yn1 = int(input("Digite a coordenada y de um ponto:"))
        xn1 = xn2
        yn2 = yn2
    if cont>1:
        xn = input("Digite a coordenada x de um ponto (enter para sair):")   
        if xn=="":
            d = math.sqrt(((xn1-xn2)**2)+((yn-yn1)**2))
            dist+=d
            break
        yn = int(int(input("Digite a coordenada y de um ponto:")))    
        xn = int(xn)
        d = math.sqrt(((xn2-xn)**2)+((yn-yn2)**2))
        xn2 = xn
        yn2 = yn
        dist+=d
    cont +=1

print("o perimetro deste poligono é igaul a:",dist)