print("Ingrese los nuemeros a calcular")
numero1=int(input("ingrese el primer numero:"))
numero2=int(input("ingrese el segundo numero:"))
operacion=input("selecciona la operacion que desea hacer\n\
S s=Suma\n\
R r= resta\n\
M m= Multiplicacion\n\
D d= Divisio")
opearacion=operacion.lower()
res=0
if operacion=="s":
    res=numero1+numero2
if operacion=="r":
    res=numero1-numero2
if operacion=="m":
    res=numero1*numero2
if operacion=="d":
    if numero2!=0:
        res=nmero1/numero2

print(f"este es el resultado:{res}")