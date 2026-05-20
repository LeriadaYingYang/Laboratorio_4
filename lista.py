nombres = ["María", "Pedro", "Ana", "Luis"]
edades = [20, 19, 22, 24]

print("LISTA DE ESTUDIANTES")
for i in range(len(nombres)):
    print(nombres[i], "-", edades[i], "años")

buscar = input("\nIngrese el nombre a buscar: ")
if buscar in nombres:
    posicion = nombres.index(buscar)
    print("Edad:", edades[posicion])
else:
    print("El nombre no se encuentra en la lista.")