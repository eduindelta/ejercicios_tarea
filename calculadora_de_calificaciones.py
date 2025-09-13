print("Calculadora de notas")
nota = int(input("Introduce tu nota del 0 al 100: "))

if nota < 0 or nota > 100:
    print("Error: introduce una nota valida(0 al 100)")
elif nota >= 90:
    print("Tu nota es 'A'")
elif nota >= 80:
    print("Tu nota es 'B'")
elif nota >= 70:
    print("Tu nota es 'C'")
elif nota >= 60:
    print("Tu nota es 'D'")
else:
    print("Tu nota es 'F'")