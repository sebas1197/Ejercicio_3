import random

def opcion1():
    print("Se ha seleccionado la opción 1.")

def opcion2():
    print("Se ha seleccionado la opción 2.")

def opcion3():
    print("Se ha seleccionado la opción 3.")

def opcion4():
    print("Se ha seleccionado la opción 4.")

def opcion5():
    print("Se ha seleccionado la opción 5.")

def opcion6():
    print("Se ha seleccionado la opción 6.")

def menu():
    vector = []

    for i in range(50):
        valor = random.randint(1, 500)
        vector.append(valor)

    matriz = []

    for i in range(5):
        fila = []
        for j in range(5):
            valor = random.randint(1, 500)
            fila.append(valor)
        matriz.append(fila)


    print("Seleccione una opción:")
    print("1. Mostrar vector y matriz de datos")
    print("2. Ordenar vector")
    print("3. Suma total vector")
    print("4. Suma total matriz")
    print("5. Primos del vector")
    print("6. Impares de la matriz")
    print("7. Ordenar matriz")
    print("8. Salir")

    opcion = input("Ingrese el número de opción: ")

    if opcion == "1":
        opcion1()
    elif opcion == "2":
        opcion2()
    elif opcion == "3":
        opcion3()
    elif opcion == "4":
        opcion4()
    elif opcion == "5":
        opcion5()
    elif opcion == "6":
        opcion6()
    elif opcion == "7":
        print("Has seleccionado la opción 7.")
    elif opcion == "8":
        print("Saliendo del programa...")
        exit()
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")


while True:
    menu()
