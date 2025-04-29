N = int(input("¿Cuántos sueldos va a ingresar?: "))
sueldos = []

for _ in range(N):
    sueldo = float(input("Ingrese sueldo: "))
    sueldos.append(sueldo)

print(f"El sueldo máximo es {max(sueldos)}")
