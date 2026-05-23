# ===========================================================================
# UPN - FUNDAMENTOS DE PROGRAMACIÓN
# TEMA 4: Cadenas de caracteres y arreglos paralelos
# APORTE INDIVIDUAL: Estructuras Combinadas y Búsqueda Textual
# Estudiante: Juan Xavier Sánchez Muñoz
# ===========================================================================

def gestionar_estructura_combinada():
    usuarios = [
        {"nombre": "Elizabeth Huingo", "email": "elizabeth@upn.pe", "ciudad": "Cajamarca"},
        {"nombre": "Fabrizio Alva", "email": "fabrizio@upn.pe", "ciudad": "Lima"},
        {"nombre": "Pablo Ramos", "email": "pablo@upn.pe", "ciudad": "Trujillo"},
        {"nombre": "Daniel Ortiz", "email": "daniel@upn.pe", "ciudad": "Cajamarca"},
        {"nombre": "Luis Torres", "email": "luis.t@upn.pe", "ciudad": "Lima"}
    ]
    print("\n" + "="*60)
    print(f"{'REGISTRO DE NUEVO USUARIO':^60}")
    print("="*60)
    
    nuevo_nombre = input("Ingrese el nombre del nuevo usuario: ").strip()
    nuevo_email = input("Ingrese el email del nuevo usuario: ").strip()
    nueva_ciudad = input("Ingrese la ciudad del nuevo usuario: ").strip()
    usuarios.append({
        "nombre": nuevo_nombre,
        "email": nuevo_email,
        "ciudad": nueva_ciudad
    })
    print("\n¡Usuario agregado correctamente a la estructura combinada!")
    print("\n" + "="*60)
    print(f"{'ESTRUCTURA COMBINADA DE USUARIOS':^60}")
    print("="*60)
    print("Se ha inicializado la lista de diccionarios con los campos:")
    print("[nombre, email, ciudad] de forma exitosa.")
    print("-" * 60)
    while True:
        ciudad_buscar = input("\nIngrese la ciudad para filtrar los usuarios: ").strip()
        print(f"\nResultados de la búsqueda para la ciudad: '{ciudad_buscar}'")
        print("-" * 60)
        coincidencias = 0
        for usuario in usuarios:
            if usuario["ciudad"].lower() == ciudad_buscar.lower():
                print(f"Nombre: {usuario['nombre']:<20} | Email: {usuario['email']:<18} | Ciudad: {usuario['ciudad']}")
                coincidencias += 1
        if coincidencias == 0:
            print("No se encontraron usuarios registrados en esa ciudad.")
        else:
            print(f"\nTotal de coincidencias encontradas: {coincidencias}")
        print("-" * 60)
        continuar = input("\n¿Desea buscar otra ciudad? (S/N): ").strip().upper()
        if continuar != 'S':
            print("Saliendo de la búsqueda de ciudades...")
            break
def main():
    while True:
        print("\n=== MÓDULO: ESTRUCTURAS COMBINADAS ===")
        print("1. Ejecutar simulación de Estructuras y Búsqueda")
        print("2. Salir")
        opcion = input("Seleccione una opción: ").strip()
        if opcion == "1":
            gestionar_estructura_combinada()
        elif opcion == "2":
            print("Saliendo del módulo individual...")
            break
        else:
            print("Opción inválida. Intente nuevamente.")
if __name__ == "__main__":
    main()
    