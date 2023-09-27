# listas

logones = ["B959263", "C569853", "T698952", "Z698563"]

roles = ["superior", "adjunto", "temporario", "tercerizado"]

contraseñas = ["CHIPI1971", "EURASIA", "JAJAJANT", "ECHENME"]

# intentos


# funciones


def terminar():
    print("sin intentos")


def usuarioLogueado():
    intento = 0
    while intento < 3:
        logonIngresado = input("ingrese su logon")
        if logonIngresado in logones:
            print("logon correcto")
            rolAsignado()

        else:
            print("logon incorrecto")
            intento += 1
    if intento == 3:
        terminar()


def rolAsignado():
    intento = 0
    while intento < 3:
        rolIngresado = input("ingrese su rol")
        if rolIngresado in roles:
            print("rol correcto")
            contraseñaPuesta()

        else:
            print("rol incorrecto")
            intento += 1
    if intento == 3:
        terminar()


def contraseñaPuesta():
    intento = 0
    while intento < 3:
        contraseñaIngresada = input("ingrese su contraseña")
        if contraseñaIngresada in contraseñas:
            print("contraseña correcta")
            print("bienvenido de vuelta")
            break

        else:
            print("contraseña incorrecta")
            intento += 1
    if intento == 3:
        terminar()


usuarioLogueado()
