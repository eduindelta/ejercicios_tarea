print("---------- Calculadora de descuento ----------")
print("Hola! por tu compra mayor a $100 obtienes un descuento del 15%")
compra = float(input("¿De cuanto fue tu compra?: "))

#Aplicamos formula ya que no se puede restar % directamente
descuento = compra - (15/100)*compra


if compra > 100:
    print("Felicidades obtienes un descuento del 15%. Tu monto a pagar es: $", descuento)
else:
    print("Tu compra es inferior a $100, por lo tanto no obtienes el descuento")