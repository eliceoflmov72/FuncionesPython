# Aqui comienza la primera función de descuento
def calcularDescuento(precio):
    """Se calcula el descuento del 30%.

Devuelve un descuento a partir de un precio:
precio = precio * 0.30
Esta sería la formula general para hacer un descuento a un precio dado

Parámetros:
precio -- Variable que recibirá un precio, se presupone que es positiva

Excepciones:
ValueError -- Si (str(precio), o recibe letras)
"""
    precio = precio*0.30
    return precio


# Aquí comienza la segunda función del desucneto del IVA
def calcularIva(precio):
    """Se calcula el descuento del 21% del IVA.

Devuelve un descuento a partir de un precio:
precio = precio * 0.21
Esta sería la formula general para hacer un descuento a un precio dado

Parámetros:
precio -- Variable que recibirá un precio, se presupone que es positiva

Excepciones:
ValueError -- Si (str(precio), o recibe letras)
"""
    precio = precio * 0.21
    return precio