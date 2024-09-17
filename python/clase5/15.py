# crear una funcion para calcular el total del pago incluyendo un iimpuesto aplica (iva)

def calculadora():

    precioBruto = int(input("ingrese el precio bruto de su compra: "))
    precioIva = precioBruto + (precioBruto * 0.21)

    print(f"el total de su compra es de {precioIva}")

calculadora()