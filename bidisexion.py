def f(x, c):
    return x**x - c

def bisection_method(a, b, c, tol=1e-8, max_iter=100):
    if f(a, c) * f(b, c) >= 0:
        raise ValueError("Los valores iniciales a y b deben tener signos opuestos.")
    
    iter_count = 0
    while (b - a) / 2 > tol and iter_count < max_iter:
        mid_point = (a + b) / 2.0
        if f(mid_point, c) == 0:
            return mid_point  # Encontramos la solución exacta
        elif f(mid_point, c) * f(a, c) < 0:
            b = mid_point
        else:
            a = mid_point
        iter_count += 1
    
    return (a + b) / 2.0

# Pedir al usuario el valor de c (el valor de la ecuación x^x = c)
c = float(input("Dame el valor de c para la ecuación x^x = c: "))

# Definir los límites iniciales del intervalo donde se buscará la raíz
a = float(input("Dame el primer valor del intervalo a considerar: "))
b = float(input("Dame el segundo valor del intervalo a considerar: "))

# Llamar al método de bisección con los valores iniciales y el valor de c
resultado = bisection_method(a, b, c)

print("La solución aproximada de x^x =", c, "es:", resultado)
