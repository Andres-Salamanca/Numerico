import sympy as sp

def newton_raphson(func, initial_guess, tol=1e-9):


  f_prime_x = sp.diff(func, x)
  f_func = sp.lambdify(x, func)
  f_prime_func = sp.lambdify(x, f_prime_x)

  x_value = initial_guess
  iterations = 0

  while True:
    f_x_value = f_func(x_value)
    f_prime_x_value = f_prime_func(x_value)

    if abs(f_prime_x_value) < tol:
        print("La derivada es cercana a cero. Es posible que el método de Newton-Raphson no converja.")
        break

    x_value = x_value - (f_x_value / f_prime_x_value)
    iterations += 1

    if abs(f_x_value) < tol:
        break



  return x_value, iterations


# Define the target function
x = sp.symbols('x')
funcion = x**3- 5*x**2 +20

# Initial guess
initial_guess = 1.0

# Apply Newton-Raphson method
root, iterations = newton_raphson(funcion, initial_guess)

# Display the results
print(f"Raiz aproximada: {root}")
print(f"NUm iteraciones: {iterations}")
