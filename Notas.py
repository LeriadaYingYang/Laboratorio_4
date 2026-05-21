# ============================================
# PARTE: NOTAS - Listas paralelas
# Curso: Fundamentos de Programación - Tema 4
# ============================================

# --- Listas paralelas ---
nombres = ["Ana García", "Luis Torres", "María Pérez", "Carlos Díaz", "Sofía Ríos"]
notas   = [18, 15, 20, 12, 17]

# len() devuelve la cantidad de elementos de la lista
n = len(nombres)

# --------------------------------------------
# FUNCIÓN PARA MOSTRAR LISTA
# --------------------------------------------

# Se define una función para mostrar cualquier lista de nombres y notas
# Recibe: lista_nombres (list), lista_notas (list), titulo (str)
def mostrar_lista(lista_nombres, lista_notas, titulo):
    # Se imprime una línea de separación de 50 caracteres
    print("\n" + "=" * 50)
    # :^50 centra el título dentro de un espacio de 50 caracteres
    print(f"{titulo:^50}")
    print("=" * 50)
    
    # Se recorre la lista por índice para mostrar nombre y nota juntos
    for i in range(len(lista_nombres)):
        print(f"{lista_nombres[i]:<25} | Nota: {lista_notas[i]}")

# --------------------------------------------
# MOSTRAR LISTA ORIGINAL
# --------------------------------------------

# Se llama a la función con las listas originales sin modificar
mostrar_lista(nombres, notas, "LISTA DE ESTUDIANTES Y NOTAS")

# --------------------------------------------
# BÚSQUEDA POR NOMBRE
# --------------------------------------------
print("\n--- BÚSQUEDA POR NOMBRE ---")

# input() captura el nombre escrito por el usuario desde teclado
nombre_buscar = input("Ingrese el nombre del estudiante: ")

# Variable de control: se vuelve True si se encuentra al estudiante
encontrado = False

# Se recorre la lista comparando cada nombre con el buscado
for i in range(n):
    # .lower() convierte ambos textos a minúsculas para comparar
    if nombres[i].lower() == nombre_buscar.lower():
        print(f"\nEstudiante encontrado: {nombres[i]}")
        print(f"Su nota es: {notas[i]}")
        encontrado = True
        # break detiene el ciclo en cuanto se encuentra al estudiante
        break

# Si después del recorrido encontrado sigue siendo False, no existe
if not encontrado:
    print("\nEstudiante no encontrado.")

# --------------------------------------------
# ORDENAMIENTO POR NOTA (Mayor a menor)
# --------------------------------------------
nombres_ord = nombres.copy()
notas_ord = notas.copy()

# Algoritmo de burbuja: compara elementos adyacentes y los intercambia
# Algoritmo de burbuja: compara elementos adyacentes y los intercambia
for i in range(n - 1):
    for j in range(n - 1 - i):
        if notas_ord[j] < notas_ord[j + 1]:
            notas_ord[j], notas_ord[j + 1] = notas_ord[j + 1], notas_ord[j]
            nombres_ord[j], nombres_ord[j + 1] = nombres_ord[j + 1], nombres_ord[j]

mostrar_lista(nombres_ord, notas_ord, "ORDENADOS POR NOTA (Mayor a menor)")

# --------------------------------------------
# ORDENAMIENTO ALFABÉTICO POR NOMBRE
# --------------------------------------------
nombres_alfa = nombres.copy()
notas_alfa = notas.copy()

# Mismo algoritmo de burbuja, pero ahora comparando nombres como texto
for i in range(n - 1):
    for j in range(n - 1 - i):
        # .lower() garantiza comparación sin distinguir mayúsculas o minúsculas
        if nombres_alfa[j].lower() > nombres_alfa[j + 1].lower():
            # Intercambio de nombres para ordenarlos de A a Z
            nombres_alfa[j], nombres_alfa[j + 1] = nombres_alfa[j + 1], nombres_alfa[j]
            # Se intercambian las notas en paralelo
            notas_alfa[j], notas_alfa[j + 1] = notas_alfa[j + 1], notas_alfa[j]

mostrar_lista(nombres_alfa, notas_alfa, "ORDENADOS ALFABÉTICAMENTE")

print("\n" + "=" * 50)