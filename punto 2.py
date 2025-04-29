N = int(input("Jugador 1, elige un número secreto: "))
print("\n" * 50)  
adivina = int(input("Jugador 2, intenta adivinar el número: "))
while adivina != N:
    if adivina < N:
        print("Mayor")
    else:
        print("Menor")
    adivina = int(input("Intenta nuevamente: "))
print("¡Correcto!")
