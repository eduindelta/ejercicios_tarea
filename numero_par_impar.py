num = int(input("Introduce un numero y te digo si es par o impar: "))

resto = num % 2

if resto == 0:
    print("El numero es par")
else:
    print("El numero es impar")