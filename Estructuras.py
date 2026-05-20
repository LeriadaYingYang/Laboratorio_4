# ===========================================================================
# UPN - FUNDAMENTOS DE PROGRAMACIÓN
# TEMA 4: Cadenas de caracteres y arreglos paralelos
# APORTE INDIVIDUAL: Estructuras Combinadas y Búsqueda Textual
# ===========================================================================

def gestionar_estructura_combinada():
    # Construcción de una estructura combinada (Lista de Diccionarios)
    usuarios = [
        {"nombre": "Elizabeth Huingo", "email": "elizabeth@upn.pe", "ciudad": "Cajamarca"},
        {"nombre": "Fabrizio Alva", "email": "fabrizio@upn.pe", "ciudad": "Lima"},
        {"nombre": "Pablo Ramos", "email": "pablo@upn.pe", "ciudad": "Trujillo"},
        {"nombre": "Daniel Ortiz", "email": "daniel@upn.pe", "ciudad": "Cajamarca"},
        {"nombre": "Luis Torres", "email": "luis.t@upn.pe", "ciudad": "Lima"}
    ]
    
    print("\n" + "="*60)
    print(f"{'ESTRUCTURA COMBINADA DE USUARIOS':^60}")
    print("="*60)
    print("Se ha inicializado la lista de diccionarios con los campos:")
    print("[nombre, email, ciudad] de forma exitosa.")
    print("-" * 60)
    
    # Búsqueda textual dentro de la estructura por campo 'ciudad'
    ciudad_buscar = input("Ingrese la ciudad para filtrar los usuarios: ").strip()
    
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

# Menú local para la ejecución y validación de tu parte
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