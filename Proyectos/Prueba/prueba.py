#programa que verifica si tenes edad esta disponible en la lista



edades = [13,14,15,16,17,18]


def buscarEdad():
    edadElegida = int(input("coloque una edad para ver si esta en la lista"))
    if edadElegida in edades:
        print("la edad esta en la lista")
    else:
        print("la edad no esta en la lista")
        buscarEdad()


buscarEdad()
