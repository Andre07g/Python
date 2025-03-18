from funciones import menu, primos_gemelos, primos_palindromos
from funciones import divisiones, gemelos
print("Bienvenido")
while True:
    op=menu()
    if op=="1":
        primos_gemelos()
    elif op=="2":
        primos_palindromos()
    elif op=="3":
        print("Saliendo...")
        break
    else: print("Ingrese una opciòn valida")
