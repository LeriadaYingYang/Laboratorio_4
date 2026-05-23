# UPN - FUNDAMENTOS DE PROGRAMACIÓN LABORATORIO 4
# Daniel Enrique Jara Alva

import subprocess
import sys

from Estructuras import gestionar_estructura_combinada
from lista import listas_paralelas, cadenas
from validacion import metodos


def ejecutar_notas():
    subprocess.run([sys.executable, "Notas.py"])#Se utiliza para ejecutar automáticamente el archivo Notas.py desde el menú principal usando el mismo intérprete de Python cuando el usuario selecciona la opción correspondiente


def main():
    while True:
        print("\n" + "=" * 60)
        print(f"{'MENÚ PRINCIPAL GENERAL':^60}")
        print("=" * 60)
        print("1. Estructuras combinadas y búsqueda por ciudad")
        print("2. Listas paralelas")
        print("3. Manejo de cadenas")
        print("4. Notas, búsqueda y ordenamiento")
        print("5. Validación de cadenas y promedios")
        print("6. Salir")
        print("=" * 60)

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            gestionar_estructura_combinada()

        elif opcion == "2":
            listas_paralelas()

        elif opcion == "3":
            cadenas()

        elif opcion == "4":
            ejecutar_notas()

        elif opcion == "5":
            metodos()

        elif opcion == "6":
            print("\nSaliendo del programa principal...")
            break

        else:
            print("\nOpción inválida. Intente nuevamente.")


if __name__ == "__main__":
    main()