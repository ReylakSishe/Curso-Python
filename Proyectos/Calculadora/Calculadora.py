def calcular():
    operacionElegida = input("que operacion quiere realizar ")
    a = int(input())
    b = int(input())
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b
    if operacionElegida == "s":
        print(suma)
    if operacionElegida == "r":
        print(resta)
    if operacionElegida == "m":
        print(multiplicacion)
    if operacionElegida == "d":
        print(division)
    calcular()


calcular()
