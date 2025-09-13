print("----------- MENU ----------")

menu = input("\nBienvenido, ¿que deseas hoy?\n1.Papas fritas.\n2.Pizza.\n3.Hamburguesa.\n").lower()

if menu == "papas" or menu == "papas fritas" or menu == "1":
    print("Excelente eleccion. Tus papas van en camino.")
elif menu == "pizza" or menu == "2":
    print("Excelente eleccion. Tu Pizza viene en camino")
elif menu == "Hamburguesa" or menu == "3":
    print("Excelente eleccion. Tu hambuerguesa viene en camino")
else:
    print("Error: Introduce un producto valido")