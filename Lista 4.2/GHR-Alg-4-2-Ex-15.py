dec =int(input("decimal:"))
resul =""
q = dec

while True:
    r=q%2
    r = str(r)
    resul+=r
    q= q//2
    if q==0:
        break
print(''.join(reversed(resul)))