positivos = []
negativos = []
ceros = 0

for _ in range(10):
    num = int(input("Ingrese un número: "))
    if num > 0:
        positivos.append(num)
    elif num < 0:
        negativos.append(num)
    else:
        ceros += 1

media_positivos = sum(positivos) / len(positivos) if positivos else 0
media_negativos = sum(negativos) / len(negativos) if negativos else 0

print(f"Media de positivos: {media_positivos}")
print(f"Media de negativos: {media_negativos}")
print(f"Cantidad de ceros: {ceros}")
