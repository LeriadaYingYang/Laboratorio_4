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

# ============================================
# PARTE: MANEJO DE CADENAS DE TEXTO
# ============================================

# --- Cadena de texto base ---
texto = "Los estudiantes del curso de Fundamentos de Programación obtuvieron buenas notas"

print("\n" + "=" * 50)
print(f"{'MANEJO DE CADENAS DE TEXTO':^50}")
print("=" * 50)

print(f"\nTexto original:\n{texto}")

# --------------------------------------------
# 1. SUBCADENA (slicing)
# --------------------------------------------
# texto[inicio:fin] extrae caracteres desde el índice inicio hasta fin-1
subcadena = texto[4:14]
print(f"\n1. Subcadena [4:14]: '{subcadena}'")

# --------------------------------------------
# 2. BUSCAR UNA PALABRA (find)
# --------------------------------------------
# find() devuelve el índice donde empieza la palabra buscada
# Si no la encuentra, devuelve -1
palabra_buscar = "Programación"
posicion = texto.find(palabra_buscar)

if posicion != -1:
    print(f"\n2. Palabra '{palabra_buscar}' encontrada en la posición: {posicion}")
else:
    print(f"\n2. Palabra '{palabra_buscar}' no encontrada.")

# --------------------------------------------
# 3. REEMPLAZAR UNA PALABRA (replace)
# --------------------------------------------
# replace(viejo, nuevo) devuelve una nueva cadena con el cambio aplicado
# El texto original NO se modifica
texto_reemplazado = texto.replace("buenas notas", "excelentes resultados")
print(f"\n3. Texto con reemplazo:\n   {texto_reemplazado}")

# --------------------------------------------
# 4. SEPARAR EL TEXTO EN PARTES (split)
# --------------------------------------------
# split() divide el texto por espacios (por defecto) y devuelve una lista
palabras = texto.split()
print(f"\n4. Texto separado en palabras ({len(palabras)} palabras):")
print(f"   {palabras}")

# También se puede dividir por otro separador, por ejemplo una coma
lista_csv = "Ana García,Luis Torres,María Pérez,Carlos Díaz,Sofía Ríos"
nombres_separados = lista_csv.split(",")
print(f"\n   Separado por coma: {nombres_separados}")

print("\n" + "=" * 50)