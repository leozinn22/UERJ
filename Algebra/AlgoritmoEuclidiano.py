def euclidiano(a,b):
    a=abs(a)
    b=abs(b)
    if(a==0 and b ==0):
        raise ValueError("A e B não podem ser iguais a 0")
    if (isinstance(a,int)==False or isinstance(b,int)==False):
        raise ValueError("A e B não pode ser diferentes de um número inteiro")
    if(a !=0 and b ==0):
        return a
    elif(a ==0 and b !=0):
        return b
    quocientes=a//b
    conc = (a-quocientes*b)
    XandY = [[1,0],[0,1]]
    while conc != 0:
        quocientes=a//b
        conc = (a-quocientes*b)
        aux =[-quocientes*(XandY[1][0])+(XandY[0][0]),-quocientes*(XandY[1][1])+(XandY[0][1])]
        XandY[0]=XandY[1]
        XandY[1]=aux
        a=b
        b=conc
    return (
        a,
        XandY[0][0],
        XandY[0][1]
        )
numeros=[0,0]
numeros[0]=int(input("Digite o primeiro número: "))
numeros[1]=int(input("Digite o segundo número: "))
print("O mdc é: {}, o valor de x é: {}, o valor de y é: {}".format(*euclidiano(numeros[0],numeros[1])))


