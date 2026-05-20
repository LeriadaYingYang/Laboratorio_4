#=====================================
# PARTE: VALIDACIÓN - Métodos substring, split, replace, etc.
# Curso: Fundamentos de Programación - Tema 4
#=====================================

# Función principal del programa
def metodos():
    # Se pide la cantidad de estudiantes
    cantidad = int(input("N° de estudiantes: "))

    # Listas para almacenar nombres y promedios
    nombres = []
    promedios = []

    # Recorrido mediante el rango de cantidad
    for i in range(cantidad):
        print(f"\nEstudiante N°{i+1}")
        nombre = input("Nombre: ").strip() # Elimina espacios al inicio y al final

        while True:
            promedio = input("Promedio [0-20]: ").strip() # Elimina espacios al inicio y al final
            promedio = promedio.replace(",", ".") # Reemplaza comas por puntos
            partes = promedio.split(".") # Divide el promedio usando "." como separador
            valido = True

    # Validando el formato del promedio
            if len(partes) > 2:
                valido = False
            else:
                if not partes[0].isdigit(): # Verifica que la parte entera sea numérica
                    valido = False
                if len(partes) == 2:
                    decimal = partes[1][:2]
                    if not decimal.isdigit(): # Verifica que la parte decimal sea numérica (si existe)
                        valido = False

    # Rango del promedio
            if valido:
                promedio_num = float(promedio)
                if 0 <= promedio_num <= 20:
                    nombres.append(nombre) # Agrega nombres a su lista
                    promedios.append(promedio_num) # Agrega promedios a su lista
                    break
                else:
                    print("Error: Promedio fuera de rango [0-20]")
            else:
                print("Formato inválido")

    # Lista final de nombres y promedios
    print("\n=== LISTA FINAL ===\n")
    for i in range(cantidad):
        print(nombres[i], "|| Promedio:", promedios[i])

# Menú Principal 
def main():
    
    while True:
        print("\n=== MENÚ PRINCIPAL ===")
        print("1. Listas paralelas")
        print("2. Métodos")
        print("3. Salir")

        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            # listas_paralelas()
            pass
        elif opcion == "2":
            metodos()
        elif opcion == "3":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

#Ejecutar el programa
if __name__ == "__main__":
    main() 