import sympy as sp

def secante_metodo(func, x0, x1, tol=1e-9, max_iterations=1000):
    x = sp.symbols('x')

    f_func = sp.lambdify(x, func)

    x_k_menos_1 = x0
    x_k = x1
    iterations = 0

    while True:
        f_x_k_menos_1 = f_func(x_k_menos_1)
        f_x_k = f_func(x_k)

        if abs(f_x_k - f_x_k_menos_1) < tol:
            print("CONVERGE.")
            break

        x_k_mas_1 = x_k - (f_x_k * (x_k - x_k_menos_1)) / (f_x_k - f_x_k_menos_1)

        x_k_menos_1 = x_k
        x_k = x_k_mas_1

        iterations += 1

    return x_k, iterations

# Define the target function
x = sp.symbols('x')
funcion = x**3- 5*x**2 +20

# Initial guesses
x0 = -2.0
x1 = 2.0

# Apply Secant method
root, iterations = secante_metodo(funcion, x0, x1)

# Display the results
print(f"Raiz aproximada: {root}")
print(f"NUm iteraciones: {iterations}")
