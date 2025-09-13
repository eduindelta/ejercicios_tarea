#Enunciado: Escribe un programa que verifique si una contraseña introducida por el usuario es "contraseña123". 
# Si lo es, imprime "Acceso concedido"; de lo contrario, imprime "Acceso denegado".

contraseña = input("Introduce tu contraseña: ")

if contraseña == ("contraseña123"):
    print("Acceso concedido")
    
else:
    print("Acceso denegado")

