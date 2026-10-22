
print("=== CALCULADORA ===")
print("1. Sumar")
print("2. Restar")
print("3. Multiplicar")
print("4. Dividir")

opcion = input("Elige una operación introduciendo el número que le corresponde: ")

numero1 = int(input("Introduce el primer número: "))
numero2 = int(input("Introduce el segundo número: "))

if opcion == "1":
    resultado = numero1 + numero2
    print(f"Resultado de la suma: {resultado}")

elif opcion == "2":
    resultado = numero1 - numero2
    print(f"Resultado de la resta: {resultado}")

elif opcion == "3":
    resultado = numero1 * numero2
    print(f"Resultado de la multiplicación: {resultado}")

elif opcion == "4":
    if numero2 != 0:
        resultado = numero1 / numero2
        print(f"Resultado de la división: {resultado}")
    else:
        print("No se puede dividir entre cero.")

else:
    print("Opción no válida.")
