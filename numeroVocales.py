def vocales(frase):
    cont = 0
    lista = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    for vocal in frase:
        if vocal in lista:
            cont+=1
    return cont
a = "Eliceo"
print(f"Tiene {vocales(a)} vocales.")