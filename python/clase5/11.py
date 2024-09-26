def listaTerminos(**termino):
    for llave, valor in termino.items():
        print(f"{llave} : {valor}")

listaTerminos(IDE = "integrated developmet envirometn", pk = "primary key")
