for i in range(100000):
    contador = f"{i:05d}"  # Rellenar con ceros a la izquierda
    contador = contador.replace('3', 'E')  # Reemplazar los 3 por E
    print('-'.join(contador))
