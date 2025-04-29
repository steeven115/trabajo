while True:
    num = int(input("Ingrese un número (negativo para salir): "))
    if num < 0:
        break
    print(f"El cuadrado de {num} es {num**2}")
