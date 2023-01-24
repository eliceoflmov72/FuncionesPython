import math
def cambiarCordenadas():
    r = int(input("Introduce coordenada radio: "))
    a = int(input("Introduce alpha: "))
    x = r * math.cos(a)
    y = r * math.sin(a)
    print(f"Las coordenadas son {x},{y}")
cambiarCordenadas()
