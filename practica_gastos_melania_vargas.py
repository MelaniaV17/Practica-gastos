# Programa: Gestor de gastos personales
# Descripción: Permite registrar, listar y resumir gastos personales aplicando conceptos avanzados de Python.

# Variable global para llevar el conteo de operaciones de registro realizadas
conteo_registros = 0

def mostrar_menu(simbolo="$"):
    """
    Muestra el menú principal de opciones en la consola.
    Utiliza un parámetro por defecto para representar el símbolo de la moneda.
    Retorna la opción seleccionada por el usuario.
    """
    print("\n========================================")
    print("      GESTOR DE GASTOS PERSONALES       ")
    print("========================================")
    print(f"Símbolo de moneda actual: {simbolo}")
    print("1. Registrar un gasto")
    print("2. Ver el listado de gastos registrados")
    print("3. Ver el resumen de gastos")
    print("4. Salir")
    opcion = input("Seleccione una opción (1-4): ")
    return opcion
