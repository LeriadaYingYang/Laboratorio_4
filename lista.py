#=================================
#Laboratorio 4 -> Listas Paralelas
#Integrante: Elizabeth Huingo 
#=================================

# Función de listas paralelas
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

# Función de cadenas
def cadenas():
    texto = "Bienvenido al laboratorio de listas paralelas"

    # Subcadena
    print("\nSubcadena:")
    print(texto[0:10])  # Imprime "Bienvenido"

    # Buscar palabra
    print("\nBuscar palabra:")
    print(texto.find("laboratorio"))  # Imprime la posición de la palabra "laboratorio"

    # Reemplazar palabra
    print("\nReemplazar palabra:")
    print(texto.replace("listas", "cadenas"))  # Reemplaza "listas" por "cadenas"

    # Split
    print("\nSplit:")
    print(texto.split(" "))  # Divide el texto en palabras y las muestra como una lista

    
# Menu principal
def main():

    while True: 
        print("\n=========MENU=========")
        print("1. Listas Paralelas")
        print("2. Cadenas")
        print("3. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            listas_paralelas()
        elif opcion == "2":
            cadenas()
        elif opcion == "3":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Intente nuevamente.")
