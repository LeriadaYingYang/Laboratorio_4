#=================================
#Laboratorio 4 -> Listas Paralelas
#Integrante: Elizabeth Huingo 
#=================================

# Funcion principal 
def listas_paralelas():

    nombres = ["Maria", "Pedro", "Ana", "Luis"]
    edades = [20, 19, 22, 24]

    # Mostrar la lista de estudiantes con sus edades
    print("\nLISTA DE ESTUDIANTES")

    for i in range(len(nombres)):
        print(nombres[i], "-", edades[i], "años")

    # Buscar estudiante 
    buscar = input("\nIngrese el nombre a buscar: ")
    if buscar in nombres:

        # Obtener la posicion
        posicion = nombres.index(buscar)
        # Mostrar la edad del estudiante
        print("Edad:", edades[posicion])
    else:
        print("El nombre no se encuentra en la lista.")
    
# Menu principal
def main():

    while True:
        print("\n=========MENU=========")
        print("1. Listas Paralelas")
        print("2. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            listas_paralelas()
        elif opcion == "2":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

# Ejecutar el programa
if __name__ == "__main__":
    main()