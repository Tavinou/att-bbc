import random
x = random.randrange(1,3)
cont = 1
listasorteio=[]
#1 = A cara
#2 = O coroa
a=0;o=0;n=0;soma=0
while cont<11:
    x = random.randrange(1,3)
    if x==1:
        a+=1
        n+=1
        listasorteio.append("A")
        if a>=3:
            a=0
            cont+=1
            print(listasorteio,n,"(sorteios)")
            listasorteio=[];soma+=n;n=0;o=0
    
    elif x==2:
        o+=1;n+=1
        listasorteio.append("O")
        if o>=3:
            cont+=1;o=0
            print(listasorteio,n,"(sorteios)")
            listasorteio=[];soma+=n;n=0;a=0
print(f"na média, foram necessários:{(soma/10):.1f} sorteios")