print("---------- Comparador de numero ----------")
num1 = float(input("Introduce el primer numero: "))
num2 = float(input("Introduce el segundo numero: "))

if num1 > num2:
    print(f"El numero {num1} es mayor que {num2}")
elif num1 < num2:
    print(f"El numero {num1} es menor que {num2}")
else:
    print(f"El numero {num1} es igual que {num2}")