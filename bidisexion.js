function f(x) {
    return Math.pow(x, x) - 2;
}

function bisectionMethod(a, b, tol=1e-8, maxIter=100) {
    if (f(a) * f(b) >= 0) {
        throw "Los valores iniciales a y b deben tener signos opuestos.";
    }

    let iterCount = 0;
    while ((b - a) / 2 > tol && iterCount < maxIter) {
        let c = (a + b) / 2;
        if (f(c) === 0) {
            return c;  // Encontramos la solución exacta
        } else if (f(c) * f(a) < 0) {
            b = c;
        } else {
            a = c;
        }
        iterCount++;
    }

    return (a + b) / 2;
}

// Definir los límites iniciales del intervalo donde se buscará la raíz
let a = 1.0;  // Valor inferior del intervalo
let b = 2.0;  // Valor superior del intervalo

// Llamar al método de bisección con los valores iniciales y una tolerancia
let resultado = bisectionMethod(a, b);

console.log("La solución aproximada de x^x = 2 es:", resultado);
