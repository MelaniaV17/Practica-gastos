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

def calcular_resumen(lista_gastos):
    """
    Calcula y retorna múltiples valores:
    el total gastado, el promedio por gasto y el gasto de mayor monto.
    """
    if len(lista_gastos) == 0:
        return 0.0, 0.0, None

    total = sum(gasto['monto'] for gasto in lista_gastos)
    promedio = total / len(lista_gastos)

    # Se busca el gasto con el monto máximo utilizando una función lambda como clave
    gasto_mayor = max(lista_gastos, key=lambda x: x['monto'])

    return total, promedio, gasto_mayor

def mostrar_resumen(lista_gastos):
    """
    Muestra el resumen de gastos utilizando la función de cálculo múltiple
    y formateando los resultados obligatoriamente con f-strings a dos decimales.
    """
    print("\n----------------------------------------")
    print("          RESUMEN DE GASTOS             ")
    print("----------------------------------------")

    if len(lista_gastos) == 0:
        print("No hay suficientes datos para generar un resumen.")
    else:
        # Llamada a función que retorna múltiples valores
        total, promedio, gasto_mayor = calcular_resumen(lista_gastos)

        print(f"Total gastado: ${total:.2f}")
        print(f"Promedio por gasto: ${promedio:.2f}")
        print(f"Gasto de mayor monto: {gasto_mayor['descripcion']} con ${gasto_mayor['monto']:.2f}")

def main():
    """
    Función principal que controla el flujo de ejecución del programa y el bucle del menú.
    """
    gastos = []

    # Bucle principal que se repite hasta que el usuario decide salir
    while True:
        # Llamada a función utilizando argumentos con nombre
        opcion = mostrar_menu(simbolo="$")

        if opcion == "1":
            registrar_gasto(lista_gastos=gastos)
        elif opcion == "2":
            mostrar_listado(gastos)
        elif opcion == "3":
            mostrar_resumen(gastos)
        elif opcion == "4":
            print(f"\nCantidad total de operaciones de registro realizadas: {conteo_registros}")
            print("¡Gracias por utilizar el gestor de gastos personales. Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, seleccione un número entre 1 y 4.")

# Bloque de ejecución principal
if __name__ == "__main__":
    main()
