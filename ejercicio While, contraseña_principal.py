contraseña="UCA123"
entrada=""
intentos=0
while entrada!=contraseña and intentos < 3:
    entrada=input("ingrese su contraseña:")
    if entrada!= contraseña:
        print("incorrecta - siga intentando:")
        intentos +=1
if entrada == contraseña:
    print("correcta!!")

else:
    print("no hay mas intentos.")
    