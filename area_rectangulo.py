print("---------- Calcular el area de un rectangulo -----------")
print("\nPara calcular el area de un rectangulo por favor, introduce el valor de la altura (h), base (b) y unidad (cm, m)\n")
h = float(input("h= "))
b = float(input("b= "))
unidad = input("Intoduce una unidad (cm, m): ").lower()

a = h * b

print(f"El area del rectangulo es = {a}{unidad}")