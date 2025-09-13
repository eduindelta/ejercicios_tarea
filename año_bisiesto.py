print("---------- Año Bisiesto ----------")
print("Coloca el año y determinaremos si es bisiesto")
año = int(input("Introduce el año ejem (2025)"))

año_bisiesto = año % 4 == 0 and año % 100 != 0
año_centenario_bisiesto = año % 400 == 0

if año_bisiesto or año_centenario_bisiesto:
    print(f"EL año {año} es Bisiesto")
else:
    print("El año no es bisiesto")