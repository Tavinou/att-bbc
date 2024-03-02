import math
pnt1lat = float(input("latitude do ponto 1:"))
pnt1lon = float(input("longitude do ponto 1:"))
pnt2lat = float(input("latitude do ponto 2:"))
pnt2lon = float(input("longitude do ponto 2:"))

pnt1lat = math.radians(pnt1lat)
pnt1lon = math.radians(pnt1lon)
pnt2lat = math.radians(pnt2lat)
pnt2lon = math.radians(pnt2lon)

dlat = pnt1lat - pnt2lat
dlon = pnt1lon - pnt2lon

h = math.sin(dlat/2)**2 + math.cos(pnt1lat) * math.cos(pnt2lat) * math.sin(dlon / 2)**2
c = 2* math.atan2(math.sqrt(h), math.sqrt(1 - h))
distancia = 6371.01 * c

print(f"A distâmcia entre os dois pontos é {distancia:.2f}km")