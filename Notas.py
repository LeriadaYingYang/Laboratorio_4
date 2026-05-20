# ============================================
# PARTE: NOTAS - Listas paralelas
# Curso: Fundamentos de Programación - Tema 4
# ============================================

# --- Listas paralelas ---
nombres = ["Ana García", "Luis Torres", "María Pérez", "Carlos Díaz", "Sofía Ríos"]
notas   = [18, 15, 20, 12, 17]

n = len(nombres)

# --------------------------------------------
# FUNCIÓN PARA MOSTRAR LISTA
# --------------------------------------------
def mostrar_lista(lista_nombres, lista_notas, titulo):
    print("\n" + "=" * 50)
    print(f"{titulo:^50}")
    print("=" * 50)
    
    for i in range(len(lista_nombres)):
        print(f"{lista_nombres[i]:<25} | Nota: {lista_notas[i]}")

# --------------------------------------------
# MOSTRAR LISTA ORIGINAL
# --------------------------------------------
mostrar_lista(nombres, notas, "LISTA DE ESTUDIANTES Y NOTAS")

# --------------------------------------------
# BÚSQUEDA POR NOMBRE
# --------------------------------------------
print("\n--- BÚSQUEDA POR NOMBRE ---")
nombre_buscar = input("Ingrese el nombre del estudiante: ")

encontrado = False

for i in range(n):
    if nombres[i].lower() == nombre_buscar.lower():
        print(f"\nEstudiante encontrado: {nombres[i]}")
        print(f"Su nota es: {notas[i]}")
        encontrado = True
        break

if not encontrado:
    print("\nEstudiante no encontrado.")

# --------------------------------------------
# ORDENAMIENTO POR NOTA (Mayor a menor)
# --------------------------------------------
nombres_ord = nombres.copy()
notas_ord = notas.copy()

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

for i in range(n - 1):
    for j in range(n - 1 - i):
        if nombres_alfa[j].lower() > nombres_alfa[j + 1].lower():
            nombres_alfa[j], nombres_alfa[j + 1] = nombres_alfa[j + 1], nombres_alfa[j]
            notas_alfa[j], notas_alfa[j + 1] = notas_alfa[j + 1], notas_alfa[j]

mostrar_lista(nombres_alfa, notas_alfa, "ORDENADOS ALFABÉTICAMENTE")

print("\n" + "=" * 50)