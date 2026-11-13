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

    def registrar_gasto(lista_gastos):
    """
    Solicita al usuario una descripción y un monto positivo.
    Actualiza la variable global de conteo e inserta el gasto en la lista.
    Retorna un único valor booleano indicando si el registro fue exitoso.
    """
    global conteo_registros

    descripcion = input("Ingrese la descripción del gasto: ").strip()
    try:
        monto = float(input("Ingrese el monto del gasto: "))

        # El monto deberá ser un número mayor que cero
        if monto > 0:
            gasto = {"descripcion": descripcion, "monto": monto}
            lista_gastos.append(gasto)
            conteo_registros += 1
            print("¡Gasto registrado con éxito!")
            return True
        else:
            print("Error: El monto debe ser un número mayor a cero.")
            return False
    except ValueError:
        print("Error: Debe ingresar un valor numérico válido para el monto.")
        return False

def mostrar_listado(lista_gastos):
    """
    Muestra en pantalla el listado numerado de todos los gastos registrados,
    indicando la descripción y el monto con dos decimales usando f-strings.
    """
    print("\n----------------------------------------")
    print("         LISTADO DE GASTOS              ")
    print("----------------------------------------")

    if len(lista_gastos) == 0:
        print("No existen gastos registrados actualmente.")
    else:
        # Se recorre la lista mostrando el índice numerado desde 1
        for i, gasto in enumerate(lista_gastos, start=1):
            print(f"{i}. Descripción: {gasto['descripcion']} | Monto: ${gasto['monto']:.2f}")
    print("2. Ver el listado de gastos registrados")
    print("3. Ver el resumen de gastos")
    print("4. Salir")
    opcion = input("Seleccione una opción (1-4): ")
    return opcion
