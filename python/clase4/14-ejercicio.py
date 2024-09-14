# hacer un programa donde el usuario ingrese una frase, se le devolvera la misma frase pero sin espacios en blanco, y un contador de los caracteres de la frase

def frase():

    frase = input("ingrese una frase: ")

    fraseSinEspacios = frase.replace(" ","")

    contador = len(fraseSinEspacios)

    print(f'la frase sin espacios es {fraseSinEspacios}')
    print (f'la frase tiene {contador} caracteres')


frase()