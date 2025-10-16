import math
def roots(a, b, c):
    discriminante = (b**2) - (4 * a * c)
    if a == 0:
        if b == 0:
            return "( )"
        else:
            r1 = -c / b
            return f"({r1:.1f})"
    if discriminante > 0:
        r1 = (-b + math.sqrt(discriminante)) / (2 * a)
        r2 = (-b - math.sqrt(discriminante)) / (2 * a)
        return f"({max(r1, r2):.1f}, {min(r1, r2):.1f})"
    elif discriminante == 0:
        r12 = -b / (2 * a)
        return f"({r12:.1f})"
    else:
        return "( )"
def value_y(a, b, c, x):
    y = a * (x**2) + b * x + c
    return y
def to_string(a, b, c):
    return f"f(x) = {a} * X^2 + {b} * X + {c}"
def derivation(a, b, c):
    derivada_a = 2 * a
    derivada_b = b
    return f"f'(x) = {derivada_a}x + {derivada_b}"
def ejecutar_cuadratica():
    print("Solucionador de Ecuaciones Cuadráticas")
    print("Usaremos la forma: f(x) = A*X^2 + B*X + C")
    try:
        a = float(input("\nIntroduce el coeficiente A: "))
        b = float(input("Introduce el coeficiente B: "))
        c = float(input("Introduce el coeficiente C: "))
    except ValueError:
        print("Error: Por favor, ingresa solo valores numéricos para A, B y C.")
        return
    print("")
    ecuacion_str = to_string(a, b, c)
    print(f"La ecuación definida es: {ecuacion_str}")
    raices_str = roots(a, b, c)
    print(f"Sus raíces reales son: {raices_str}")
    derivada_str = derivation(a, b, c)
    print(f"Su función derivada es: {derivada_str}")
    try:
        x_prueba = float(input("\nPara finalizar, introduce un valor de X para evaluar la función: "))
        y_valor = value_y(a, b, c, x_prueba)
        print(f"Al evaluar en X = {x_prueba}, el valor de Y es: {y_valor}")
    except ValueError:
        print("Error al evaluar X.")
    print("")
