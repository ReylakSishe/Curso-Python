def calcular():
    operacionElegida = input("que operacion quiere realizar ")
    a = int(input())
    b = int(input())
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b
    if operacionElegida == "suma":
        print(suma)
    if operacionElegida == "resta":
        print(resta)
    if operacionElegida == "multiplicacion":
        print(multiplicacion)
    if operacionElegida == "division":
        print(division)
    calcular()


calcular()
