pa = str(input("digite a palavra:"))
pal= ""
for i in list(pa):
    pal = pal+i

if ''.join(reversed(pal))==pa:
    print("palíndromo")
else:
    print("não é palíndromo")
