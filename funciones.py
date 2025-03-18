global divisiones
divisiones=0
gemelos=[]
def menu():
    men="""
    ******Menu principal********
    1.Encontrar y mostrar numeros
    primos gemelos
    2.Encontrar y mostrar numeros
    primos palindromicos
    3.Salir
    *****************************
    """
    print(men)
    return input("Elija una opciòn: ")

def primos_gemelos():
    global divisiones, e
    mayorrango=int(input("Ingrese el numero limite del rango de busqueda: "))
    ind=1
    if mayorrango>2:
        for i in range(2, mayorrango):
            if i%2==0:
                    divisiones+=1
            elif i%3==0 and i!=3:
                    divisiones+=1
            elif i%5==0 and i!=5:
                  divisiones+=1
            elif i%7==0 and i!=7:
                  divisiones+=1
            elif i%9==0 and i!=9:
                  divisiones+=1
            if divisiones==0:
                    gemelos.append(i)
            divisiones=0
        for gemelo in gemelos:
              if gemelo==gemelos[-1]:
                    print("")
              elif gemelos[ind]-gemelo==2:
                    print(f"({gemelo},{gemelos[ind]})")
              ind+=1
        gemelos.clear()
def primos_palindromos():
        global divisiones
        limite=int(input("Ingrese limite de el rango: "))
        for i in range(10, limite):
            if i%2==0:
                    divisiones+=1
            elif i%3==0:
                    divisiones+=1
            if divisiones==0:
                    gemelos.append(i)
            divisiones=0
        for gem in gemelos:
            carac=str(gem)
            if carac[::-1]==carac:
                  print(gem,",""\n")
        gemelos.clear()


