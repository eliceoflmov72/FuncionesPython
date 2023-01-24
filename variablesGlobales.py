# Intercambia dos variables globales con una función - Apunte a,b = b,a 52
variable1 = 1
variable2 = 2
def intercambiar():
    global variable1
    global variable2
    varaible3 = variable1
    variable1 = variable2
    variable2 = varaible3
intercambiar()
print(variable1,variable2)