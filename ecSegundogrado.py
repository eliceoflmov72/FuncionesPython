def resolverEcuacion(a, b ,c):
    """Resuelve una ecuación cuadrática.
    Devuelve en una tupla las dos raíces que resuelven la ecuación cuadrática:
    ax^2 + bx + c = 0.
    Utiliza la fórmula general.
    Parámetros:
    a -- coeficiente cuadrático (debe ser distinto de 0)
    b -- coeficiente lineal
    c -- término independiente
    Excepciones:
    ValueError -- Si (a == 0)
    """
    from math import sqrt
    resultado1 = (-b+sqrt(b**2-4*a*c))/(2*a) 
    resultado2 = (-b-sqrt(b**2-4*a*c))/(2*a) 
    return resultado1,resultado2 #

