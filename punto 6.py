num = int(input("Ingrese un número entre 0 y 10 para su tabla de multiplicar: "))
if 0 <= num <= 10:
    for i in range(11):
        print(f"{num} x {i} = {num * i}")
else:
    print("Número fuera de rango.")
