# Arreglos paralelos con más alumnos y notas.
nombres = ["Ana", "Luis", "Carlos", "Marta", "Pedro", "Lucía", "Jorge", "Sofía"]
notas = [15.5, 18.0, 12.5, 19.5, 10.0, 16.5, 14.0, 17.0]

# Mostrar lista
print("Lista de estudiantes y sus notas (0-20):")
for i in range(len(nombres)):
    print(f"{i+1}. {nombres[i]} : {notas[i]:.1f}")

# Búsqueda por nombre
def buscar_nota(nombre_buscar):
    for i in range(len(nombres)):
        if nombres[i].lower() == nombre_buscar.lower():
            return notas[i]
    return None

# Prueba de búsqueda
nombre = input("\nIngrese nombre a buscar: ")
nota = buscar_nota(nombre)
if nota is not None:
    print(f"La nota de {nombre} es {nota:.1f}")
else:
    print(f"{nombre} no encontrado")

# Ordenar alfabéticamente los nombres
pares = list(zip(nombres, notas))
pares.sort(key=lambda x: x[0])
nombres_ordenados, notas_ordenadas = zip(*pares)

print("\nLista ordenada alfabéticamente:")
for i, (n, nota) in enumerate(zip(nombres_ordenados, notas_ordenadas), 1):
    print(f"{i}. {n} : {nota:.1f}")

# Ordenar por nota descendente (extra, demostración)
pares_nota = list(zip(nombres, notas))
pares_nota.sort(key=lambda x: x[1], reverse=True)
print("\nRanking por nota (de mayor a menor):")
for i, (n, nota) in enumerate(pares_nota, 1):
    print(f"{i}. {n} : {nota:.1f}")

# Promedio del grupo
promedio = sum(notas) / len(notas)
print(f"\nPromedio del grupo: {promedio:.2f}")