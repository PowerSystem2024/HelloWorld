# hacer un programa que pida una cadena por teclado, luego meter los caracteres en una lista, sin repetirlos

def sinRepetirCaracteres(cadena):

    sinRepetidos = []

    for i in cadena:
        sinRepetidos.append(i)
        sinRepetidosSet = set(sinRepetidos)

    print(sinRepetidosSet)

sinRepetirCaracteres("hola hola hola")
