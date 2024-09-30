#Oscar Andres Hernandez Pineda - 2264488-2724

# Definimos la función y su derivada manualmente
def f(x):
    return x**3 + 4*x**2 -10  # Ejemplo: función cúbica

def df(x):
    return 3*x**2 + 8*x  # Derivada de la función cúbica

# Método de Newton-Raphson
def newton_method(x0, error_tolerado, max_iter=100):
    x = x0
    iteraciones = 0  # Contador de iteraciones
    for _ in range(max_iter):
        fx = f(x)
        dfx = df(x)
        if dfx == 0:  # Previene la división por cero
            print("La derivada es cero. No se puede continuar.")
            return None, iteraciones
        
        x_new = x - fx / dfx
        
        iteraciones += 1  # Incrementa el contador de iteraciones
        
        if abs(x_new - x) < error_tolerado:
            return x_new, iteraciones
        
        x = x_new

    print("El método no converge dentro del número máximo de iteraciones.")
    return x, iteraciones

# Ingreso de los valores por parte del usuario
a = float(input("Ingresa el extremo izquierdo del intervalo: "))
b = float(input("Ingresa el extremo derecho del intervalo: "))
error_tolerado = float(input("Ingresa el nivel de error permitido: "))

# Selección de un punto inicial dentro del intervalo
x0 = (a + b) / 2  # Punto medio del intervalo como punto de inicio

# Llamada al método de Newton-Raphson
resultado, iteraciones = newton_method(x0, error_tolerado)

# Verificación de que el resultado está dentro del intervalo
if resultado is not None and a <= resultado <= b:
    print(f"La raíz aproximada es {resultado} con un error menor a {error_tolerado}.")
    print(f"El método convergió en {iteraciones} iteraciones.")
elif resultado is not None:
    print(f"La raíz calculada está fuera del intervalo proporcionado.")
    print(f"El método hizo {iteraciones} iteraciones.")
else:
    print(f"No se pudo encontrar una raíz después de {iteraciones} iteraciones.")
