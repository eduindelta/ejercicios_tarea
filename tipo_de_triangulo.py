print("Vamos a determinar el tipo de triangulo")
lado1 = float(input("Introduce el primer lado: "))
lado2 = float(input("Introduce el segundo lado: "))
lado3 = float(input("Introduce el tercer lado: "))

if lado1 == lado2 and lado1 == lado3:
    print("El triangulo es un equilatero")
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print("El triangulo es un isosceles")
else:
    print("El triangulo es un escaleno")
