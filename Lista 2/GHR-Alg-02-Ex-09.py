data = int(input("digite o dia em DDMMAA:"))
dia = data//10000 #acha o dia
mes = (data -(dia*10000)) //100 #tira os dia e acha os meses
ano = ((data -(dia*10000)) + (data - (mes*100))) - data #tira os anos
print(f"{ano}{mes}{dia}")