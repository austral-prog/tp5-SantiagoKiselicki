def max_of_two(x, y):
    if x > y:
        return x
    else:
        return y
def max_of_three(x, y, z):
    max_xy = max_of_two(x, y)
    return max_of_two(max_xy, z)
def ejecutar_calculo_maximos():
    print("Calculadora de Máximos entre Números")
    print("Verificación con 2 Números")
    try:
        a = float(input("Introduce el primer número (x): "))
        b = float(input("Introduce el segundo número (y): "))
        resultado_dos = max_of_two(a, b)
        print(f"El número más grande entre {a} y {b} es: {resultado_dos}")
    except ValueError:
        print("Error: Asegúrate de ingresar solo valores numéricos.")
        return
    print("Verificación con 3 Números")
    try:
        c = float(input("Introduce el primer número (x): "))
        d = float(input("Introduce el segundo número (y): "))
        e = float(input("Introduce el tercer número (z): "))
        resultado_tres = max_of_three(c, d, e)
        print(f"El número más grande entre {c}, {d} y {e} es: {resultado_tres}")
    except ValueError:
        print("Error: Asegúrate de ingresar solo valores numéricos.")
        return
if name == "main":
    ejecutar_calculo_maximos()
