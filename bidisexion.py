def f(x):
    return x**x - 9
def bisection_method(a, b, tol=1e-8, max_iter=100):
    if f(a) * f(b) >= 0:
        raise ValueError("Los valores iniciales a y b deben tener signos opuestos.")
    
    iter_count = 0
    while (b - a) / 2 > tol and iter_count < max_iter:
        c = (a + b) / 2.0
        if f(c) == 0:
            return c  # Encontramos la solución exacta
        elif f(c) * f(a) < 0:
            b = c
        else:
            a = c
        iter_count += 1
    
    return (a + b) / 2.0
# Definir los límites iniciales del intervalo donde se buscará la raíz
a = 2.0  # Valor inferior del intervalo
b = 3.0  # Valor superior del intervalo

# Llamar al método de bisección con los valores iniciales y una tolerancia
resultado = bisection_method(a, b)

print("La solución aproximada de x^x = 2 es:", resultado)
