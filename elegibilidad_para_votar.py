edad = int(input("¿que edad tienes?"))
inscrito = input("¿Estas inscrito en el cne? SI/NO ").upper()

if edad >= 18 and inscrito == "SI":
    print("puedes votar")
else:
    print("No puedes votar")