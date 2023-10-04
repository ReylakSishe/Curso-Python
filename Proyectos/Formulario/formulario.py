from datetime import date


def form1():
    nombre = str(input("Nombre: "))
    apellido = str(input("Apelllido: "))
    direccion = str(input("Direccion: "))
    fechaDeActo = input("Fecha de acto (AÑO-MES-DIA): ")
    numeroDeOficina = int(input("Numero de oficina: "))
    logon = str(input("Logon: "))
    provincia = str(input("Provincia: "))
    localidad = str(input("Localidad: "))
    codigoPostal = int(input("Codigo postal: "))
    NumeroDNI = int(input("Numero de DNI: "))

    try:
        fechaDeActo = date.fromisoformat(fechaDeActo)
    except:
        print("Ingrese la fecha en el formato indicado (AÑO-MES-DIA)")

    print("Su acto quedo asi:")
    print("Nombre: ", nombre)
    print("Apellido: ", apellido)
    print("Direccion: ", direccion)
    print("Fecha de acto: ", fechaDeActo)
    print("Numero de oficina: ", numeroDeOficina)
    print("Logon", logon)
    print("Provincia: ", provincia)
    print("Localidad: ", localidad)
    print("Codigo postal: ", codigoPostal)
    print("Numero de DNI: ", NumeroDNI)


form1()
