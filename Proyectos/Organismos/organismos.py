#listas

logones = ["B959263","C569853","T698952","Z698563"]

roles = ["superior","adjunto","temporario","tercerizado"]

contraseñas = ["CHIPI1971","EURASIA","JAJAJANT","ECHENME"]

#intentos

intento = 0
intentoHecho = intento + 1

#funciones

def sumarIntento():
    intento = intentoHecho


def usuarioLogueado():
    logonIngresado = input("ingrese su logon")
    if logonIngresado in logones:
        print("logon correcto")
        rolAsignado()
        
    else:
        print("logon incorrecto")

        if intento > 3:
            print("ya no podes ingresar")


        else:
            print ("intente de nuevo por favor")
            usuarioLogueado()
            sumarIntento()
            
            



def rolAsignado():
    rolIngresado = input("ingrese su rol")
    if rolIngresado in roles:
        print("rol correcto")
        contraseñaPuesta()
        
    else:
        print("rol incorrecto")
        
        if intento > 3:
            print("ya no podes ingresar")

        else:
            print ("intente de nuevo por favor")
            usuarioLogueado()
            sumarIntento()
          

def contraseñaPuesta():
    contraseñaIngresada = input("ingrese su contraseña")
    if contraseñaIngresada in contraseñas:
        print("contraseña correcta, bienvenido de vuelta")
        
    else:
        print("contraseña incorrecta")

        if intento > 3:
            print("ya no podes ingresar")

        else:
            print("intente de nuevo por favor")
            usuarioLogueado()
            sumarIntento()


usuarioLogueado()