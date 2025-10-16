def number_to_month(month):
    meses_map = {
        1: "enero",
        2: "febrero",
        3: "marzo",
        4: "abril",
        5: "mayo",
        6: "junio",
        7: "julio",
        8: "agosto",
        9: "septiembre",
        10: "octubre",
        11: "noviembre",
        12: "diciembre" }
    return meses_map.get(month, "error")
def ejecutar_conversor_meses():
    print("Conversor de Número a Mes")
    print("Introduce un número del 1 al 12 para saber a qué mes corresponde.")
    try:
        numero_mes = int(input("Número de mes (1-12): "))
    except ValueError:
        print("Error: Necesitas ingresar un número entero. Por favor, intenta de nuevo.")
        return
    nombre_del_mes = number_to_month(numero_mes) 
    print("Resultado")
    if nombre_del_mes == "error":
        print(f"El número {numero_mes} no está en el rango válido (1-12).")
        print("Retorna: "error"")
    else:
        print(f"El número {numero_mes} corresponde al mes de "{nombre_del_mes}"")
if name == "main":
    ejecutar_conversor_meses()
