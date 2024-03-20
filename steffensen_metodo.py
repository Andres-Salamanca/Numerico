def steffensen_metodo(f, x0, tol=1e-9, max_iter=100):
    iter = 0
    for i in range(max_iter):
        iter += 1
        x1 =  f(x0)
        x2 = f(x1)
        x3 =  f(x2)
        if x1 == x2 and x1==x3:
          print(f'numero de iteraciones {iter}')
          return x0
        # Aceleración de Aitken
        x_approx = x1 - ((x1 - x2)**2) / (x3 + x1 - 2*x2 )
        
        if abs(x_approx - x0) < tol:
            print(f'numero de iteraciones {iter}')
            return x_approx
        
        x0 = x_approx

    
    # Si no se alcanza la convergencia después del número máximo de iteraciones
    raise ValueError("El método de Steffensen no convergió después de {} iteraciones".format(max_iter))

# Ejemplo de uso:
# Definimos una función de ejemplo y una estimación inicial
def function(x):
    return ((10-x**3)/4)**(1/2)

punto = 1.5

# Usamos el método de Steffensen para encontrar la raíz
root = steffensen_metodo(function, punto)
print("Aproximación de la raíz:", root)
