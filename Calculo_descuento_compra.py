#Entrada
compra=int(input("Ingresa el monto total de la compra: "))
if(compra<50):
    print("No hay descuento")
elif(compra>=50 and compra<=100):
    descuento=compra*0.05
    total=compra-descuento
    print("Descuento aplicado:",descuento)
    print("Total a pagar:",total)
elif(compra>100):
    descuento=compra*0.1
    total=compra-descuento
    print("Descuento aplicado:",descuento)
    print("Total a pagar:",total)
