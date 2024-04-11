msm=str(input("digite a palavra para codificar:"))
rotacao =int(input("digite o numero da rotação:"))
pa=""
if rotacao>0:
    while rotacao>26:
        rotacao-=26
elif rotacao<0:
    while rotacao<-26:
        rotacao+=26
for i in msm:
    i =ord(i)
    if i>=65 and i<=90:
        if i+rotacao>90:
            i= (i-26)+rotacao
            i=chr(i)
            pa+=i
        elif i+rotacao<65:
            i=(i+26)+rotacao
            i=chr(i)
            pa+=i
        else:
            i+=rotacao
            i=chr(i)
            pa+=i
    elif i>=97 and i<=122:
        if i+rotacao>122:
            i= (i-26)+rotacao
            i=chr(i)
            pa+=i
        elif i+rotacao<97:
            i=(i+26)+rotacao
            i=chr(i)
            pa+=i
        else:
            i+=rotacao
            i=chr(i)
            pa+=i
    else:
        i=chr(i)
        pa+=i
print(f"mensagem:{msm}\ncriptocrafada:{pa}")