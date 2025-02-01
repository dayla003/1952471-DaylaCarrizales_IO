#Espacio muestra de todos los resultados posibles de lanzar 3 dados de 20 caras
for x1 in range(1, 21):
    for x2 in range(1, 21):
        for x3 in range(1, 21):
            print(f"({x1}, {x2}, {x3})")
            print("valor de X= " + str(x1 + x2 + x3))