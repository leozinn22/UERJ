def mdc(a,b):
    a=abs(a)
    b=abs(b)
    if(a==0 and b ==0):
        raise ValueError("A e B não podem ser iguais a 0")
    if (isinstance(a,int)==False or isinstance(b,int)==False):
        raise ValueError("A e B não podem ser diferentes de um número inteiro")
    if(a !=0 and b ==0):
        return a
    elif(a ==0 and b !=0):
        return b
    m=a//b
    conc = (a-m*b)
    while conc != 0:
        m=a//b
        conc = (a-m*b)
        a=b
        b=conc
    return a
numeros=[0,0]
numeros[0]=int(input("Digite o valor de A: "))
numeros[1]=int(input("Digite o valor de B: "))
print("O mdc é: "+str(mdc(numeros[0],numeros[1])))