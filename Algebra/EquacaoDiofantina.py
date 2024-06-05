def mdc(a,b):
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
def diofantinas(a:int,b:int,c:int):
    euclidiano = mdc(a,b)
    mdc1 = euclidiano[0]
    multiplo = 1
    if(c%mdc1!=0):
        raise ValueError("A e B não tem solução inteira")
    if(c !=mdc1):
        aux =0
        if(c>mdc1):
            aux = c//mdc1
        else:
            aux = mdc1//c
        if(aux!=0):
            multiplo = aux
    x_x=(euclidiano[1])*multiplo
    y_y=(euclidiano[2])*multiplo
    def prova1(x,y):
        return a*x+b*y 
    if(a<0):
        x_x=x_x*-1
    if(b<0):
        y_y=y_y*-1
    if(prova1(x_x,y_y)!=mdc1):
        raise ValueError("Erro ao gerar eq diofantinas")
    return (
            ({
                "x":x_x,"y":y_y,"multiplo":multiplo,
                "euclidiano":euclidiano,
                "resultado1":"{}*{}+{}*{}={}".format(a,x_x,b,y_y,c),
                "resultadoX":"x={}+ T *{}/{}".format(x_x,b,mdc1),
                "resultadoY":"y={}- T *{}/{}".format(y_y,a,mdc1),
            })
        )


numeros=[0,0,0]
numeros[0]=int(input("Digite o valor de A: "))
numeros[1]=int(input("Digite o valor de B: "))
numeros[2]=int(input("Digite o valor de C: "))

print(str(diofantinas(numeros[0],numeros[1],numeros[2])))


