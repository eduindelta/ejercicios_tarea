print("---------- Calculadora IMC ----------")
peso = float(input("Introduce tu peso (Kg): "))
altura = float(input("Introduce tu altura (m): "))

imc = peso / altura**2

if imc < 0:
    print("Error: no puedes introducir numeros negativos")
elif imc < 18.5:
    print(f"Tu IMC es de: {imc}\nClasificacion: Peso Insuficiente (IMC menor a 18.5)")
elif imc >= 18.5 and imc <= 24.9:
    print(f"Tu IMC es de: {imc}\nClasificacion: Peso Normal (IMC de 18.5 a 24.9)")
elif imc >= 25 and imc < 30:
    print(f"Tu IMC es de: {imc}\nClasificacion: Sobrepeso (IMC de 25 a 29.9)")
elif imc >= 30 and imc < 35:
    print(f"Tu IMC es de: {imc}\nClasificacion: Obesidad Clase 1 (IMC de 30 a 34.9)")
elif imc >= 35 and imc < 40:
    print(f"Tu IMC es de: {imc}\nClasificacion: Obesidad Clase 2 (IMC de 35 a 39.9)")
else:
    print(f"Tu IMC es de: {imc}\nClasificacion: Obesidad Clase 3 (IMC mayor a 40)")