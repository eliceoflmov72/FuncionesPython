# Intercambia dos variables que sean pasadas globales con una función - Apunte a,b = b,a    53
def intercambiar():
    global variable1
    variable1 = int(input("Introduce la variable 1: "))
    global variable2
    variable2 = int(input("Introduce la variable 2: "))
    variable1, variable2 = variable2, variable1
intercambiar()
print(variable1,variable2)