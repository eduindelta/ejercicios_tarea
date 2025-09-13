print("----------El mayor de 3 numeros----------")
num1 = float(input("Introduce el primer numero: "))
num2 = float(input("Introduce el segundo numero: "))
num3 = float(input("Introduce el tercer numero: "))

if num1 > num2 and num1 > num3:
    print(f"El primer numero ({num1}) es el mayor de los que ingresaste")
elif num2 > num1 and num2 > num3:
    print(f"El segundo numero ({num2}) es el mayor de los que ingresaste")
else:
    print(f"El tercer numero ({num3}) es el mayor de los que ingresaste")