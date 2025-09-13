print("------ Verificador de vocal o consonante ------")

letra = input("Introduce una letra: ").lower()

if len(letra) == 1 and letra.isalpha():
    
    if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
        print("Esta letra es una vocal")
    else:
        print("Esta letra es una consonante")
else:
    print("Error: debes introducir un unico caracter del alfabeto.")