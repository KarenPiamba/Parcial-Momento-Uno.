#Entrada
compra=int(input("Ingresa el monto total de la compra"))
if(compra<50):
    print("No hay descuento")
elif(compra>=50 and compra<=100):
    descuento=compra*0.05
    total=compra-descuento
    print("El descuento del cinco porciento es:",descuento)
    print("El total a pagar en la compra es:",total)
elif(compra>100):
    descuento=compra*0.1
    total=compra-descuento
    print("El descuento del cinco porciento es:",descuento)
    print("El total a pagar en la compra es:",total)