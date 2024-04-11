
msm = str(input("digite a frase:"))
msmno = ""
for i in msm:
    if i!=" " and i!="." and i!="," and i!="?" and i!="!":
        msmno+=i
msmno = msmno.lower()
if "".join(reversed(msmno))==msmno:
    print("A frase é palíndromos")
else:
    print("não é palindromos")