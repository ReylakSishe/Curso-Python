# listas

logones_roles = {
    "B959263": "superior",
    "C569853": "adjunto",
    "T698952": "temporario",
    "Z698563": "tercerizado",
}

contraseñas = ["CHIPI1971", "EURASIA", "JAJAJANT", "ECHENME"]

# intentos


# funciones


def terminar():
    print("sin intentos")


def usuarioLogueado():
    intento = 0
    while intento < 3:
        logonIngresado = input("ingrese su logon")
        if logonIngresado in logones_roles:
            print("logon correcto")
            rolAsignado(logonIngresado)
            break

        else:
            print("logon incorrecto")
            intento += 1
            continue
    if intento == 3:
        terminar()


def rolAsignado(logon):
    intento = 0
    while intento < 3:
        rolIngresado = input("ingrese su rol")
        if rolIngresado == logones_roles[logon]:
            print("rol correcto")
            contraseñaPuesta()
            break

        else:
            print("rol incorrecto")
            intento += 1
            continue
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
            continue
    if intento == 3:
        terminar()


usuarioLogueado()
